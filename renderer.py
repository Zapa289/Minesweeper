
import pygame
from numpy import ndarray

from textures import TILE_SIZE, Textures
from tile import Tile

DEFAULT_X = 400
DEFAULT_Y = 500

TRAY_GAP = 50

TL_MINE = (0, TRAY_GAP)

class Renderer:
  def __init__(self) -> None:
    pygame.init()

    self.tiles = pygame.sprite.Group()

    self.screen_size = (DEFAULT_X, DEFAULT_Y)
    self.screen = pygame.display.set_mode(self.screen_size)
    self.textures = Textures()

    pygame.display.set_icon(self.textures.logo)
    pygame.display.set_caption("Minesweeper")

  def create_field(self, minefield:ndarray) -> None:
    tile_x_size , tile_y_size = TILE_SIZE
    x_pos, y_pos = TL_MINE

    for row_index, row in enumerate(minefield):
      x_pos = 0
      for col_index, proximity in enumerate(row):
        tile = Tile(mine_row=row_index, mine_column=col_index, location=(x_pos, y_pos), proximity=proximity, surface=self.textures.hidden)
        self.tiles.add(tile)
        x_pos += tile_x_size
      y_pos += tile_y_size

    self.screen = pygame.display.set_mode((x_pos, y_pos))
    self.screen.fill((255,255,255))
    tray = self.textures.tray
    tray = pygame.transform.scale(tray, (x_pos, TRAY_GAP))
    self.screen.blit(tray, (0,0))

    for tile in self.tiles:
      self.screen.blit(tile.surf, tile.rect)

    pygame.display.flip()

  def redraw_field(self) -> None:
    for tile in self.tiles:
      self.update_texture(tile)
      self.screen.blit(tile.surf, tile.rect)
    pygame.display.flip()

  def highlight_tile(self, tile: Tile) -> None:
    if not tile.isClicked:
      tile.surf.set_alpha(150)
      pygame.draw.rect(self.screen, (255, 255, 255), tile.rect)
      self.screen.blit(tile.surf, tile.rect)
      pygame.display.flip()

  def no_highlight_tile(self, tile: Tile) -> None:
    tile.surf.set_alpha(255)
    pygame.draw.rect(self.screen, (255, 255, 255), tile.rect)
    self.screen.blit(tile.surf, tile.rect)
    pygame.display.flip()

  def update_timer(self, time: int) -> None:
    pass

  def update_flag_count(self, flag_count: int) -> None:
    pass

