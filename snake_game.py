import pygame
from pygame.locals import *
import time
import random

pygame.init()

# Colors
red = (255, 0, 0)
green = (51, 102, 0)
blue = (51, 153, 255)
grey = (192, 192, 192)
yellow = (0, 255, 255)

# Window
win_width = 600
win_height = 400
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Snake Game")
time.sleep(1)

# Snake settings
snake = 10
snake_speed = 15

clock = pygame.time.Clock()

# Fonts
font_style = pygame.font.SysFont("calibri", 26)
score_font = pygame.font.SysFont("stencil", 30)

def user_score(score):
    number = score_font.render("Score : " + str(score), True, red)
    rect = number.get_rect(center=(win_width // 2, 20))  # Top center
    window.blit(number, rect)

def game_snake(snake, snake_length_list):
    for x in snake_length_list:
        pygame.draw.rect(window, green, [x[0], x[1], snake, snake])

def message(mmsg):
    msg = font_style.render(mmsg, True, red)
    rect = msg.get_rect(center=(win_width // 2, win_height // 2))  # Centered
    window.blit(msg, rect)

def game_loop():
    gameOver = False
    gameClose = False

    x1 = win_width // 2
    y1 = win_height // 2

    x1_change = 0
    y1_change = 0

    snake_length_list = []
    snake_length = 1

    direction = ""  # Track direction

    foodx = round(random.randrange(0, win_width - snake) / 10.0) * 10.0
    foody = round(random.randrange(0, win_height - snake) / 10.0) * 10.0

    while not gameOver:
        while gameClose:
            window.fill(grey)
            message("You lost!! Press P to Play again or Q to Quit")
            user_score(snake_length - 1)  # Show final score
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameClose = False
                        gameOver = True
                    if event.key == pygame.K_p:
                        game_loop()
                        return

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != "RIGHT":
                    x1_change = -snake
                    y1_change = 0
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    x1_change = snake
                    y1_change = 0
                    direction = "RIGHT"
                elif event.key == pygame.K_UP and direction != "DOWN":
                    x1_change = 0
                    y1_change = -snake
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    x1_change = 0
                    y1_change = snake
                    direction = "DOWN"

        if x1 >= win_width or x1 < 0 or y1 >= win_height or y1 < 0:
            gameClose = True
        x1 += x1_change
        y1 += y1_change
        window.fill(grey)
        pygame.draw.rect(window, yellow, [foodx, foody, snake, snake])
        snake_size = [x1, y1]
        snake_length_list.append(snake_size)
        if len(snake_length_list) > snake_length:
            del snake_length_list[0]

        for block in snake_length_list[:-1]:
            if block == snake_size:
                gameClose = True

        game_snake(snake, snake_length_list)
        user_score(snake_length - 1)

        pygame.display.update()

        if round(x1) == foodx and round(y1) == foody:
            foodx = round(random.randrange(0, win_width - snake) / 10.0) * 10.0
            foody = round(random.randrange(0, win_height - snake) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

if __name__ == "__main__":
    game_loop()
