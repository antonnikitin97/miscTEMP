from sr.robot import *

R = robot()

def driveForward(speed):
    R.motors[].m0.power = speed
    r.motors[].m1.power = speed

def driveBackwards(speed):
    R.motors[].m0.power = -speed
    R.motors[].m1.power = -speed

def lookForTokenMarkers():
	markers = R.see
       	token_markers = []
	for m in markers
		if m.info.marker_type = MARKER_TOKEN:
			token_markers.append(m)
	return token_markers

while True:
	markers = lookForTokenMarkers()
	if markers:
		DriveForward(20)
