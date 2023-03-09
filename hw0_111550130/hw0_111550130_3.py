# library 
import numpy as np 
import cv2 as cv 

# read the img 
img = cv.imread(cv.samples.findFile("image.png"))
height = img.shape[0]
width = img.shape[1]

# Translation 
tx = height / 5
ty = width / 8
transition_matrix = np.array([
    [1, 0, tx],
    [0, 1, ty]
], dtype=np.float32)

img_tran = cv.warpAffine(img, transition_matrix, dsize = (width, height))
cv.imwrite('img_tran.jpg', img_tran)

# Rotation 
img_90_CW = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
cv.imwrite('img_90_CW.jpg', img_90_CW)

img_90_CCW = cv.rotate(img, cv.ROTATE_90_COUNTERCLOCKWISE)
cv.imwrite('img_90_CCW.jpg', img_90_CCW)

img_180 = cv.rotate(img, cv.ROTATE_180)
cv.imwrite('img_180.jpg', img_180)

# Flipping 
img_UD_flip = cv.flip(img, 0)
cv.imwrite('img_UD_flip.jpg', img_UD_flip)

img_LR_flip = cv.flip(img, 1)
cv.imwrite('img_LR_flip.jpg', img_LR_flip)

img_UDLR_flip = cv.flip(img, -1)
cv.imwrite('img_UDLR_flip.jpg', img_UDLR_flip)

# Scaling 
small_width = (int)(width / 3)
small_height = (int)(height / 3)
img_small = cv.resize(img, (small_width, small_height), fx = 0, fy = 0, interpolation = cv.INTER_LINEAR)
cv.imshow('smaller', img_small)
if(cv.waitKey(0) == ord('q')) : 
    cv.imwrite('img_small.jpg', img_small)

cv.imshow('normal', img)
if(cv.waitKey(0) == ord('q')) : 
    cv.imwrite('img_tmp.jpg', img)

large_width = (int)(width * 3)
large_height = (int)(height * 3)
img_large = cv.resize(img, (large_width, large_height), fx = 0, fy = 0, interpolation= cv.INTER_LINEAR)
cv.imshow('larger', img_large)
if(cv.waitKey(0) == ord('q')) : 
    cv.imwrite('img_large.jpg', img_large)

# Chopping 
img_chop1 = img[200:400, 150:300]
cv.imwrite('img_chop1.jpg', img_chop1)

img_chop2 = img[750:1000, 445:889]
cv.imwrite('img_chop2.jpg', img_chop2)
