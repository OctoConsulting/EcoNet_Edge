import av
import numpy as np
from dataclasses import dataclass
from collections import defaultdict, OrderedDict
from klvdata import streamparser
from klvdata.element import UnknownElement
from klvdata.common import packet_checksum, bytes_to_hexstr
from argparse import ArgumentTypeError as ArgpTypeError
from enum import Enum


class FixSizeOrderedDict(OrderedDict):
    def __init__(self, *args, **kwds):
        self.size_limit = kwds.pop("size_limit", None)
        OrderedDict.__init__(self, *args, **kwds)
        self._check_size_limit()

    def __setitem__(self, key, value):
        OrderedDict.__setitem__(self, key, value)
        self._check_size_limit()

    def _check_size_limit(self):
        if self.size_limit is not None:
            while len(self) > self.size_limit:
                self.popitem(last=False)

def parse_packets(pts, packet_data, verbose=False):
    """ parses mpegts packet into frame (rgb, thermal) and data (klv, flight gui))"""
    # TODO: implement flight gui parsing

    for pk in streamparser.StreamParser(packet_data):

        try:
            # flir gui information is an unknown packet type
            if isinstance(pk, UnknownElement):
                if verbose:
                    print("UnKno Key: {}".format(":".join(["{:02x}".format(c) for c in pk.key])))
                return None
            else:
                if verbose:
                    print("Known Key: {}".format(":".join(["{:02x}".format(c) for c in pk.key])))

            if packet_checksum(packet_data) != pk.items[b'\x01'].value.value:
                if verbose:
                    print("Parsing Error: Bad Checksum")
                return None

            # no key
            if b'\x01' not in pk.items:
                if verbose:
                    print("Parsing Error: KLV start byte not found")
                return None
            # yes key
            else:
                # default dictionary makes for easier checking
                meta = defaultdict(lambda: None)
                meta.update({v.LDSName: str(v.value.value) for k, v in pk.items.items() if hasattr(v, 'LDSName')})
                meta["meta_timestamp_int"] = pts
                meta["Checksum"] = bytes_to_hexstr(pk.items[b'\x01'].value.value)
                return meta

        except Exception as e:
            if verbose:
                print('Error Decoding KLV packet')
            return None

def decode_stream_old(source):

    timed_latest_meta_data_buffer = FixSizeOrderedDict(size_limit=3)

    with av.open(source) as container:
        for i, packet in enumerate(container.demux()):

            # check if packet is klv packet
            # don't need because it parrot does some encode and sending packet whole.
            # if packet.stream.type == 'data':
            #     meta_data = parse_packets(packet.pts, packet.to_bytes(), verbose=False)

            #     # check if meta data is valid and update latest instance
            #     # None type is returned on unknown packet types
            #     if meta_data is not None:
            #         timed_latest_meta_data_buffer[packet.pts] = meta_data

            if packet.stream.type == 'video':

                for frame in packet.decode():

                    frame = frame.to_ndarray(format='bgr24')

                    # frame could be thermal or color
                    # color (480, 640, 3)
                    # thermal (240, 320, 3)

                    # return only the color images
                    if frame.shape == (480, 640, 3):

                        meta_pts = packet.pts
                        meta_data = None

                        if len(timed_latest_meta_data_buffer) > 0:

                            # pair packets with matching pts times (default to latest time if no match exists)
                            if packet.pts in timed_latest_meta_data_buffer:
                                meta_data = timed_latest_meta_data_buffer[packet.pts]
                            # take last value
                            else:
                                meta_pts = next(reversed(timed_latest_meta_data_buffer))
                                meta_data = timed_latest_meta_data_buffer[meta_pts]

                        # print("Presentation Time Stamp Pair: {} {}".format(meta_pts, packet.pts))

                        yield meta_pts, meta_data, packet.pts, frame

class Platform(Enum):
    BT = 0
    BT3 = 1

@dataclass()
class DataFrame:

    pts: int = None
    _meta: dict = None
    platform: Platform = None

    t = None
    r = None
    ccm = None
    tcm = None

    rgb: np.ndarray = np.array([])
    thermal: np.ndarray = np.array([])
    rgb_mask: np.ndarray = np.array([])
    thermal_mask: np.ndarray = np.array([])

    @property
    def meta(self):
        return self._meta

    @meta.setter
    def meta(self, _meta):
        self._meta = _meta
        self.platform = Platform.BT if _meta['Platform Designation'][-2:].strip() == '3' else Platform.BT3

    def filled(self):
        if self.meta is None:
            return False

        if self.platform == Platform.BT:
            return bool(len(self.rgb))
        else:
            return bool(len(self.rgb) and len(self.thermal))

        return False

def decode_stream(source):
    size_limit = 3
    dataframe_buffer = FixSizeOrderedDict(size_limit=size_limit)

    with av.open(source) as container:
        for i, packet in enumerate(container.demux()):

            # if packet.stream.type == 'data':
            #     meta = parse_packets(packet.pts, packet.to_bytes(), verbose=False)

            #     if meta is not None:
            #         df = dataframe_buffer.get(packet.pts, DataFrame())
            #         df.pts = packet.pts
            #         df.meta = meta
            #         dataframe_buffer[packet.pts] = df
            #     else:
            #         print()
            if packet.stream.type == 'video':
                for frame in packet.decode():
                    frame = frame.to_ndarray(format='bgr24')

                    df = dataframe_buffer.get(packet.pts, DataFrame())
                    df.pts = packet.pts

                    if frame.shape == (480, 640, 3):
                        df.rgb = frame

                    if frame.shape == (240, 320, 3):
                        df.thermal = frame
                    else:
                        print()
                    dataframe_buffer[packet.pts] = df
                    yield frame

            # df = dataframe_buffer[next(iter(dataframe_buffer))]
            # if df.filled():
            #     dataframe_buffer.popitem(last=False)
            #     yield df

def str_to_bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise ArgpTypeError('Boolean value expected.')
