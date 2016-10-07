from sr.robot import *

R = Robot()

def driveForward(speed):
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = speed

def driveBackwards(speed):
    r.motors[0].m0.power = -speed
    R.motors[0].m1.power = -speed

def lookForTokenMarkers():
	markers = R.see()
       	token_markers = []
	for m in markers:
		if m.info.marker_type == MARKER_TOKEN:
			token_markers.append(m)
	return token_markers

while True:
	markers = lookForTokenMarkers()
	if markers:
		driveForward(20)
