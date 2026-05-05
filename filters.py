import cv2 as cv
import random 
from PIL import Image, ImageFilter

def SaltAndPepper(img):
    row, col = img.shape[:2]
    flag = 0

    pixels = random.randint(300, 10000)

    for _ in range(pixels):
        x = random.randint(0, row-1)
        y = random.randint(0, col-1)

        img[x][y] = (0,0,0) if flag else (255,255,255)
        flag ^= 1
    return img

def GrayScale():
    img = Image.open('cur.jpg').convert('L')
    img.save('cur.jpg')
    img = cv.imread('cur.jpg')
    return img

def binary():
    img = Image.open('cur.jpg').convert('1')
    img.save('cur.jpg')
    img = cv.imread('cur.jpg')
    return img

def Filter(num):
    img = Image.open('cur.jpg')
    if num == 0:
        img = img.filter(ImageFilter.BLUR)
    elif num == 1:
        img = img.filter(ImageFilter.BoxBlur(5))
    elif num == 2:
        img = img.filter(ImageFilter.CONTOUR)
    elif num == 3:
        img = img.filter(ImageFilter.EDGE_ENHANCE)
    elif num == 4:
        img = img.filter(ImageFilter.EMBOSS)
    elif num == 5:
        img = img.filter(ImageFilter.GaussianBlur(5))
    elif num == 6:
        img = img.filter(ImageFilter.SMOOTH)
    elif num == 7:
        img = img.filter(ImageFilter.ModeFilter)
    elif num == 8:
        img = img.filter(ImageFilter.SHARPEN)
    else:
        img = img.filter(ImageFilter.FIND_EDGES)



    img.save('cur.jpg')
    img = cv.imread('cur.jpg')
    return img