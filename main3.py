import cv2

# Load the pre-trained Haar Cascade classifier for human detection
human_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# Load the video file
cap = cv2.VideoCapture('D:\Human detection\pexels-free-videos-853889-1920x1080-25fps.mp4')

# Loop through the frames in the video
while cap.isOpened():
    # Read the frame
    ret, frame = cap.read()
    
    # If the frame is successfully read
    if ret:
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect humans in the frame
        humans = human_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
        
        # Draw rectangles around the detected humans
        for (x, y, w, h) in humans:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # Display the frame with the detected humans
        cv2.imshow('frame', frame)
        
        # Exit if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release the video capture and close the window
cap.release()
cv2.destroyAllWindows()
