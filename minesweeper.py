import pygame

import testField
from game import UPDATE_TIMER, Game
from minefield import Minefield
from renderer import Renderer

MOUSE_LEFT = 1
MOUSE_MIDDLE = 2
MOUSE_RIGHT = 3


def main() -> None:
    rows = 10
    columns = 10
    mines = testField.MINES

    pygame.init()

    renderer = Renderer()
    minefield = Minefield(rows=rows, columns=columns, number_of_mines=mines)

    game = Game(minefield=minefield, renderer=renderer)
    run_game(game)


def reset(game: Game):
    minefield = Minefield(
        rows=game.minefield.rows,
        columns=game.minefield.columns,
        number_of_mines=game.minefield.number_of_mines,
    )

    game.reset(minefield)
    run_game(game)


def run_game(game: Game):
    while game.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False

            # If we are in gameover, skip all button processing except quit
            if game.gameover:
                continue

            if event.type == pygame.MOUSEMOTION:
                game.handle_mouse_move(pygame.mouse.get_pos())

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == MOUSE_LEFT:
                    game.handle_mouse_down(pygame.mouse.get_pos())

                if event.button == MOUSE_RIGHT:
                    game.toggle_flag(pygame.mouse.get_pos())

                if event.button == MOUSE_MIDDLE:
                    reset(game=game)
                    # game.group_click(pygame.mouse.get_pos())

            if event.type == pygame.MOUSEBUTTONUP:
                pygame.display.flip()

            if event.type == UPDATE_TIMER:
                game.tick_timer()


if __name__ == "__main__":
    main()
