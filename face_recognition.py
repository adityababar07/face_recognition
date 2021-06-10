from cv2 import cv2

# load trained_face_data
trained_face_data = cv2.CascadeClassifier(
    "/media/hacker07/Hacker07/code/face_recognition/haarcascade_eye.xml")

image = cv2.imread(
    '/media/hacker07/Hacker07/code/face_recognition/185025482_485513809315784_5303460256642576007_n.jpg')

grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detect the face
face_coordinates = trained_face_data.detectMultiScale(
    grey_image,
    scaleFactor=1.2,
    minNeighbors=7,
    minSize=(20, 20)
   )

# drawing a box around the face

for (x, y, w, h) in face_coordinates:
    cv2.rectangle(image, (x, y), ((x+w), (y+h)), (0, 250, 0), 3)
# saving to dataset
    # cv2.imwrite(
    #     '/media/hacker07/Hacker07/code/face_recognition/media/185025482_485513809315784_5303460256642576007_n.jpg', grey_image[y:y+h, x:x+w])
# showing image
cv2.imshow('face_detector', image)
cv2.waitKey()
cv2.destroyAllWindows()
