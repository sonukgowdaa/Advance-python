import cv2
import numpy as np

# Read image
image = cv2.imread("sample.png")

if image is None:
    print("Image not found!")

else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Create kernel
    kernel = np.ones((5,5), np.uint8)

    # Perform erosion
    erosion = cv2.erode(gray, kernel, iterations=1)

    # Perform dilation
    dilation = cv2.dilate(gray, kernel, iterations=1)

    # Display images
    cv2.imshow("Original Image", gray)
    cv2.imshow("Erosion", erosion)
    cv2.imshow("Dilation", dilation)

    print("Morphological operations completed successfully.")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
