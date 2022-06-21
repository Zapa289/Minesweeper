
import pygame

import testField
from events import *
from game import Game
from minefield import Minefield
from renderer import Renderer


def main() -> None:
  rows = 10
  columns = 10
  mines = testField.MINES

  renderer = Renderer()
  minefield = Minefield(rows=rows, columns=columns, number_of_mines=mines)

  game = Game(minefield, renderer)

  running = True

  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

      if event.type == pygame.MOUSEMOTION:
        game.handle_mouse_move(pygame.mouse.get_pos())

      if event.type == pygame.MOUSEBUTTONDOWN:
        game.handle_mouse_down(pygame.mouse.get_pos())

      if event.type == pygame.MOUSEBUTTONUP:
        game.handle_mouse_up()

      if event.type == UPDATE_TIMER:
        game.tick_timer()

if __name__ == "__main__":
  main()
