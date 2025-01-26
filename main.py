                                         
import pygame
import math
import sys
from collections import defaultdict
import random

pygame.init()

width, height = 1100, 600
screen = pygame.display.set_mode((width,height))
objects = []


h = defaultdict(list)
for i in range(0,360,2):
    for r in range(0,600,3):
        radians = (math.pi/180) * i
        h[radians].append((int(math.sin(radians) * r), int(math.cos(radians) * r)))
 
for _ in range(10):
    color = (255, 255, 0) 
    position = (random.randint(0, width), random.randint(0, height))
    radius = 30
    circle_properties = {'color': color, 'position': position, 'radius': radius}
    objects.append(circle_properties)

try:
    while True:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
        pos = pygame.mouse.get_pos()
        

    

        for i in range(0,360,4):
            #circ1.centerx
            
            radians = (math.pi/180) * i
            
            x = pos[0]
            y = pos[1]
            r = 0
            nx = 0
            ny = 0
            collided = False
            while 0 <= nx <= width and 0 <= ny <= height and not collided:
                
                ny = int((math.sin(radians) * r) + y)
                nx = int((math.cos(radians) * r) + x)
                for obj in objects:
                    oX = obj['position'][0]
                    oY = obj['position'][1]
                    oR = obj['radius']/2

                    if math.sqrt((oX - nx) ** 2 + (oY - ny) ** 2) < oR:
                        collided = True
                screen.set_at((nx, ny), (255,255,255))
                r += 15

        for circle in objects:
            pygame.draw.circle(screen, circle['color'], circle['position'], circle['radius'])

        pygame.draw.circle(screen, (255,255,255), pygame.mouse.get_pos(), 50)
        pygame.display.flip()

except KeyboardInterrupt:
    pygame.quit()