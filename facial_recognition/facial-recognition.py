import cv2
import face_recognition as fr

# Load images
photo_A = fr.load_image_file('img/henry.jpg')
photo_B = fr.load_image_file('img/jennifer.jpg')


# Images to rgb
photo_A = cv2.cvtColor(photo_A, cv2.COLOR_BGR2RGB)
photo_B = cv2.cvtColor(photo_B, cv2.COLOR_BGR2RGB)

# Face locations
location_face_A = fr.face_locations(photo_A)[0]
encoded_face_A = fr.face_encodings(photo_A)[0]

location_face_B = fr.face_locations(photo_B)[0]
encoded_face_B = fr.face_encodings(photo_B)[0]

# Show rectangle
cv2.rectangle(photo_A,
              (location_face_A[3], location_face_A[0]),
              (location_face_A[1], location_face_A[2]),
              (0, 255, 0),
              2)

cv2.rectangle(photo_B,
              (location_face_B[3], location_face_B[0]),
              (location_face_B[1], location_face_B[2]),
              (0, 255, 0),
              2)

# Make comparison
result = fr.compare_faces([encoded_face_A], encoded_face_B, 0.6)
print(result)

# Measure distance
distance = fr.face_distance([encoded_face_A], encoded_face_B)
print(distance)

# Show result
cv2.putText(photo_A,
            f'{result} {distance.round(2)}',
            (50, 50),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (0, 255, 0),
            2)

# show images
cv2.imshow('Photo A', photo_A)
cv2.imshow('Photo B', photo_B)

# Keep running the program
cv2.waitKey(0)
