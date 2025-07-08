import sys
import random
import pygame.freetype
from pygame.locals import *

from json_helpers import *
from snake import *
from rect_helpers import *

global screen, clock, score_font, game_over_font, apple_x, apple_y, THE_WALLS, score, high_score, game_over

def setup():
    global screen, clock, score_font, game_over_font, apple_x, apple_y, THE_WALLS, score, high_score, game_over
    pygame.init()
    screen = pygame.display.set_mode([640, 480])
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()

    score_font = pygame.freetype.Font("JetBrainsMono-Regular.ttf", 24)
    game_over_font = pygame.freetype.Font("JetBrainsMono-Regular.ttf", 55)

    apple_x = random.randint(0, 620)
    apple_y = random.randint(0, 460)

    THE_WALLS = 0, 620, 0, 460

    game_over = False
    snake_init()
    score = 0
    high_score = 0

    high_score = json_read()

def process_input():
    for game_event in pygame.event.get():
        if game_event.type == QUIT:
            pygame.quit()
            sys.exit()

        if game_event.type == KEYDOWN:
            key = game_event.key

            if key == K_LEFT or key == K_a:
                return "left"
            elif key == K_RIGHT or key == K_d:
                return "right"
            elif key == K_UP or key == K_w:
                return "up"
            elif key == K_DOWN or key == K_s:
                return "down"
    return ""

def high_score_change():
    global high_score, score
    if high_score < score:
        high_score = score

def game_over_update():
    global game_over, score

    process_input()

    if any(pygame.key.get_pressed()):
        snake_init()
        game_over = False
        score = 0

    game_over_font.render_to(screen, (180, 180), "Game over", pygame.Color("red"))


snake_steps = 0

def play_mode_update():
    global apple_x, apple_y, score, game_over, snake_steps

    new_direction = process_input()
    snake_set_direction(new_direction)

    if snake_steps >= 8:
        snake_move()
        snake_steps = 0
    snake_steps += 1

    game_over = snake_check_walls(THE_WALLS)

    snake_rect = snake_get_rect()

    apple_rect = pygame.Rect(apple_x, apple_y, 20, 20)

    if check_rects_collision(snake_rect, apple_rect):
        score += 1
        high_score_change()
        import_to_json(high_score)
        snake_tail_draw(screen)
        apple_x = random.randint(0, 620)
        apple_y = random.randint(0, 460)

    screen.fill(pygame.Color("dark blue"))
    pygame.draw.rect(screen, pygame.Color("green"), snake_rect)
    pygame.draw.rect(screen, pygame.Color("red"), apple_rect)

    snake_tail_draw(screen)
    score_font.render_to(screen, (260, 3), f"Score: {score}", pygame.Color("white"))
    score_font.render_to(screen, (260, 40), f"High Score: {high_score}", pygame.Color("white"))

def run_game():
    setup()

    while True:
        clock.tick(50)

        if game_over:
            game_over_update()
        else:
            play_mode_update()

        pygame.display.flip()

if __name__ == "__main__":
    run_game()
