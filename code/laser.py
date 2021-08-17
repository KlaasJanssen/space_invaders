import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, speed, screen_height):
        super().__init__()
        self.image = pygame.Surface((4,20))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(center = pos)
        self.speed = speed
        self.height_y_constraint = screen_height

    def update(self):
        self.move_laser()
        self.destroy()

    def move_laser(self):
        self.rect.y += self.speed

    def destroy(self):
        if self.rect.y <= -50 or self.rect.y >= self.height_y_constraint:
            self.kill()
