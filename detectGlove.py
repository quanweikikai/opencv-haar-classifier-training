#! /usr/bin/python

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import glob
import sys

cascadeDict = sys.argv[1]

def countPix(image, colorFlt):
	row, col,ept = image.shape
	count = 0
	for i in xrange(row):
		for j in xrange(col):
			cntFlg = True
			for k in xrange(3):
				if not (image[i,j,k]<colorFlt[k*2+1] and image[i,j,k]>colorFlt[k*2]):
					cntFlg = False
			if cntFlg:
				count +=1
	return count

def detectObj(imgPath):
	img = cv.imread(imgPath)
	img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
	plotIMG = np.copy(img)
	face_cascade = cv.CascadeClassifier(cascadeDict)
	faces = face_cascade.detectMultiScale(img, 1.1, 5)
	#colorFilter = (74,126,74,128,105,188)
	colorFilter = (79,97,95,110,118,121)
	for (x,y,w,h) in faces:
		x_ctr = x+w/2
		y_ctr = y+h/2
		subImg = img[y_ctr-15:y_ctr+15,x_ctr-15:x_ctr+15,:]
		if  x == 2261:
			for k in xrange(3):
				plt.hist(subImg[:,:,k].ravel(),256,[0,256])
				plt.show()

		pixRate = countPix(subImg, colorFilter)/900.0
		print pixRate
		if pixRate >= 0.000:
			cv.rectangle(plotIMG,(x_ctr-20,y_ctr-20),(x_ctr+20,y_ctr+20),(255,0,0),2)

	#plt.imshow(plotIMG)
	#plt.show()
	fileName = imgPath[:-12] + "/result/" + imgPath[-12:]
	#cv.imwrite(fileName,plotIMG)
	plt.imsave(fileName,plotIMG)
	#cv.namedWindow('image')
	#while (1):
	#	cv.imshow("image",img)
	#	key = cv.waitKey(20)
	#	if key & 0xFF == 27:
	#		break
	#cv.destroyAllWindows()
		
		
if __name__ == "__main__":
	vec_directory = "../train"
	files = glob.glob('{0}/*.jpg'.format(vec_directory))
	for f in sorted(files): 
		detectObj(f)
	
