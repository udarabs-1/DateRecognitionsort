from easyocr import Reader
import cv2
import time

image = cv2.imread("cropped.png")
cv2.imshow("Original Image", image)
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

reader = Reader(['en'], gpu = True)

ts = time.time()

results = reader.readtext(grayImage)
te = time.time()
td = te - ts
print(f'Completed in {td} seconds')

print(results)