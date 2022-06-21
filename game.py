
import pygame

from events import *
from minefield import Minefield
from renderer import Renderer

GAME_SPEED = 10 # FPS

class Game:
  def __init__(self, minefield:Minefield, renderer:Renderer) -> None:
    self.minefield = minefield
    self.renderer = renderer

    self.timer = 0
    self.timer_running = False

    self.clock = pygame.time.Clock()
    self.clock.tick(GAME_SPEED)

    self.renderer.create_field(self.minefield.minefield)

    self.running = True
    self.gameover = False
  def start_game(self) -> None:
    pass

  def start_timer(self) -> None:
    if not self.timer_running:
      self.timer_running = True
      pygame.time.set_timer(UPDATE_TIMER, 1000)

  def tick_timer(self) -> None:
    self.timer += 1
    self.renderer.update_timer(self.timer)

  def handle_mouse_move(self, mouse_pos: tuple[float, float]) -> None:
    for tile in self.renderer.tiles:
      if tile.rect.collidepoint(mouse_pos) and not tile.isClicked:
        self.renderer.highlight_tile(tile)
      else:
        self.renderer.no_highlight_tile(tile)

  def handle_mouse_down(self, mouse_pos: tuple[float, float]) -> None:
    for tile in self.renderer.tiles:
      if tile.rect.collidepoint(mouse_pos):
        if not tile.isClicked:
          tile.click()
          if tile.proximity == 10:
            self.trigger_gameover()
          if tile.proximity == 0:
            need_to_click = self.minefield.click_cascade(tile.row, tile.column, set())
            self.click_list(need_to_click)
          self.renderer.tiles.update(self.renderer.screen)
          self.start_timer()

  def handle_mouse_up(self) -> None:
    pygame.display.flip()

  def click_list(self, click_list: set[tuple[int, int]]) -> None:
    for tile in self.renderer.tiles:
      if (tile.row, tile.column) in click_list:
        tile.click()
    self.renderer.tiles.update(self.renderer.screen)

  def toggle_flag(self, mouse_pos: tuple[float, float]) -> None:
    for tile in self.renderer.tiles:
      if tile.rect.collidepoint(mouse_pos):
        tile.toggle_flag()
        self.renderer.update_texture(tile)

  def trigger_gameover(self):
    self.reveal_mines()
    pygame.display.flip()
    self.gameover = True

  def reveal_mines(self):
    for tile in self.renderer.tiles:
      if tile.proximity == 10:
        tile.click()
    self.renderer.tiles.update(self.renderer.screen)

