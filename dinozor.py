import pygame
import os

pygame.init()
screen_height = 600
screen_weidth = 1100
screen = pygame.display.set_mode((screen_weidth, screen_height))

running = [pygame.image.load(os.path.join("pictures", "dinozor.png")),
           pygame.image.load(os.path.join("pictures", "dinozor2.png"))]
ducking = [pygame.image.load(os.path.join("pictures", "dinozor_duck.png")),
           pygame.image.load(os.path.join("pictures", "dinozor_duck2.png"))]
jumping = [pygame.image.load(os.path.join("pictures", "dinozor_jump.png"))]
cactus = [pygame.image.load(os.path.join("pictures", "cactus.png"))]
bird = [pygame.image.load(os.path.join("pictures", "bird.png"))]


class Dinozor:
    x_pos = 80
    y_pos = 310
    y_pos_duck = 340
    const_jump_vel = 8.5

    def __init__(self):
        self.run_img = running
        self.duck_img = ducking
        self.jump_img = running

        self.is_duck = False
        self.is_running = True
        self.is_jumping = False

        self.step_index = 0
        self.jump_vel = self.const_jump_vel
        self.img = self.run_img[0]
        self.dino_rect = self.img.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos

    def update(self, user_input):
        if self.is_duck:
            self.duck()
        if self.is_jumping:
            self.jump()
        if self.is_running:
            self.run()

        if self.step_index >= 10:
            self.step_index = 0

        if user_input[pygame.K_UP] and not self.is_jumping:
            self.is_duck = False
            self.is_running = False
            self.is_jumping = True
        elif user_input[pygame.K_DOWN] and not self.is_duck and not self.is_jumping:
            self.is_duck = True
            self.is_running = False
            self.is_jumping = False
        elif not (self.is_jumping or user_input[pygame.K_DOWN]):
            self.is_duck = False
            self.is_running = True
            self.is_jumping = False

    def run(self):
        self.img = self.run_img[self.step_index // 5]
        self.dino_rect = self.img.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos
        self.step_index += 1

    def duck(self):
        self.img = self.duck_img[self.step_index // 5]
        self.dino_rect = self.img.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos_duck
        self.step_index += 1

    def jump(self):
        self.img = self.jump_img[0]
        if self.is_jumping:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -1 * self.const_jump_vel:
            self.is_jumping = False
            self.jump_vel = self.const_jump_vel

    def draw(self, screen):
        screen.blit(self.img, (self.dino_rect.x, self.dino_rect.y))


def main():
    run = True
    clock = pygame.time.Clock()
    player = Dinozor()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill((255, 255, 255))
        user_input = pygame.key.get_pressed()
        player.draw(screen)
        player.update(user_input)

        clock.tick(30)
        pygame.display.update()


main()
