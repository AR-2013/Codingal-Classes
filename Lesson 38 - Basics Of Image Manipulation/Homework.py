import cv2

image = cv2.imread("Image.png")

rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

brightened = cv2.convertScaleAbs(rotated, x=1.0, y=50)

cropped = brightened[50:250, 50:250]

cv2.imshow("Original Image", image)
cv2.imshow("Rotated Image", rotated)
cv2.imshow("Brightened Image", brightened)
cv2.imshow("Cropped Image", cropped)

cv2.imwrite("Edited_Image.png", cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()