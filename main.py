import cv2

# Load the HOG descriptor for human detection
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Load the image and resize it
image = cv2.imread("humimg.jpg")
image = cv2.resize(image, (640, 480))

# Detect humans in the image
(rects, weights) = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05)

# Draw rectangles around the detected humans
for (x, y, w, h) in rects:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

# Display the image with detected humans
cv2.imshow("Human Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
