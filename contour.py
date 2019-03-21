from scipy.spatial import distance as dist
import numpy as np
import cv2
from imutils import contours
from imutils import perspective
from matplotlib import pyplot as plt
import imutils


def midpoint(ptA, ptB):
	return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

def get_size(img):
	# img = cv2.imread('../banana4.jpg')
	# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(img, (7, 7), 0)

	edged = cv2.Canny(gray, 50, 100)
	edged = cv2.dilate(edged, None, iterations=1)
	edged = cv2.erode(edged, None, iterations=1)

	# countour for object dimension
	cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[0] if imutils.is_cv2() else cnts[1]

	height_cm = 0
	width_cm = 0

	if(len(cnts) == 0):
		return {'image' : img, 'width' : width_cm, 'height' : height_cm, 'size' : 0}

	(cnts, _) = contours.sort_contours(cnts)

	pixelsPerMetric = None

	for c in cnts:
		# if the contour is not sufficiently large, ignore it
		if cv2.contourArea(c) < 200:
			continue
	 
		# compute the rotated bounding box of the contour
		orig = img.copy()
		box = cv2.minAreaRect(c)
		box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
		box = np.array(box, dtype="int")
	 
		# order the points in the contour such that they appear
		# in top-left, top-right, bottom-right, and bottom-left
		# order, then draw the outline of the rotated bounding
		# box
		box = perspective.order_points(box)
		cv2.drawContours(orig, [box.astype("int")], -1, (0, 255, 0), 2)
	 
		# loop over the original points and draw them
		for (x, y) in box:
			cv2.circle(orig, (int(x), int(y)), 5, (0, 0, 255), -1)

		(tl, tr, br, bl) = box
		(tltrX, tltrY) = midpoint(tl, tr)
		(blbrX, blbrY) = midpoint(bl, br)
	 
		# compute the midpoint between the top-left and top-right points,
		# followed by the midpoint between the top-righ and bottom-right
		(tlblX, tlblY) = midpoint(tl, bl)
		(trbrX, trbrY) = midpoint(tr, br)
	 	
	 	# print "Height Inch: " , round(bl[1] / 75)
	 	# print "Width Inch: " ,  round(br[0] / 75)

	 	
	 	height_cm = round((blbrY - tltrY) / 75) * 2.54
	 	width_cm = round((trbrX - tlblX) / 75) * 2.54
	 	width_ = (trbrX - tlblX)
	 	height_ = ( blbrY - tltrY )
	 	size_ = ( blbrY - tltrY ) * (trbrX - tlblX)
		# draw the midpoints on the image
		cv2.circle(orig, (int(tltrX), int(tltrY)), 5, (255, 0, 0), -1)
		cv2.circle(orig, (int(blbrX), int(blbrY)), 5, (255, 0, 0), -1)
		cv2.circle(orig, (int(tlblX), int(tlblY)), 5, (255, 0, 0), -1)
		cv2.circle(orig, (int(trbrX), int(trbrY)), 5, (255, 0, 0), -1)
	 
		# draw lines between the midpoints
		cv2.line(orig, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)),
			(255, 0, 255), 2)
		cv2.line(orig, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)),
			(255, 0, 255), 2)

		# cv2.imshow("Image", orig)
		return {'image' : orig, 'width' : width_cm, 'height' : height_cm, 'size' : size_}
		break		