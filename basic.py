import cv2

img = cv2.imread ("C:\\Users\\LEBITSO\\Pictures\\2019 campaign\\FB_IMG.jpg", 1)

resized = cv2.resize(img, (300, 200))
cv2.imshow("politician", resized)

cv2.waitKey(4000)

cv2.destroyAllWindows()

