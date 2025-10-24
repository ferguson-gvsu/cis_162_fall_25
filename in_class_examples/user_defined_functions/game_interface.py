import pygame
from func_example_40 import is_in_circle

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

circle_x = screen_width // 2
circle_y = screen_height // 2
circle_rad = 50

done = False
while not done:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            done = True
        elif evt.type == pygame.KEYDOWN:
            if evt.key == pygame.K_ESCAPE or evt.key == pygame.K_q:
                done = True
        if evt.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            mouse_x = mouse_pos[0]
            mouse_y = mouse_pos[1]
            if is_in_circle(circle_x, circle_y, mouse_x, mouse_y, circle_rad):
                print('Hit!')
            else: 
                print('Miss!')
    screen.fill((0,0,0))
    pygame.draw.circle(screen, (255,0,0), (circle_x, circle_y), circle_rad)
    pygame.display.flip()
pygame.quit()