import pygame

pygame.init()
image = pygame.image.load('maze.png')
tile_size = 10
s = ''
for y in range(image.get_height() // tile_size):
  for x in range(image.get_width() // tile_size):
    if image.get_at((x * tile_size, y * tile_size)) == (0,0,0):
      s += '#'
    else:
      s += '.'
  s += '\n'
print(s)
