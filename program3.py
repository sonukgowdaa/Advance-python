import cv2

# Read image
image = cv2.imread("sample.png")

if image is None:
    print("Image not found!")

else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Thresholding
    ret, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Display images
    cv2.imshow("Original Image", gray)
    cv2.imshow("Threshold Image", threshold)

    print("Thresholding applied successfully.")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
