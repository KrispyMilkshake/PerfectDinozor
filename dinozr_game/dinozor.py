import pygame

import dinozr_game.constants


class Dinozor:
    x_pos = 800
    y_pos = 500
    y_pos_duck = 550
    const_jump_vel = 8.5

    def __init__(self):
        self.run_img = dinozr_game.constants.RUNNING_IMGS
        self.duck_img = dinozr_game.constants.DUCKING_IMGS
        self.jump_img = dinozr_game.constants.RUNNING_IMGS

        self.is_duck = False
        self.is_running = True
        self.is_jumping = False

        self.step_index = 0
        self.jump_vel = self.const_jump_vel
        self.img = pygame.transform.scale(self.run_img[0], (100, 100))
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
        self.img = pygame.transform.scale(self.run_img[self.step_index // 5], (100, 100))
        self.dino_rect = self.img.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos
        self.step_index += 1

    def duck(self):
        self.img = pygame.transform.scale(self.duck_img[self.step_index // 5], (100, 50))
        self.dino_rect = self.img.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos_duck
        self.step_index += 1

    def jump(self):
        self.img = pygame.transform.scale(self.jump_img[0], (100, 100))
        if self.is_jumping:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -1 * self.const_jump_vel:
            self.is_jumping = False
            self.jump_vel = self.const_jump_vel

    def draw(self, screen):
        screen.blit(self.img, (self.dino_rect.x, self.dino_rect.y))
