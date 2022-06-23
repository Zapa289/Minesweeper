import pygame

from textures import Textures

textures = Textures()

TILE_SIZE = (25, 25)


class Tile(pygame.sprite.Sprite):
    def __init__(
        self,
        mine_row: int,
        mine_column: int,
        location: tuple[int, int],
        proximity: int,
        surface: pygame.Surface,
    ):

        super(Tile, self).__init__()
        self.surf = surface
        self.rect = self.surf.get_rect(topleft=location)

        self.row = mine_row
        self.column = mine_column
        self.proximity = proximity
        self.is_flagged = False
        self.is_clicked = False

    def click(self) -> None:
        self.is_clicked = True

    def toggle_flag(self) -> None:
        self.is_flagged = not self.is_flagged
        return self.is_flagged

    def update(self, screen: pygame.Surface) -> None:
        if self.is_clicked:
            self.surf = pygame.transform.scale(
                textures.proximity[self.proximity], TILE_SIZE
            )
        else:
            if self.is_flagged:
                self.surf = pygame.transform.scale(textures.flag, TILE_SIZE)
            else:
                self.surf = pygame.transform.scale(textures.hidden, TILE_SIZE)

        pygame.draw.rect(screen, (255, 255, 255), self.rect)
        screen.blit(self.surf, self.rect)
