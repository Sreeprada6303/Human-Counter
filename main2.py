import cv2

# Open the video file
cap = cv2.VideoCapture('D:\Human detection\pexels-free-videos-853889-1920x1080-25fps.mp4')

# Check if the video file was successfully opened
if not cap.isOpened():
    print("Error opening video file")

# Read and display the first frame of the video
ret, frame = cap.read()
cv2.imshow('Video', frame)

# Process each frame of the video
while cap.isOpened():
    # Read a frame from the video
    ret, frame = cap.read() 

    # Check if the frame was successfully read
    if not ret:
        break

    # Display the frame
    cv2.imshow('Video', frame)
    # Detect humans in the image
    
   

# Draw rectangles around the detected humans
    for (x, y, w, h) in rects:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    # Wait for a key press to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
