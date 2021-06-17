import face_recognition
import numpy as np
import cv2

face_1 = face_recognition.load_image_file("/media/hacker07/Hacker07/code/face_recognition/media/185025482_485513809315784_5303460256642576007_n.jpg")
face_1_encoding = face_recognition.face_encodings(face_1)[0]
