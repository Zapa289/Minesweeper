from pathlib import Path

import pygame

TILE_SIZE = (25,25)

class Textures:
  def __init__(self) -> None:
    self.proximity = {
      0 : pygame.transform.scale(pygame.image.load(Path("./art/MINESWEEPER_0.png")).convert(), TILE_SIZE),
      1 : pygame.transform.scale(pygame.image.load(Path("./art/MINESWEEPER_1.png")).convert(), TILE_SIZE),
      2 : pygame.transform.scale(pygame.image.load(Path("./art/MINESWEEPER_2.png")).convert(), TILE_SIZE),
      3 : pygame.transform.scale(pygame.image.load(Path("./art/MINESWEEPER_3.png")).convert(), TILE_SIZE),
      4 : pygame.transform.scale(pygame.image.load(Path("./art/MINESWEEPER_4.png")).convert(), TILE_SIZE),
      5 : pygame.transform.scale(pygame.image.load(Path("./art/MINESWEEPER_5.png")).convert(), TILE_SIZE),
      6 : pygame.transform.scale(pygame.image.load(Path("./art/MINESWEEPER_6.png")).convert(), TILE_SIZE),
      7 : pygame.transform.scale(pygame.image.load(Path("./art/MINESWEEPER_7.png")).convert(), TILE_SIZE),
      8 : pygame.transform.scale(pygame.image.load(Path("./art/MINESWEEPER_8.png")).convert(), TILE_SIZE),
      10 : pygame.transform.scale(pygame.image.load(Path("./art/MINESWEEPER_M.png")).convert(), TILE_SIZE)
    }
    self.hidden = pygame.transform.scale(pygame.image.load(Path("./art/MINESWEEPER_X.png")).convert(), TILE_SIZE)
    self.flag = pygame.transform.scale(pygame.image.load(Path("./art/MINESWEEPER_F.png")).convert(), TILE_SIZE)

    self.tray = pygame.image.load(Path("./art/MINESWEEPER_TRAY.png")).convert()
    self.logo = pygame.image.load(Path("./art/logo.png")).convert()
