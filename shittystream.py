import requests
import pygame
import os
from PIL import Image
from time import sleep
ip = input("please enter your xbox one ip \n")
pygame.init()
(width, height) = (1920, 1080)
screen = pygame.display.set_mode((width, height))
while True:
    image = requests.get('https://'+ ip +':11443/ext/screenshot?download=true', verify=False)
    file= open("i.png",'wb')
    file.write(image.content)
    im = Image.open("i.png")
    rgb_im = im.convert('RGB')
    rgb_im.save('j.jpg')
    bg = pygame.image.load("j.jpg")
    screen.blit(bg,(0,0))
    pygame.display.update()
