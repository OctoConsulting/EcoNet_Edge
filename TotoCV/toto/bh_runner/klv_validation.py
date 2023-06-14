import os


def valid_video_file(video_file):
    if not os.path.exists(video_file):
        raise OSError('video file {} does not exists'.format(video_file))
    if not video_file.endswith('mpg'):
        raise TypeError('video file does not end with mpg')
    return video_file


def validate_ip(s):
    a = s.split('.')
    if len(a) != 4:
        raise TypeError("address must contain 4 octets")
    for x in a:
        if not x.isdigit():
            raise TypeError("address octets must be numbers")
        i = int(x)
        if i < 0 or i > 255:
            raise TypeError("address octets must be between 0-255")
    return s


def valid_port(s):
    if not s.isdigit():
        raise TypeError("port must be a number")
    return s


def validate_klv(klv):

    if klv is None:
        return False

    valid_check = \
    [
        klv["Sensor Latitude"],
        klv["Sensor Longitude"],
        klv["Sensor Ellipsoid Height"],
        klv["Sensor Relative Elevation Angle"],
        klv["Platform Heading Angle"],
        klv["Sensor Horizontal Field of View"],
        klv["Sensor Vertical Field of View"],
        klv["Frame Center Latitude"],
        klv["Frame Center Longitude"],
        klv["Frame Center Height Above Ellipsoid"],
        klv['Corner Latitude Point 1 (Full)']
    ]

    return None not in valid_check