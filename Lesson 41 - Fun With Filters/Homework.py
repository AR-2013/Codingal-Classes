import cv2
import numpy as np

def apply_color_filter(image, filter_type, red_intensity, green_intensity, blue_intensity):
    filtered_image = image.copy()

    if filter_type == "red_tint":
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 0] = 0

    elif filter_type == "blue_tint":
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 2] = 0

    elif filter_type == "green_tint":
        filtered_image[:, :, 0] = 0
        filtered_image[:, :, 2] = 0

    filtered_image[:, :, 2] = np.clip(
        filtered_image[:, :, 2].astype(np.int16) + red_intensity, 0, 255
    ).astype(np.uint8)

    filtered_image[:, :, 1] = np.clip(
        filtered_image[:, :, 1].astype(np.int16) + green_intensity, 0, 255
    ).astype(np.uint8)

    filtered_image[:, :, 0] = np.clip(
        filtered_image[:, :, 0].astype(np.int16) + blue_intensity, 0, 255
    ).astype(np.uint8)

    return filtered_image


image_path = input("Enter the image filename: ")
image = cv2.imread(image_path)

if image is None:
    print("Error! This image was not found.")
else:
    filter_type = "original"

    red_intensity = 0
    green_intensity = 0
    blue_intensity = 0

    print()
    print("Press the following keys to apply filters:")
    print("r = red tint")
    print("b = blue tint")
    print("g = green tint")
    print("o = original image")
    print()
    print("Adjust RGB intensity:")
    print("i = increase red")
    print("d = decrease red")
    print("j = increase green")
    print("f = decrease green")
    print("k = increase blue")
    print("v = decrease blue")
    print()
    print("s = save image")
    print("q = quit")

    while True:
        filtered_image = apply_color_filter(
            image,
            filter_type,
            red_intensity,
            green_intensity,
            blue_intensity
        )

        cv2.imshow("Filtered Image", filtered_image)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("r"):
            filter_type = "red_tint"

        elif key == ord("b"):
            filter_type = "blue_tint"

        elif key == ord("g"):
            filter_type = "green_tint"

        elif key == ord("o"):
            filter_type = "original"
            red_intensity = 0
            green_intensity = 0
            blue_intensity = 0

        elif key == ord("i"):
            red_intensity = min(red_intensity + 10, 255)
            print("Red intensity:", red_intensity)

        elif key == ord("d"):
            red_intensity = max(red_intensity - 10, -255)
            print("Red intensity:", red_intensity)

        elif key == ord("j"):
            green_intensity = min(green_intensity + 10, 255)
            print("Green intensity:", green_intensity)

        elif key == ord("f"):
            green_intensity = max(green_intensity - 10, -255)
            print("Green intensity:", green_intensity)

        elif key == ord("k"):
            blue_intensity = min(blue_intensity + 10, 255)
            print("Blue intensity:", blue_intensity)

        elif key == ord("v"):
            blue_intensity = max(blue_intensity - 10, -255)
            print("Blue intensity:", blue_intensity)

        elif key == ord("s"):
            filename = input("Enter a filename to save the image: ")

            if not filename.lower().endswith((".png", ".jpg", ".jpeg")):
                filename += ".png"

            cv2.imwrite(filename, filtered_image)
            print("Image saved as", filename)

        elif key == ord("q"):
            print("Exiting...")
            break

        else:
            print("Not valid! Please choose one of the available keys.")

    cv2.destroyAllWindows()