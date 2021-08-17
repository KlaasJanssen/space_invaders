import pygame

class Alien(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        file_path = '../graphics/' + color + '.png'
        self.image = pygame.image.load(file_path).convert_alpha()
        self.rect = self.image.get_rect(topleft = (x,y))

        if color == "red": self.value = 100
        if color == "green": self.value = 200
        if color == "yellow": self.value = 300

    def update(self, direction):
        self.rect.x += direction

class Extra(pygame.sprite.Sprite):
    def __init__(self, side, screen_width):
        super().__init__()
        self.image = pygame.image.load('../graphics/extra.png').convert_alpha()
        self.side = side
        self.x_constraint = screen_width
        if side == 'right':
            x = screen_width + 50
            self.speed = -3
        else:
            x = -50
            self.speed = 3
        self.rect = self.image.get_rect(topleft = (x,80))

    def update(self):
        self.rect.x += self.speed
        self.destroy()

    def destroy(self):
        if self.side == 'right' and self.rect.right <= 0:
            self.kill()
        elif self.side == 'left' and self.rect.left >= self.x_constraint:
            self.kill()
