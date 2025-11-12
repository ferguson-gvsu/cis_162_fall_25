import pygame
import random


class Coin:
    def __init__(self, screen_width, screen_height):
        self.radius = random.randint(5, 50)
        x = random.randint(self.radius, screen_width - self.radius)
        y = random.randint(self.radius, screen_height - self.radius)
        self.position = [x, y]
        vel_x = random.uniform(-5, 5)
        vel_y = random.uniform(-5, 5)
        self.vel = [vel_x, vel_y]
        r = random.randint(50, 255)
        g = random.randint(50, 255)
        b = random.randint(50, 255)
        self.color = [r, g, b]

    def draw(self, surf):
        pygame.draw.circle(surf, self.color, self.position, self.radius)


# Pygame initialization
pygame.init()

# Define the main variables for our game
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])
clock = pygame.time.Clock()
is_game_running = True

num_coins = 100
coin_positions = []
coin_velocities = []
coin_radii = []
coin_colors = []
coins = []

for i in range(num_coins):
    coin = Coin(screen_width, screen_height)
    coins.append(coin)
    # radius = random.randint(5, 50)
    # x = random.randint(radius, screen_width - radius)
    # y = random.randint(radius, screen_height - radius)  
    # vel_x = random.uniform(-5, 5)
    # vel_y = random.uniform(-5, 5)
    # r = random.randint(50, 255)
    # g = random.randint(50, 255)
    # b = random.randint(50, 255)
    # coin_dict = {}
    # coin_dict['position'] = [x, y]
    # coin_dict['velocity'] = [vel_x, vel_y]
    # coin_dict['radius'] = radius
    # coin_dict['color'] = [r, g, b]
    # coins.append(coin_dict)


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
    # for coin in coins:
    #     coin_pos = coin['position']
    #     coin_vel = coin['velocity']
    #     coin_pos[0] += coin_vel[0]
    #     coin_pos[1] += coin_vel[1]
    #     if coin_pos[0] >= screen_width - coin['radius']:
    #         coin_vel[0] *= -1
    #     elif coin_pos[0] <= coin['radius']:
    #         coin_vel[0] *= -1
    #     if coin_pos[1] >= screen_height - coin['radius']:
    #         coin_vel[1] *= -1
    #     elif coin_pos[1] <= coin['radius']:
    #         coin_vel[1] *= -1

    # Draw!
    screen.fill((0,0,0))
    for coin in coins:
        #pygame.draw.circle(screen, coin['color'], coin['position'], coin['radius'])
        coin.draw(screen)
    pygame.display.flip()
