
import pygame

from textures import Textures

textures = Textures()

class Tile(pygame.sprite.Sprite):
  def __init__(self, mine_row: int, mine_column: int, location: tuple[int, int], proximity: int, surface: pygame.Surface):

    super(Tile, self).__init__()
    self.surf = surface
    self.rect = self.surf.get_rect(topleft = location)

    self.row = mine_row
    self.column = mine_column
    self.proximity = proximity
    self.isFlagged = False
    self.isClicked = False

  def click(self) -> None:
    self.isClicked = True

  def toggle_flag(self) -> None:
    self.isFlagged = not self.isFlagged
    return self.isFlagged

  def update(self, screen: pygame.Surface) -> None:
    if self.isClicked:
      self.surf = textures.proximity[self.proximity]
    else:
      if self.isFlagged:
        self.surf = textures.flag
      else:
        self.surf = textures.hidden

    pygame.draw.rect(screen, (255, 255, 255), self.rect)
    screen.blit(self.surf, self.rect)
