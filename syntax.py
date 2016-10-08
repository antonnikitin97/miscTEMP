from sr.robot import *

R = Robot()


def driveForward(speed):
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = speed


def driveBackwards(speed):
    R.motors[0].m0.power = -speed
    R.motors[0].m1.power = -speed


def lookForTokenMarkers():
    markers = R.see()
    arena_markers = []
    for m in markers:
        if m.info.marker_type == MARKER_ARENA:
            arena_markers.append(m)
    return arena_markers

while True:
    markers = lookForTokenMarkers()
    if markers:
        driveForward(20)

