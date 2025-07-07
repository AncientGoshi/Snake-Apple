import pygame

global snake_x, snake_y, apple_x, apple_y, score, current_direction, high_score, tail_x, tail_y

snake_speed = 20
snake_size = 20

def snake_init():
    global snake_x, snake_y, current_direction, tail_x, tail_y
    snake_x = 20
    snake_y = 20
    tail_x = 0
    tail_y = 20
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
    global snake_x, snake_y, tail_x, tail_y

    if current_direction == "left":
        snake_x -= snake_speed
    elif current_direction == "right":
        snake_x += snake_speed
    elif current_direction == "up":
        snake_y -= snake_speed
    elif current_direction == "down":
        snake_y += snake_speed

    tail_x = tail_update()[0]
    tail_y = tail_update()[1]

def tail_update():
    global snake_x, snake_y, current_direction, tail_x, tail_y
    tail_x = snake_x
    tail_y = snake_y

    if current_direction == "left": tail_x = snake_x + snake_size
    elif current_direction == "right": tail_x = snake_x - snake_size
    elif current_direction == "up": tail_y = snake_y + snake_size
    elif current_direction == "down": tail_y = snake_y - snake_size
    return tail_x, tail_y

def snake_get_rect():
    global snake_x, snake_y
    return pygame.Rect(snake_x, snake_y, snake_size, snake_size)

def snake_tail_get_rect():
    global tail_x, tail_y
    return pygame.Rect(tail_x, tail_y, snake_size, snake_size)
