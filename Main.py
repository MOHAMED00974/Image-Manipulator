import cv2 as cv
import pygame
import sys
from trans import transform
from PIL import ImageFilter

pygame.init()

IMAGE_PATH = "img.jpg"

# Load image as a pygame surface
original = pygame.image.load(IMAGE_PATH)
img = cv.imread(IMAGE_PATH)

cv.imwrite('cur.jpg', img)

current = pygame.image.load('cur.jpg')


def set_screen(original, current):
    size = (current.get_size()[0]+original.get_size()[0], max(current.get_size()[1],original.get_size()[1]))
    return pygame.display.set_mode(size)
# Fit window to image size (or set a fixed size)

screen = set_screen(original, current)

pygame.display.set_caption("Image Editor")

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            key = event.key

            right_panel = pygame.Rect(original.get_width(), 0, current.get_width(), current.get_height())
            screen.fill((0,0,0), right_panel)  # fill with black, or use your bg color
            

            transform(key)
            current = pygame.image.load('cur.jpg')

            screen = set_screen(original, current)


    # Draw the current image onto the screen
    screen.blit(original, (0, 0))
    screen.blit(current, (original.get_size()[0], 0))

    pygame.display.flip()
    clock.tick(60)

