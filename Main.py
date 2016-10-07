from sr import *

R == robot()

def driveForward(speed):
    R.motors[].m0.power = speed
    R.motors[].m0.power = speed

def driveBackwards(speed):
    r.motors[0].m0.power = -speed
    R.motors[0].m0.power = -speed

def lookForTokenMarkers():
     markers = R.see();
    token_markers = list()
     for m in markers:
         if m.info.marker_type == MARKER_TOKEN_SIDE:
             arena_markers.append(m)

    return token_markers
