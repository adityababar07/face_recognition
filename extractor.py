# from mysql.connector import Error
# import dlib
# import mysql.connector
from cv2 import cv2

name_of_person = input("enter name of the person :-\t")
face_id = int(input("enter face id :- \t"))

# load trained_face_data
trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

file_no = 0
for i in range(389):
    file_no += 1
    image = cv2.imread(f'{name_of_person}/{file_no}.jpg')

# convert the image to greyscale
    grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#detect the face
    face_coordinates = trained_face_data.detectMultiScale(
    grey_image, 
    scaleFactor=1.2, 
    minNeighbors=7, 
    minSize=(20, 20)
    )

    with open(f"{name_of_person}_coordinates", "a") as f:
        data = f"\n{face_coordinates}"
        f.write(data)
        f.close()

# drawing a box around the face
    try:
        for (x, y, w, h) in face_coordinates:
            cv2.rectangle(image, (x, y), ((x+w), (y+h)), (0, 250, 0), 3)
# saving to dataset
        cv2.imwrite(f'datasets/{name_of_person}/{name_of_person}.{face_id}.{file_no}.jpg', grey_image[y:y+h, x:x+w])
    except:
        print(f"face not found {file_no}")
# showing image
    # cv2.imshow('face_detector', image)
    cv2.waitKey()
    cv2.destroyAllWindows()
