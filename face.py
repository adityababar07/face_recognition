import face_recognition
import numpy as np
from cv2 import cv2
import os
import time


starttime = time.time()

folder = "media"
files = os.listdir(folder)
video = cv2.VideoCapture('source.mp4')

known_face_encodings = []
known_face_names = []

for image in files:
    face = face_recognition.load_image_file(f"{folder}/{image}")
    face_encoding = face_recognition.face_encodings(face)[0]
    known_face_encodings.append(face_encoding)
    image = image[:-4]
    known_face_names.append(image)

face_locations = []
face_encoding2 = []
process_this_frame = True

while True:
    # grabbing a single frame
    ret, frame = video.read()
    time.sleep(0.01)
    try:
        # converting the frame to small for faster encoding
        small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

        # converting bgr to RGB
        rgb = small_frame[:, :, ::-1]

        if process_this_frame: 
            face_locations = face_recognition.face_locations(rgb)
            face_encodings2 = face_recognition.face_encodings(
                rgb, face_locations)
            face_names = []

            for face_encoding in face_encodings2:
                matches = face_recognition.compare_faces(
                    known_face_encodings, face_encoding, tolerance=0.52)
                name = "Unknown"
                face_distances = face_recognition.face_distance(
                    known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                face_names.append(name)

        process_this_frame = not process_this_frame

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 2
            right *= 2
            bottom *= 2
            left *= 2
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, bottom-(-20)),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

        cv2.namedWindow('', cv2.WINDOW_NORMAL)
        cv2.imshow('', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except:
        print("finished")
video.release()
cv2.destroyAllWindows()

print('That took {} seconds'.format(time.time() - starttime))
