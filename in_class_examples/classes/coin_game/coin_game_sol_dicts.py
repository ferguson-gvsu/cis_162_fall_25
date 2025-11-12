import pygame
import random



def get_clicked(m_x, m_y, center_x, center_y, radius):
    dist_squared = (m_x - center_x) ** 2 + (m_y - center_y) ** 2
    return dist_squared <= radius ** 2

# Pygame initialization
pygame.init()

# Define the main variables for our game
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])
clock = pygame.time.Clock()
is_game_running = True
num_coins = 100

# Add coins
coins = []
for i in range(num_coins):
    
    coin_radius = random.randint(5, 30)
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    vel_x = random.uniform(-300, 300)
    vel_y = random.uniform(-300, 300)
    r = random.randint(50, 255)
    g = random.randint(50, 255)
    b = random.randint(50, 255)
    coin_dict = {}
    coin_dict['position'] = [x, y]
    coin_dict['velocity'] = [vel_x, vel_y]
    coin_dict['radius'] = coin_radius
    coin_dict['color'] = [r, g, b]
    coins.append(coin_dict)


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
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            coins_to_remove = []
            for coin in coins:
                coin_pos = coin['position']
                if get_clicked(mouse_x, mouse_y, coin_pos[0], coin_pos[1], coin['radius']):
                    coins_to_remove.append(coin)
            for coin in coins_to_remove:
                coins.remove(coin)
    
    # Update!
    for coin_dict in coins:
        coin_pos = coin_dict['position']
        coin_vel = coin_dict['velocity']
        coin_radius = coin_dict['radius']
        coin_pos[0] += coin_vel[0] * delta_time
        coin_pos[1] += coin_vel[1] * delta_time
        # Check y bounds
        if coin_pos[1] + coin_radius >= screen_height:
            coin_vel[1] *= -1
            coin_pos[1] = screen_height - coin_radius
        elif coin_pos[1] <= coin_radius:
            coin_vel[1] *= -1
            coin_pos[1] = coin_radius
        # Check x bounds
        if coin_pos[0] + coin_radius >= screen_width:
            coin_vel[0] *= -1
            coin_pos[0] = screen_width - coin_radius
        elif coin_pos[0] <= coin_radius:
            coin_vel[0] *= -1
            coin_pos[0] = coin_radius

    # Draw!
    screen.fill((0,0,0))
    for coin_dict in coins:
        coin_pos = coin_dict['position']
        coin_radius = coin_dict['radius']
        coin_color = coin_dict['color']
        pygame.draw.circle(screen, coin_color, coin_pos, coin_radius)
    pygame.display.flip()
