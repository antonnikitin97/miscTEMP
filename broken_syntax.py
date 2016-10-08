from sr.robot import *

R = robot()


def driveForward(speed):
    r.motors[].m0.power = speed
    r.motors[].m1.power = speed


def driveBackwards(speed):
    r.motors[].m0.power = -speed
    R.motors[].m1.power = -speed


def lookForTokenMarkers()
    markers = R.see()
   arena_markers = []
    for m in markers:
        if m.info.marker_type = MARKER_ARENA:
            arena_markers.append(m)
    return arena_markers

while True:
    markers = lookForTokenMarkers()
    if markers:
        DriveForward(20)

