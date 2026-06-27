import cv2

image = cv2.imread("Loaded Image.png")

sizes = [(200, 200), (300, 300), (400, 400)]

for width, height in sizes:
    resized = cv2.resize(image, (width, height))

    cv2.imshow(f"{width}x{height}", resized)

    cv2.imwrite(f"Resized_{width}x{height}.png", resized)

    print(f"Resized image: {resized.shape}")

    cv2.waitKey(0)
    cv2.destroyAllWindows()