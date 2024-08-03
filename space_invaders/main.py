import random
import pygame
import math
from pygame import mixer

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Background img
background_img = pygame.image.load('img/galaxy.png')

# Title and icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('img/icon.png')
pygame.display.set_icon(icon)

# Music and Sound
mixer.music.load('sound/MusicaFondo.mp3')
mixer.music.set_volume(0.2)
mixer.music.play(-1)

# Player variables
player_img = pygame.image.load('img/player_spaceship.png')
player_x = 368
player_y = 520
player_change = 0
player_speed = 5

# Score
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text_x = 10
text_y = 10


def show_score(x, y):
    text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(text, (x, y))


# Game over text
font_game_over = pygame.font.Font('freesansbold.ttf', 50)
final_text_x = 250
final_text_y = 250
game_over = False


def show_game_over(x, y):
    text = font_game_over.render('GAME OVER', True, (255, 255, 255))
    screen.blit(text, (x, y))


# Enemy variables
enemy_img = pygame.image.load('img/alien.png')
enemy_x = []
enemy_y = []
enemy_speed = 2
enemy_x_change = []
enemy_y_change = []
enemy_numbers = 12

for enemy in range(0, enemy_numbers):
    enemy_x.append(random.randint(10, 728))
    enemy_y.append(random.randint(10, 200))
    enemy_x_change.append(enemy_speed)
    enemy_y_change.append(50)

# Bullet variables
bullet_img = pygame.image.load('img/bullet.png')
bullets = []
bullet_x = player_x
bullet_y = player_y - 20
bullet_y_change = -5
bullet_visible = False


# Detect impacts
def impact(x_1, y_1, x_2, y_2):
    distance = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_1 - y_2, 2))
    if distance < 30:
        return True
    else:
        return False


def player(x, y):
    # Player function
    screen.blit(player_img, (x, y))


def enemy(x, y):
    # Enemy function
    screen.blit(enemy_img, (x, y))


def bullet(x, y):
    # Bullet function
    screen.blit(bullet_img, (x + 20, y))


# Execute the game
running = True
while running:
    # Screen background-color in rgb format
    # screen.fill((232, 188, 67))

    screen.blit(background_img, (0, 0))

    for event in pygame.event.get():
        # Close the program if pressed the quit button
        if event.type == pygame.QUIT:
            running = False

    # Press a key
        if event.type == pygame.KEYDOWN:
            # Move left
            if event.key == pygame.K_LEFT:
                player_change = - player_speed
            # Move right
            if event.key == pygame.K_RIGHT:
                player_change = player_speed
            # Shoot a bullet
            if event.key == pygame.K_SPACE:
                new_bullet = {
                    'x': player_x,
                    'y': player_y - 20,
                    'bullet_visible': True
                }
                bullet_sound = mixer.Sound('sound/disparo.mp3')
                bullet_sound.play()
                bullets.append(new_bullet)
        # Release a key
        if event.type == pygame.KEYUP:
            # Stop moving if left or right key is released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_change = 0

    # Player movement
    player(player_x, player_y)
    player_x += player_change

    # Player limits
    if player_x < 0:
        player_change = 0
    if player_x > 736:
        player_change = 0

    # Bullet movement
    for b in bullets:
        if b['bullet_visible']:
            bullet(b['x'], b['y'])
            b['y'] += bullet_y_change
    # Remove bullets outside the screen
    bullets = [b for b in bullets if b['y'] >= -24]

    # Enemy movement
    for e in range(0, enemy_numbers):
        enemy(enemy_x[e], enemy_y[e])
        enemy_x[e] += enemy_x_change[e]

    # Enemy limits
    for e in range(0, enemy_numbers):
        if enemy_x[e] < 0:
            enemy_x_change[e] = enemy_speed
            enemy_y[e] += enemy_y_change[e]
        if enemy_x[e] > 736:
            enemy_x_change[e] = - enemy_speed
            enemy_y[e] += enemy_y_change[e]

    # Impacts
        for b in bullets:
            if b['bullet_visible']:
                collision_bullet = impact(b['x'], b['y'], enemy_x[e], enemy_y[e])
                if collision_bullet:
                    b['bullet_visible'] = False
                    b['y'] = -100
                    score += 5
                    enemy_x[e] = random.randint(10, 728)
                    enemy_y[e] = random.randint(10, 200)
                    impact_sound = mixer.Sound('sound/Golpe.mp3')
                    impact_sound.play()

    # GAME OVER
        if enemy_y[e] > 480:
            game_over = True
    if game_over:
        for ene in range(0, enemy_numbers):
            enemy_y[ene] = 1000
        show_game_over(final_text_x, final_text_y)

    # Score
    show_score(text_x, text_y)

    pygame.display.update()
