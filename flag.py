import pygame

from textures import Textures

textures = Textures()

COUNTER_X = 70
COUNTER_Y = 30
COUNTER_SIZE = (COUNTER_X, COUNTER_Y)

FLAG_X = COUNTER_Y
FLAG_Y = FLAG_X
FLAG_SIZE = (FLAG_X, FLAG_Y)

TEXT_X = COUNTER_X - FLAG_X
TEXT_Y = COUNTER_Y
TEXT_SIZE = (TEXT_X, TEXT_Y)

FONT = 'lucidasans'
FONT_SIZE = 20

COLOR_KEY = (255, 53, 184)

class FlagCounter:
  def __init__(self):
    self.font = pygame.font.SysFont(FONT, FONT_SIZE, bold=True)

    self.surf = pygame.surface.Surface(size=COUNTER_SIZE)
    self.surf.set_colorkey(COLOR_KEY)

    self.text_surf = pygame.surface.Surface(size=TEXT_SIZE)
    self.text_rect = self.text_surf.get_rect(right = COUNTER_X)

    self.flag_icon = pygame.transform.scale(textures.flag, FLAG_SIZE)

  def update_flags(self, flags: int) -> pygame.Surface:

    self.surf.blit(self.flag_icon, self.flag_icon.get_rect())

    font_surface = self.font.render(str(flags), False, (0, 0, 0), COLOR_KEY)
    font_rect = font_surface.get_rect(right = COUNTER_X - FLAG_X, centery = COUNTER_Y // 2)

    self.text_surf.fill(COLOR_KEY)
    self.text_surf.blit(font_surface, font_rect)

    self.surf.blit(self.text_surf, self.text_rect)

    return self.surf
