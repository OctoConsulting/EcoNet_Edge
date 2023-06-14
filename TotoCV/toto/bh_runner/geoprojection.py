import numpy as np
from scipy.spatial.transform import Rotation as R
from pyproj import Proj

proj = Proj("+proj=utm +zone=18 +north +ellps=WGS84 +datum=WGS84 +units=m +no_defs")


def project_to_world_with_klv(klv, detc):

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
        klv["Frame Center Height Above Ellipsoid"]
    ]

    if None in valid_check:
        return None
    else:
        valid_check = [float(x) for x in valid_check]
        return project_to_world(*valid_check, detc, proj)


def frame_corners(meta):
    clat = 'Corner Latitude Point {} (Full)'
    clon = 'Corner Longitude Point {} (Full)'

    # check if valid corenrs present
    if not meta[clon.format(1)]:
        return None

    v = [(meta[clon.format(x)], meta[clat.format(x)]) for x in range(1, 5)]

    return [proj(x, y) for x, y in v]


def project_to_world(slat, slon, salt, sea, sh, shfov, svfov, fclat, fclon, fcalt, detc, prj):
    """takes in the meta data and pixel space detection, reprojects out the detection into lat lon"""

    east, north = prj(slon, slat)

    if (fclon > -179):
        eastCenter, northCenter = prj(fclon, fclat)

        viewVector = np.array([eastCenter - east, northCenter - north, fcalt - salt])
        viewVector = viewVector / np.linalg.norm(viewVector)
        rightVector = np.cross(viewVector, np.array([0, 0, 1]))
        upVector = np.cross(rightVector, viewVector)
        r = np.transpose(np.array([viewVector, rightVector, upVector]))
    else:
        r = R.from_euler('xyz', [[0, -sea, 90 - sh]], degrees=True)
        r = r[0].as_matrix()

    x = float(detc[0])
    y = float(detc[1])
    v = np.array([1, np.tan(np.pi * shfov * (x - 320.0) / 320.0 / 360.0),
                  np.tan(np.pi * svfov * (240.0 - y) / 240.0 / 360.0)])

    v = v / np.linalg.norm(v)
    ray = np.matmul(r, v)

    AGL = np.float64(salt - fcalt)

    rayLen = AGL / (-ray[2])
    sensorLoc = np.array([east, north, salt])
    targetLocation = sensorLoc + rayLen * ray
    linLon, linLat = prj(targetLocation[0], targetLocation[1], inverse=True)

    return targetLocation[0], targetLocation[1], linLon, linLat