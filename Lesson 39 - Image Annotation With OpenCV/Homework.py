import cv2

image = cv2.imread("Image.png")

height, width = image.shape[:2]

y = height // 2

cv2.arrowedLine(image, (0, y), (width // 2, y), (0, 255, 0), 2)
cv2.arrowedLine(image, (width, y), (width // 2, y), (0, 255, 0), 2)

text = f"Width: {width} px"

font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.8
thickness = 2

(text_width, text_height), _ = cv2.getTextSize(text, font, font_scale, thickness)

text_x = (width - text_width) // 2
text_y = y - 15

cv2.putText(image, text, (text_x, text_y), font, font_scale, (255, 0, 0), thickness)

cv2.imwrite("output_images/annotated_width.png", image)

cv2.imshow("Annotated Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()