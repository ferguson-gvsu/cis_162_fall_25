import pygame
import random

# Initialize pygame and the screen
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Do the math for the grid
tile_size = 50
width_tiles = screen_width // tile_size
height_tiles = screen_height // tile_size


# State variables
player_pos = [0,0]
player_color = [100, 200, 50]
player_chunks = [player_pos.copy()]
apple_pos = [5, 5]
apple_color = [200, 50, 5]
direction = 'down'

# Use a pygame clock to lock our FPS to 10
clock = pygame.time.Clock()
fps_limit = 10

# Load our sound
pickup_sound = pygame.mixer.Sound('pickupCoin.wav')

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

  # Update!
  keys = pygame.key.get_pressed()
  if keys[pygame.K_w]:
    direction = 'up'
  elif keys[pygame.K_s]:
    direction = 'down'
  elif keys[pygame.K_a]:
    direction = 'left'
  elif keys[pygame.K_d]:
    direction = 'right'

  old_pos = player_pos.copy()
  
  if direction == 'up':
    player_pos[1] -= 1
  elif direction == 'down':
    player_pos[1] += 1
  elif direction == 'left':
    player_pos[0] -= 1
  elif direction == 'right':
    player_pos[0] += 1
 
  player_chunks.pop(-1)
  player_chunks.insert(0, player_pos.copy())

  if player_pos[0] == apple_pos[0] and player_pos[1] == apple_pos[1]:
    apple_pos[0] = random.randint(0, width_tiles-1)
    apple_pos[1] = random.randint(0, height_tiles-1)
    player_chunks.append(old_pos)
    pickup_sound.play()

  if player_pos[0] >= width_tiles or player_pos[0] < 0 or player_pos[1] < 0 or player_pos[1] >= height_tiles:
    is_running = False
    print('Ya ran off the edge!')
    print(f'Score: {len(player_chunks)}')

  if len(player_chunks) > 1:
    for chunk in player_chunks[1:]:
      if chunk[0] == player_pos[0] and chunk[1] == player_pos[1]:
        is_running = False
        print('Ya ate yourself!')
        print(f'Score: {len(player_chunks)}')
  
  # Draw!
  screen.fill((0,0,0))
  apple_x = apple_pos[0] * tile_size
  apple_y = apple_pos[1] * tile_size
  pygame.draw.rect(screen, apple_color, (apple_x, apple_y, tile_size, tile_size))
  player_x = player_pos[0] * tile_size
  player_y = player_pos[1] * tile_size
  pygame.draw.rect(screen, player_color, (player_x, player_y, tile_size, tile_size))
  for player_chunk in player_chunks:
    chunk_x = player_chunk[0] * tile_size
    chunk_y = player_chunk[1] * tile_size
    pygame.draw.rect(screen, player_color, (chunk_x, chunk_y, tile_size, tile_size))
  pygame.display.flip()
