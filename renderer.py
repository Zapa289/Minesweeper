
import pygame
from numpy import ndarray

from flag import FlagCounter
from textures import Textures
from tile import TILE_SIZE, Tile
from timer import Timer

DEFAULT_X = 400
DEFAULT_Y = 500

TRAY_GAP = 50

TL_MINE = (0, TRAY_GAP)

EDGE_GAP = 20

FLAG_POS_X = EDGE_GAP
FLAG_POS_Y = TRAY_GAP // 2

TIMER_POS_Y = TRAY_GAP // 2

class Renderer:
  def __init__(self) -> None:
    self.textures = Textures()

    self.tiles = pygame.sprite.Group()
    self.flag_counter = FlagCounter()
    self.timer = Timer()

    self.screen_size = (DEFAULT_X, DEFAULT_Y)
    self.screen = pygame.display.set_mode(self.screen_size)

    pygame.display.set_icon(self.textures.logo)
    pygame.display.set_caption("Minesweeper")

  def create_field(self, minefield:ndarray) -> None:
    tile_x_size , tile_y_size = TILE_SIZE
    x_pos, y_pos = TL_MINE

    for row_index, row in enumerate(minefield):
      x_pos = 0
      for col_index, proximity in enumerate(row):
        tile = Tile(
          mine_row=row_index,
          mine_column=col_index,
          location=(x_pos, y_pos),
          proximity=proximity,
          surface=pygame.transform.scale(self.textures.hidden,
          TILE_SIZE)
          )
        self.tiles.add(tile)
        x_pos += tile_x_size
      y_pos += tile_y_size

    self.screen_size = (x_pos, y_pos)
    self.screen = pygame.display.set_mode(self.screen_size)
    self.screen.fill((255,255,255))

    self.draw_tray(0, 0)

    for tile in self.tiles:
      self.screen.blit(tile.surf, tile.rect)

    pygame.display.flip()

  def draw_tray(self, flag_count: int, time: int) -> None:
    x_pos, _ = self.screen_size
    tray = self.textures.tray
    tray = pygame.transform.scale(tray, (x_pos, TRAY_GAP))
    self.screen.blit(tray, (0,0))

    self.update_flag_count(flag_count=flag_count)
    self.update_timer(time=time)

    pygame.display.flip()

  def redraw_field(self) -> None:
    self.tiles.update()
    for tile in self.tiles:
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
    screen_x, _ = self.screen_size

    timer_surface = self.timer.update(time)
    timer_rect = timer_surface.get_rect(right = screen_x - EDGE_GAP, centery = TIMER_POS_Y)

    self.screen.blit(timer_surface, timer_rect)

  def update_flag_count(self, flag_count: int) -> None:
    flag_counter_surface = self.flag_counter.update_flags(flag_count)
    flag_counter_rect = flag_counter_surface.get_rect(left = FLAG_POS_X, centery = FLAG_POS_Y)

    self.screen.blit(flag_counter_surface, flag_counter_rect)

