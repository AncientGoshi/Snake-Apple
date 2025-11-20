import sys
import random
import pygame.freetype
from pygame.locals import *

from json_helpers import *
from snake import *

global screen, clock, score_font, game_over_font, apple_x, apple_y, THE_WALLS, score, high_score, game_state, menu_selected_option
global snake_object

def setup():
    global screen, clock, score_font, game_over_font, apple_x, apple_y, THE_WALLS, score, high_score, game_state, menu_selected_option
    global snake_object

    pygame.init()
    screen = pygame.display.set_mode([640, 480])
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()
    
    score_font = pygame.freetype.Font("JetBrainsMono-Regular.ttf", 24)
    game_over_font = pygame.freetype.Font("JetBrainsMono-Regular.ttf", 55)

    apple_x = random.randint(0, 620)
    apple_y = random.randint(0, 460)

    THE_WALLS = 0, 620, 0, 460

    game_state = "MENU"
    menu_selected_option = 0

    snake_object = Snake()

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
    global game_state, score, high_score, snake_object, apple_x, apple_y

    # 1. Clear the screen
    screen.fill(pygame.Color("dark blue"))

    # 2. Display text
    game_over_rect = game_over_font.get_rect("Game Over")
    game_over_rect.center = (320, 180)
    game_over_font.render_to(screen, game_over_rect, "Game Over", pygame.Color("red"))

    score_text = f"Your Score: {score}"
    score_rect = score_font.get_rect(score_text)
    score_rect.center = (320, 250)
    score_font.render_to(screen, score_rect, score_text, pygame.Color("white"))

    high_score_text = f"High Score: {high_score}"
    high_score_rect = score_font.get_rect(high_score_text)
    high_score_rect.center = (320, 290)
    score_font.render_to(screen, high_score_rect, high_score_text, pygame.Color("white"))

    instructions_text = "Press C to Play Again or Q to Quit"
    instructions_rect = score_font.get_rect(instructions_text)
    instructions_rect.center = (320, 350)
    score_font.render_to(screen, instructions_rect, instructions_text, pygame.Color("yellow"))

    # 3. Handle specific input
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_q:
                pygame.quit()
                sys.exit()
            if event.key == K_c:
                game_state = "PLAYING"
                score = 0
                snake_object.init()
                apple_x = random.randint(0, 620)
                apple_y = random.randint(0, 460)

snake_steps = 0

def play_mode_update():
    global apple_x, apple_y, score, game_state, snake_steps

    new_direction = process_input()
    snake_object.set_direction(new_direction)

    if snake_steps >= 8:
        snake_object.move()
        snake_steps = 0
        if snake_object.check_walls(THE_WALLS) or snake_object.get_hit_tail():
            game_state = "GAME_OVER"
            return

    snake_steps += 1

    snake_rect = snake_object.get_rect()
    apple_rect = pygame.Rect(apple_x, apple_y, snake_size, snake_size)

    if snake_rect.colliderect(apple_rect):
        score += 1
        high_score_change()
        import_to_json(high_score)
        snake_object.tail_add()
        apple_x = random.randint(0, 620)
        apple_y = random.randint(0, 460)

    screen.fill(pygame.Color("dark blue"))
    pygame.draw.rect(screen, pygame.Color("red"), apple_rect)

    snake_object.draw(screen)

    score_font.render_to(screen, (260, 3), f"Score: {score}", pygame.Color("white"))
    score_font.render_to(screen, (260, 40), f"High Score: {high_score}", pygame.Color("white"))

def menu_update():
    global game_state, menu_selected_option, score, snake_object, apple_x, apple_y

    # --- Input Handling ---
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                menu_selected_option = (menu_selected_option - 1) % 2
            elif event.key == K_DOWN:
                menu_selected_option = (menu_selected_option + 1) % 2
            elif event.key == K_RETURN:
                if menu_selected_option == 0:  # Start Game
                    game_state = "PLAYING"
                    # Reset game state for a new game
                    score = 0
                    snake_object.init()
                    apple_x = random.randint(0, 620)
                    apple_y = random.randint(0, 460)
                elif menu_selected_option == 1:  # Quit
                    pygame.quit()
                    sys.exit()

    # --- Drawing ---
    screen.fill(pygame.Color("dark blue"))

    # Title
    title_rect = game_over_font.get_rect("SNAKE")
    title_rect.center = (320, 150)
    game_over_font.render_to(screen, title_rect, "SNAKE", pygame.Color("green"))

    # Menu Options
    start_color = pygame.Color("yellow") if menu_selected_option == 0 else pygame.Color("white")
    quit_color = pygame.Color("yellow") if menu_selected_option == 1 else pygame.Color("white")

    start_rect = score_font.get_rect("Start Game")
    start_rect.center = (320, 280)
    score_font.render_to(screen, start_rect, "Start Game", start_color)

    quit_rect = score_font.get_rect("Quit")
    quit_rect.center = (320, 330)
    score_font.render_to(screen, quit_rect, "Quit", quit_color)


def run_game():
    setup()

    while True:
        clock.tick(50)

        if game_state == "MENU":
            menu_update()
        elif game_state == "PLAYING":
            play_mode_update()
        elif game_state == "GAME_OVER":
            game_over_update()

        pygame.display.flip()

if __name__ == "__main__":
    run_game()
