
import pygame


class Tile(pygame.sprite.Sprite):
  def __init__(self, mine: tuple[int, int], location: tuple[int, int], proximity: int, surface: pygame.Surface):

    super(Tile, self).__init__()
    self.surf = surface
    self.rect = self.surf.get_rect(topleft = location)

    self.row, self.column = mine
    self.proximity = proximity
    self.isFlagged = False
    self.isClicked = False

  def click(self) -> None:
    self.isClicked = True

  def toggle_flag(self) -> None:
    self.isFlagged = not self.isFlagged
