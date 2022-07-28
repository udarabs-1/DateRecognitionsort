import cv2
from matplotlib import pyplot as plt

# Define our imshow function
def imshow(title = "Image", image = None, size = 12):
    w, h = image.shape[0], image.shape[1]
    aspect_ratio = w/h
    plt.figure(figsize=(size * aspect_ratio,size))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()

image = cv2.imread('./main.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
(thresh, blackAndWhiteImage) = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)
imshow('main', blackAndWhiteImage)

# Load Template image
template = cv2.imread('./sub.jpg')
grayty   = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
(thresh, blackAndWhiteImage1) = cv2.threshold(grayty, 45, 255, cv2.THRESH_BINARY)
imshow('sub', blackAndWhiteImage1)

result = cv2.matchTemplate(blackAndWhiteImage, blackAndWhiteImage1, cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

#Create Bounding Box
top_left = max_loc
bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])
cv2.rectangle(image, top_left, bottom_right, (0,0,255), 5)

imshow('Where is Waldo?', image)
