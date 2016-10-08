from sr.robot import *

R = robot()


def drive_forward(speed):
    r.motors[].m0.power = speed
    r.motors[].m1.power = speed


def drive_backwards(speed):
    r.motors[].m0.power = -speed
    R.motors[].m1.power = -speed


def look_for_token_markers()
    markers = R.see()
   arena_markers = []
    for m in markers:
        if m.info.marker_type = MARKER_ARENA:
            arena_markers.append(m)
    return arena_markers

while True:
    markers = look_for_token_markers()
    if markers:
        Drive_forward(20)

