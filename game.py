import pygame

from minefield import Minefield
from renderer import Renderer
from tile import Tile

GAME_SPEED = 10  # FPS
UPDATE_TIMER = pygame.USEREVENT + 1


class Game:
    def __init__(self, minefield: Minefield, renderer: Renderer) -> None:
        self.minefield = minefield
        self.renderer = renderer

        self.time = 0
        self.timer_running = False

        self.clock = pygame.time.Clock()
        self.clock.tick(GAME_SPEED)

        self.flag_count = minefield.number_of_mines

        self.running = True
        self.gameover = False

        self.renderer.create_field(
            self.minefield.proximity_matrix, self.flag_count, self.time
        )

    def reset(self, minefield: Minefield) -> None:
        self.minefield = minefield
        self.flag_count = self.minefield.number_of_mines

        self.time = 0
        self.stop_timer()
        self.renderer.create_field(
            self.minefield.proximity_matrix, self.flag_count, self.time
        )
        self.renderer.draw_tray(self.flag_count, self.time)

    def start_timer(self) -> None:
        if not self.timer_running:
            self.timer_running = True
            pygame.time.set_timer(UPDATE_TIMER, 1000)

    def stop_timer(self) -> None:
        self.timer_running = False
        pygame.time.set_timer(UPDATE_TIMER, 0)

    def tick_timer(self) -> None:
        self.time += 1
        self.renderer.draw_tray(self.flag_count, self.time)

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
                    self.click_tile(tile)
                    self.check_tile(tile)
                    self.start_timer()

    def check_tile(self, tile: Tile) -> None:
        if tile.proximity == 10:
            self.trigger_gameover()
        if tile.proximity == 0:
            need_to_click = self.minefield.check_for_cascade(
                tile.row, tile.column, set()
            )
            self.click_list(need_to_click)

    def click_tile(self, tile: Tile) -> None:
        tile.click()
        tile.update(self.renderer.screen)

    def click_list(self, click_list: set[tuple[int, int]]) -> None:
        for tile in self.renderer.tiles:
            if (tile.row, tile.column) in click_list:
                self.click_tile(tile)

    def toggle_flag(self, mouse_pos: tuple[float, float]) -> None:
        for tile in self.renderer.tiles:
            if tile.rect.collidepoint(mouse_pos):
                is_flagged = tile.toggle_flag()
                self.flag_count = (
                    self.flag_count - 1 if is_flagged else self.flag_count + 1
                )
                tile.update(self.renderer.screen)
                self.renderer.draw_tray(self.flag_count, self.time)

    def trigger_gameover(self):
        self.reveal_mines()
        pygame.display.flip()
        self.stop_timer()
        self.gameover = True

    def reveal_mines(self):
        for tile in self.renderer.tiles:
            if tile.proximity == 10:
                self.click_tile(tile)

    def group_click(self, mouse_pos: tuple[float, float]):
        for tile in self.renderer.tiles:
            if tile.rect.collidepoint(mouse_pos):
                pass
