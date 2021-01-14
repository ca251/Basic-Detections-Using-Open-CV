import cv2

# here we`re creating a cascade classifier object
face_cascade = cv2.CascadeClassifier('C:\\Users\\LEBITSO\\PycharmProject\\demo')

# Reading the image
img = cv2.imread("FB_IMG.jpg")

# reading the image as gray scale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# searching for the co-ordinates of the image
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

# we will then use a for loop method to put a rectangle shape around the face(s)p
for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

resized = cv2.resize(img, (int(img.shape[1] / 7), int(img.shape[0] / 7)))

cv2.imshow("politician", resized)

cv2.waitKey(0)

cv2.destroyAllWindows()
