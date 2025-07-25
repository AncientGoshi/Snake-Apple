import pygame
import rect_helpers

global snake_x, snake_y, apple_x, apple_y, score, current_direction, high_score, tail_coordinates

snake_speed = 20
snake_size = 20


def snake_init():
    global snake_x, snake_y, current_direction, tail_coordinates
    snake_x = snake_speed * 2
    snake_y = snake_speed
    tail_coordinates = []
    current_direction = "right"

def snake_set_direction(new_direction):
    global current_direction

    if new_direction != "":
        current_direction = new_direction

def snake_check_walls(the_walls):
    global snake_x, snake_y
    if snake_x < the_walls[0]:
        return True
    if snake_x > the_walls[1]:
        return True
    if snake_y < the_walls[2]:
        return True
    if snake_y > the_walls[3]:
        return True
    return False

def snake_move():
    global snake_x, snake_y

    tail_update()

    if current_direction == "left":
        snake_x -= snake_speed
    elif current_direction == "right":
        snake_x += snake_speed
    elif current_direction == "up":
        snake_y -= snake_speed
    elif current_direction == "down":
        snake_y += snake_speed

def tail_update():
    global snake_x, snake_y, tail_coordinates

    if tail_coordinates.__len__() > 0:
        del tail_coordinates[0]
        snake_tail_add()

def snake_tail_add():
    global snake_x, snake_y
    tail_coordinates.append((snake_x, snake_y))

def snake_draw_tail(screen, tail_x, tail_y):
    tail_rect = pygame.Rect(tail_x, tail_y, snake_size, snake_size)
    pygame.draw.rect(screen, pygame.Color("yellow"), tail_rect)

def snake_tail_draw(screen):
    for x, y in tail_coordinates:
        snake_draw_tail(screen, x, y)


def snake_get_rect():
    global snake_x, snake_y
    return pygame.Rect(snake_x, snake_y, snake_size, snake_size)


def snake_get_hit_tail():
    global snake_x, snake_y, tail_coordinates

    snake_rect = pygame.Rect(snake_x + 1, snake_y + 1, snake_size - 2, snake_size - 2)
    for (x, y) in tail_coordinates:
        tail_rect = pygame.Rect(x, y, snake_size, snake_size)
        tail_collision = rect_helpers.check_rects_collision(tail_rect, snake_rect)
        if tail_collision:
            return True
    return False

