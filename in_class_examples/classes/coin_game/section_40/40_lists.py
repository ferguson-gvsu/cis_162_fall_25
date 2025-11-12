import pygame
import random

# Pygame initialization
pygame.init()


# Define the main variables for our game
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])
clock = pygame.time.Clock()
is_game_running = True

direction = 1
coin_num = 100
coin_positions = []
coin_velocities = []
coin_radii = []
coin_colors = []

for i in range(coin_num):
    radius = random.randint(5, 50)
    x = random.randint(radius, screen_width - radius)
    y = random.randint(radius, screen_height - radius)
    coin_positions.append([x, y])
    vel_x = random.uniform(-5, 5)
    vel_y = random.uniform(-5, 5)
    coin_velocities.append([vel_x, vel_y])
    coin_radii.append(radius)
    r = random.randint(50, 255)
    g = random.randint(50, 255)
    b = random.randint(50, 255)
    coin_colors.append([r, g, b])

# Main game loop
while is_game_running:
    delta_time = clock.tick(60) / 1000
    # Handle input (mostly to allow us to quit!)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                is_game_running = False
    
    # Update!
    for coin_idx in range(len(coin_positions)):
        coin_pos = coin_positions[coin_idx]
        coin_vel = coin_velocities[coin_idx]
        radius = coin_radii[coin_idx]
        coin_pos[0] += coin_vel[0]
        coin_pos[1] += coin_vel[1]
        if coin_pos[1] >= screen_height - radius:
            coin_vel[1] *= -1
        elif coin_pos[1] <= radius:
            coin_vel[1] *= -1
        if coin_pos[0] >= screen_width - radius:
            coin_vel[0] *= -1
        elif coin_pos[0] <= radius:
            coin_vel[0] *= -1

    # Draw!
    screen.fill((0,0,0))
    for coin_idx in range(len(coin_positions)):
        coin_pos = coin_positions[coin_idx]
        radius = coin_radii[coin_idx]
        color = coin_colors[coin_idx]
        pygame.draw.circle(screen, color, coin_pos, radius)
    pygame.display.flip()
