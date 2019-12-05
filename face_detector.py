import cv2

# Get a reference to webcam 
video_capture = cv2.VideoCapture("bald.mp4") # CHANGE THIS TOT THE WEBCAM

# Initialize variables
face_locations = []

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    #load cascade classifier training file for haarcascade
    haar_face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

    #let's detect multiscale (some images may be closer to camera than others) images
    faces = haar_face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5)

    # Display the results
    for top, right, bottom, left in faces:
        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2) # CODE FOR OTHER GROUPS GOES IN HERE

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()