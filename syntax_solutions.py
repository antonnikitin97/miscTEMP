from sr.robot import *

R = robot()    # Capital 'R' in robot.


def drive_forward(speed):
    r.motors[].m0.power = speed    # Capital R in R.motor. [0] avoids syntax error
    r.motors[].m1.power = speed    # "


def drive_backwards(speed):
    r.motors[].m0.power = -speed    # Same problems but won't be caught as it is never run.
    R.motors[].m1.power = -speed


def look_for_token_markers()    # Missing ':'
    markers = R.see()
   arena_markers = []    # Bad indentation
    for m in markers:
        if m.info.marker_type = MARKER_ARENA:    # Should be '==' instead.
            arena_markers.append(m)
    return arena_markers

while True:
    markers = look_for_token_markers()
    if markers:
        Drive_forward(20)    # Should be lower-case 'd'
