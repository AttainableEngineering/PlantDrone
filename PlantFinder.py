import cv2
import numpy as np

# Dictionary with file handles, and directory for images
fhs = {1 : "Plants1.png", 2 : "Plants2.png", 3 : "Plants3.png", 4 : "Plants4.png", 5 : "Plants5.png", 6 : "Plants6.png", 7 : "Plants7.png"}
dr = r"Drone\\"
file = dr + fhs[5]
print("\n"+file+"\n")

# Read and show image of interest
image = cv2.imread(file, cv2.IMREAD_COLOR)

cv2.imshow("Image", image)
cv2.waitKey(0)

# Convert image to HSV color-space
hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

# HSV Green Values - - adjust threshhold
green_low = (36, 25, 25)
green_high = (86, 255, 255)
mask = cv2.inRange(hsv, green_low, green_high)

# Isolate green
iso = mask > 0
green = np.zeros_like(image, np.uint8)
green[iso] = image[iso]

cv2.imshow("Isolated Greens",green)
cv2.waitKey(0)
