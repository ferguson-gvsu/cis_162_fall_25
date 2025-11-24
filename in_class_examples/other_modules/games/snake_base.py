import pygame

# Initialize pygame and the screen
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Do the math for the grid
tile_size = 20
width_tiles = screen_width // tile_size
height_tiles = screen_height // tile_size


# State variables
player_pos = [0,0]
player_color = [100, 200, 50]
apple_pos = [5, 5]
apple_color = [200, 50, 5]

# Use a pygame clock to lock our FPS to 10
clock = pygame.time.Clock()
fps_limit = 10

# Main loop
is_running = True
while is_running:
  clock.tick(fps_limit)

  # Handle events so we don't freeze!
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      is_running = False
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
      is_running = False
  
  # Draw!
  screen.fill((0,0,0))
  apple_x = apple_pos[0] * tile_size
  apple_y = apple_pos[0] * tile_size
  pygame.draw.rect(screen, apple_color, (apple_x, apple_y, tile_size, tile_size))
  pygame.display.flip()
