class Obsticle:
    def __init__(self, img, x_pos, y_pos):
        self.img = img
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.obs_rect = self.img.get_rect()
        self.obs_rect.x = self.x_pos
        self.obs_rect.y = self.y_pos

    def update(self, game_speed):
        self.x_pos += game_speed
        self.obs_rect.x = self.x_pos

    def draw(self, screen):
        screen.blit(self.img, (self.obs_rect.x, self.obs_rect.y))
