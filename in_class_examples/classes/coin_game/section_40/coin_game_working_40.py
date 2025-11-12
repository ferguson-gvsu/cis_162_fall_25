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
        self.velocity = [vel_x, vel_y]
        r = random.randint(50, 255)
        g = random.randint(50, 255)
        b = random.randint(50, 255)
        self.color = [r, g, b]

    def draw(self, surf):
        pygame.draw.circle(surf,self.color, self.position, self.radius)

    def update(self, screen_width, screen_height):
            self.position[0] += self.velocity[0]
            self.position[1] += self.velocity[1]
            if self.position[1] >= screen_height - self.radius:
                self.velocity[1] *= -1
            elif self.position[1] <= self.radius:
                self.velocity[1] *= -1
            if self.position[0] >= screen_width - self.radius:
                self.velocity[0] *= -1
            elif self.position[0] <= self.radius:
                self.velocity[0] *= -1

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
coins = []
for i in range(coin_num):
    coin = Coin(screen_width, screen_height)
    coins.append(coin)

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
    for coin in coins:
        coin.update(screen_width, screen_height)

    # Draw!
    screen.fill((0,0,0))
    for coin in coins:
        coin.draw(screen)
    pygame.display.flip()
