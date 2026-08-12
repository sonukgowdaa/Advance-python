import cv2

# Open webcam
cap = cv2.VideoCapture(0)

# Variables
drawing = False
start_point = None
end_point = None

# Store all completed lines
lines = []

# Mouse callback function
def draw_line(event, x, y, flags, param):
    global drawing, start_point, end_point, lines

    # Mouse button pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_point = (x, y)
        end_point = (x, y)

    # Mouse moved while holding the button
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            end_point = (x, y)

    # Mouse button released
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        end_point = (x, y)

        # Save the completed line
        lines.append((start_point, end_point))


# Create window and set mouse callback
cv2.namedWindow("Webcam")
cv2.setMouseCallback("Webcam", draw_line)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to access webcam.")
        break

    # Draw all saved lines
    for start, end in lines:
        cv2.line(frame, start, end, (0, 255, 0), 2)

    # Draw the current line while dragging
    if drawing and start_point is not None:
        cv2.line(frame, start_point, end_point, (0, 255, 0), 2)

    # Show webcam
    cv2.imshow("Webcam", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()