import face_recognition
import os
import cv2
import time
def detect_faces(dataset_path="dataset", delay_time=30):
    known_faces = {}
    # Load known faces from the dataset
    for person_folder in os.listdir(dataset_path):
        person_path = os.path.join(dataset_path, person_folder)
        if os.path.isdir(person_path):
            person_images = []
            for image_file in os.listdir(person_path):
                image_path = os.path.join(person_path, image_file)
                person_images.append(face_recognition.load_image_file(image_path))
            # Encode and store face encodings for the person
            person_face_encodings = [face_recognition. 
            face_encodings(image)[0] for image in 
            person_images]
            known_faces[person_folder] =  person_ face _ 
            encodings
    # Main loop for video capture and face detection
    cap = cv2.VideoCapture(0)  
   # Initialize video capture (use 0 for default camera)
    processed_faces = {name: False for name in known _ 
    faces.keys()}
    detected_names = []
    start_time = time.time()
    while True:
        ret, frame = cap.read()  
# Read a frame from the video capture
        # Find all face locations and face encodings in the frame
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)
        # Check if any known face is detected
        for face_encoding in face_encodings:
            for name, known_encodings in known_faces.items():
                # Compare the detected face with known faces
                if not processed_faces[name]:
                    matches = face_recognition.compare_ faces 
                    (known_encodings, face_encoding, 
                    tolerance=0.5)
                    if True in matches:
                        detected_names.append(name)
                        processed_faces[name] = True
        # Display the video frame with face rectangles
for face_location in face_locations:
            top, right, bottom, left = face_location
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 
            255), 2)
        # Display the frame
        cv2.imshow('Video', frame)
        # Check if the delay time has elapsed, then break the 
        loop
        if time.time() - start_time >= delay_time:
            break
        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # Release the video capture and close all windows
    cap.release()
    cv2.destroyAllWindows()
    return detected_names
# Call the function to detect faces for 30 seconds and get the names
