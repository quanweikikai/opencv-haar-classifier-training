#! /usr/bin/python

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import glob

side = 20
X,Y = 25, 25

def draw_circle(event,x,y,flags,param):
    global X,Y
    if event == cv.EVENT_LBUTTONUP:
		#cv.circle(img,(x,y),100,(255,0,0),-1)
		print x,y
		X = x
		Y = y

def cropImg(filename,baseImg):
	global X, Y
	cv.namedWindow('image')
	cv.setMouseCallback('image',draw_circle)
	while (1):
		img = np.copy(baseImg)
		cv.rectangle(img,(X-side,Y-side),(X+side,Y+side),(255,0,0),2)
		cv.imshow("image",img)
		key = cv.waitKey(20)
		if key & 0xFF == 27:
			subImg = baseImg[Y-side:Y+side,X-side:X+side,:]
			fileName = filename[:-12] + "/crop/" + filename[-12:]
			cv.imwrite(fileName,subImg)
			break
		if key & 0xFF == 110:
			break
	cv.destroyAllWindows()

if __name__ == "__main__":
	vec_directory = "../train"
	files = glob.glob('{0}/*.jpg'.format(vec_directory))
	for f in sorted(files):
		baseImg = cv.imread(f)
		cropImg(f,baseImg)
