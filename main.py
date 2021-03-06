# import the necessary packages
import numpy as np
import argparse
import cv2
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())
# load the image
image = cv2.imread(args["image"])
# define the list of boundaries
boundaries = [
	([0, 0, 80], [201, 39, 255]),
	([0, 88, 111], [85, 255, 255]),
]
# loop over the boundaries

i = 0
for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
 
	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)
 
	# show the images
	cv2.imshow("imagenes", np.hstack([image, output]))
	if i == 0 :
		cv2.imwrite("rojo.jpg",output)
	else:
		cv2.imwrite("amarillo.jpg",output)
	i+=1
	cv2.waitKey(0)