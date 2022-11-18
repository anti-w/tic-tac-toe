import re

from tic_tac_toe.game.players import Player
from tic_tac_toe.logic.exceptions import InvalidMove
from tic_tac_toe.logic.models import GameState, Move


class ConsolePlayer(Player):
    def get_move(self, game_state: GameState) -> Move | None:
        while not game_state.game_over:
            try:
                index = grid_to_index(input(f"Vez do jogador {self.mark}: ").strip())
            except ValueError:
                print("Por favor envie apenas coordenadas no formato A1-a1 ou 1A- 1a")
            else:
                try:
                    return game_state.make_move_to(index)
                except InvalidMove:
                    print("Esse espaço já foi utilizado.")
        return None


def grid_to_index(grid: str) -> int:
    if re.match(r"[abcABC][123]", grid):
        col, row = grid
    elif re.match(r"[123][abcABC]", grid):
        row, col = grid
    else:
        raise ValueError("Coordenadas inválidas")
    return 3 * (int(row) - 1) + (ord(col.upper()) - ord("A"))
