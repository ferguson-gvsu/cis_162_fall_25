import pygame
import random

def check_click(mouse_x, mouse_y, target_x, target_y, rad):
  '''Checks to see if the mouse is inside the target circle'''
  dist_squared = (target_x - mouse_x) ** 2 + (target_y - mouse_y) ** 2
  return dist_squared <= rad**2

def draw_text(surf : pygame.Surface, text : str, pos : tuple[int,int]):
  '''Draws the given string at the specified point of the pygame surface

  surf - Just pass screen
  text - The text you want to draw, as a string
  pos - an tuple of the form (x, y), where x and y are ints
  '''
  font = pygame.font.SysFont('', 24)
  font_surf = font.render(text, True, (255,255,255))
  surf.blit(font_surf, pos)


pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
fps_clock = pygame.time.Clock()

radius = 30
target_x = random.randint(radius, screen_width - radius)
target_y = random.randint(radius, screen_height - radius)

# LOAD HIGHSCORE HERE
highscore = 0

score = 0
timer_started = False
targets_hit = 0
targets_required = 5

is_running = True
while is_running:
  delta_time = fps_clock.tick(60) / 1000
  if timer_started:
    score += delta_time
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      is_running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
        is_running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
      if not timer_started: 
        timer_started = True
      mouse_x, mouse_y = pygame.mouse.get_pos()
      if check_click(mouse_x, mouse_y, target_x, target_y, radius):
        print('hit!')
        targets_hit += 1
        target_x = random.randint(radius, screen_width - radius)
        target_y = random.randint(radius, screen_height - radius)
        if targets_hit >= targets_required:
          is_running = False
     

  screen.fill((0,0,0))
  pygame.draw.circle(screen, (200, 0, 0), (target_x, target_y), radius)
  draw_text(screen, f"Current highscore: {highscore}", (0,0))
  draw_text(screen, f"Current time: {round(score, 2)}", (0,25))
  draw_text(screen, f"Targets remaining: {targets_required - targets_hit}", (0,50))
  pygame.display.flip()

score = round(score, 2)
print(f'You hit all the targets in {score} seconds!')

if score < highscore: 
  print('You beat the high score!')
  # WRITE NEW HIGHSCORE TO FILE HERE!
