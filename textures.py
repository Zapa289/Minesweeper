from pathlib import Path

import pygame


class Textures:
  def __init__(self) -> None:
    self.proximity = {
      0 : pygame.image.load(Path("./art/MINESWEEPER_0.png")),
      1 : pygame.image.load(Path("./art/MINESWEEPER_1.png")),
      2 : pygame.image.load(Path("./art/MINESWEEPER_2.png")),
      3 : pygame.image.load(Path("./art/MINESWEEPER_3.png")),
      4 : pygame.image.load(Path("./art/MINESWEEPER_4.png")),
      5 : pygame.image.load(Path("./art/MINESWEEPER_5.png")),
      6 : pygame.image.load(Path("./art/MINESWEEPER_6.png")),
      7 : pygame.image.load(Path("./art/MINESWEEPER_7.png")),
      8 : pygame.image.load(Path("./art/MINESWEEPER_8.png")),
      10 : pygame.image.load(Path("./art/MINESWEEPER_M.png"))
    }
    self.hidden = pygame.image.load(Path("./art/MINESWEEPER_X.png"))
    self.flag =pygame.image.load(Path("./art/MINESWEEPER_F.png"))

    self.tray = pygame.image.load(Path("./art/MINESWEEPER_TRAY.png"))
    self.logo = pygame.image.load(Path("./art/logo.png"))
