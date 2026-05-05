import cv2 as cv
import pygame
import filters 
import sys
import copy

stack = []

def transform(key):
    img = cv.imread('cur.jpg')
    
    if key != pygame.K_BACKSPACE:
        stack.append(copy.deepcopy(img))

    if key == pygame.K_RIGHT:
        img = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)

    elif key == pygame.K_LEFT:
        img = cv.rotate(img, cv.ROTATE_90_COUNTERCLOCKWISE)
   
    elif key == pygame.K_i:
        img = 255-img
    
    elif key == pygame.K_h:
        img = cv.flip(img, 0)
    
    elif key == pygame.K_v:
        img = cv.flip(img, 1)
    
    elif key == pygame.K_p:
        img = filters.SaltAndPepper(img)
    
    elif key == pygame.K_g:
        img = filters.GrayScale()
    
    elif key == pygame.K_b:
        img = filters.binary()
    
    elif key == pygame.K_f:
        num = input("Enter the number of the filter you want")
        img = filters.Filter(int(num))
    elif key == pygame.K_BACKSPACE:
        if len(stack) > 0:
            img = stack.pop()

    elif key == pygame.K_s:
        cv.imwrite('output.jpg', img)
        pygame.quit()
        sys.exit()
    cv.imwrite('cur.jpg', img)
