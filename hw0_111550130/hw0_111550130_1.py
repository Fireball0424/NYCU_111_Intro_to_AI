#library 
import cv2 as cv

# read the image and txt
img = cv.imread(cv.samples.findFile("image.png"))
with open("bounding_box.txt") as file : 
    box_str = file.read()
box = list(map(int, box_str.split()))

# Draw boxes 
sz = len(box)
i = 0
while i < sz : 
    x1 = box[i]
    y1 = box[i + 1]
    x2 = box[i + 2]
    y2 = box[i + 3]
    i = i + 4
    cv.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

# Display and write 
cv.imshow("Display window", img)
close_input = cv.waitKey(0)
if close_input == ord("s") :
    cv.imwrite("hw0_111550130_1.png", img)
