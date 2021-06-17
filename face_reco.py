import os
from cv2 import cv2

# load trained_face_data
trained_face_data = cv2.CascadeClassifier(
    "/media/hacker07/Hacker07/code/face_recognition/haarcascade_frontalface_default.xml")
# media = os.listdir("media")
# for images in media:

image = cv2.imread("/media/hacker07/Hacker07/code/face_recognition/media/49435463_246259366289537_750400105396723221_n.jpg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

canny_image = cv2.Canny(image, 150, 150)

# detect the face
face_coordinates = trained_face_data.detectMultiScale(
     gray_image,
     scaleFactor=1.2,
     minNeighbors=7,
     minSize=(20, 20)
     )

# drawing a box around the face

for (x, y, w, h) in face_coordinates:
     cv2.rectangle(image, (x, y), ((x+w), (y+h)), (0, 250, 0), 3)
     print(x, y, w, h)

# saving to dataset
    # cv2.imwrite(
    #     '/media/hacker07/Hacker07/code/face_recognition/media/185025482_485513809315784_5303460256642576007_n.jpg', grey_image[y:y+h, x:x+w])

# showing image
cv2.imshow('face_detector', image)
cv2.waitKey()
cv2.destroyAllWindows()
