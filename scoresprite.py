import pygame

class ScoreSprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(ScoreSprite.containers)  # 自動登録
        self.font = pygame.font.Font(None, 30)
        self.color = (255, 255, 255)
        self.score = 0
        self.start_time = pygame.time.get_ticks()
        self.bg_color = None

        self.image = self.font.render(str(self.score), True, self.color)
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, dt):
        # スコアが変化したときに描画を更新（ここでは毎回更新）
        self.image = self.render_text()
        self.rect = self.image.get_rect(topleft=self.rect.topleft)

    def draw(self, screen):
        self.image = self.font.render(str(self.score), True, self.color)
        self.rect = self.image.get_rect(topleft=self.rect.topleft) 
        
    def set_score(self, new_score):
        self.score = new_score

    def render_text(self):
        elapsed_sec = (pygame.time.get_ticks() - self.start_time) / 1000
        text = f"Score: {self.score}    Time: {elapsed_sec:.1f}s"
        surface = self.font.render(text, True, self.color, self.bg_color)
        return surface