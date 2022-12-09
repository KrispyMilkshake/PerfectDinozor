import random

import pygame
import os

pygame.init()
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = [pygame.image.load(os.path.join("pictures", "dinozor.png")),
           pygame.image.load(os.path.join("pictures", "dinozor2.png"))]
ducking = [pygame.image.load(os.path.join("pictures", "dinozor_duck.png")),
           pygame.image.load(os.path.join("pictures", "dinozor_duck2.png"))]
jumping = [pygame.image.load(os.path.join("pictures", "dinozor_jump.png"))]
cactus = [pygame.image.load(os.path.join("pictures", "cactus.png"))]
bird = [pygame.image.load(os.path.join("pictures", "bird.png"))]


class Dinozor:
    x_pos = 800
    y_pos = 500
    y_pos_duck = 550
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


class Obsticle:
    def __init__(self, img, x_pos, y_pos):
        self.img = img
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.obs_rect = self.img.get_rect()
        self.obs_rect.x = self.x_pos
        self.obs_rect.y = self.y_pos

    def update(self):
        global game_speed
        self.x_pos += game_speed
        self.obs_rect.x = self.x_pos

    def draw(self, screen):
        screen.blit(self.img, (self.obs_rect.x, self.obs_rect.y))


class Cactus(Obsticle):
    def __init__(self):

        super().__init__(pygame.transform.scale(cactus[0], (45, 45)), 0, 550)

class Bird(Obsticle):
    def __init__(self):

        super().__init__(pygame.transform.scale(bird[0], (45, 45)), 0, 490)


def game_loose_check(player, obsticles):
    for obs in obsticles:
        if player.dino_rect.colliderect(obs.obs_rect):
            return True
    return False


def main():
    global points, game_speed
    run = True
    clock = pygame.time.Clock()
    player = Dinozor()
    game_speed = 10
    points = 0
    font = pygame.font.Font("Mermaid Babies.ttf", 20)
    obsticles = []
    next_time_to_spoon_obsticale = 0

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1

        text = font.render("Points: " + str(points), True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 40)
        SCREEN.blit(text, text_rect)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if next_time_to_spoon_obsticale == 0:
            obsticles.append(random.choice([Cactus(), Bird()]))
            next_time_to_spoon_obsticale = random.randint(50, 110)
        else:
            next_time_to_spoon_obsticale -= 1

        SCREEN.fill((100, 24, 255))
        user_input = pygame.key.get_pressed()
        player.draw(SCREEN)
        player.update(user_input)
        for obs in obsticles:
            obs.update()
            obs.draw(SCREEN)
        if game_loose_check(player, obsticles):
            break
        score()

        clock.tick(30)
        pygame.display.update()


main()
