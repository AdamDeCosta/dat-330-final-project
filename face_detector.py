import cv2

# Get a reference to webcam 
video_capture = cv2.VideoCapture("bald.mp4") # CHANGE THIS TO THE WEBCAM

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

