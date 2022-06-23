import pygame

from textures import Textures

textures = Textures()

TIMER_SIZE = (60, 30)

FONT = 'franklingothicmedium'
FONT_SIZE = 25
FONT_COLOR = (255,0,0)
FONT_BG_COLOR = (0,0,0)

class Timer():
  def __init__(self):

    self.font = pygame.font.SysFont(FONT, FONT_SIZE)

    self.surf = pygame.surface.Surface(size=TIMER_SIZE)
    self.rect = self.surf.get_rect()

  def update(self, time: int) -> pygame.Surface:
    time_str = f"{time:03d}"

    font_surface = self.font.render(time_str, False, FONT_COLOR, FONT_BG_COLOR)
    timer_x, timer_y = TIMER_SIZE
    font_rect = font_surface.get_rect(center = (timer_x // 2, timer_y // 2))

    self.surf.fill((0,0,0))
    self.surf.blit(font_surface, font_rect)

    return self.surf
