import cv2

# Read image
image = cv2.imread("sample.png")

if image is None:
    print("Image not found!")

else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Histogram Equalization
    equalized = cv2.equalizeHist(gray)

    # Display images
    cv2.imshow("Original Grayscale", gray)
    cv2.imshow("Histogram Equalized Image", equalized)

    print("Histogram Equalization completed successfully.")

    cv2.waitKey(0)
    cv2.destroyAllWindows()

