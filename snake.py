import pygame

snake_speed = 20
snake_size = 20

class Snake:
    x = 0
    y = 0
    current_direction = ""
    tail = []

    def __init__(self):
        self.init()

    def init(self):
        self.x = snake_speed * 2
        self.y = snake_speed
        self.tail = []
        self.current_direction = "right"

    def set_direction(self, new_direction):
        if new_direction != "":
            self.current_direction = new_direction

    def check_walls(self, the_walls):
        if self.x < the_walls[0]:
            return True
        if self.x > the_walls[1]:
            return True
        if self.y < the_walls[2]:
            return True
        if self.y > the_walls[3]:
            return True
        return False

    def move(self):
        self.tail_update()

        if self.current_direction == "left":
            self.x -= snake_speed
        elif self.current_direction == "right":
            self.x += snake_speed
        elif self.current_direction == "up":
            self.y -= snake_speed
        elif self.current_direction == "down":
            self.y += snake_speed

    def tail_update(self):
        if self.tail.__len__() > 0:
            del self.tail[0]
            self.tail_add()

    def tail_add(self):
        self.tail.append((self.x, self.y))

    def draw_tail(self, screen, tail_x, tail_y):
        tail_rect = pygame.Rect(tail_x, tail_y, snake_size, snake_size)
        pygame.draw.rect(screen, pygame.Color("yellow"), tail_rect)

    def tail_draw(self, screen):
        for x, y in self.tail:
            self.draw_tail(screen, x, y)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, snake_size, snake_size)

    def get_hit_tail(self):
        snake_rect = pygame.Rect(self.x + 1, self.y + 1, snake_size - 2, snake_size - 2)
        for (x, y) in self.tail:
            tail_rect = pygame.Rect(x, y, snake_size, snake_size)
            tail_collision = snake_rect.colliderect(tail_rect)
            if tail_collision:
                return True
        return False

    def draw(self, screen):
        pygame.draw.rect(screen, pygame.Color("green"), self.get_rect())
        self.tail_draw(screen)
