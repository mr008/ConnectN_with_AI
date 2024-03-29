import random
from typing import List
from .player import Player
from ConnectNGame.src.board import Board
from ConnectNGame.src import move

class RandomAI(Player):

    def __init__(self, name: str, piece: str) -> None:
        super().__init__(name, piece)

    def get_move(self, board: Board) -> "move.Move":
        possible_col=[]
        for col in range(board.num_cols):
            if board.is_column_full(col) == False:
                possible_col.append(col)
        choice=random.choice(possible_col)
        return move.Move(self, choice)

    @staticmethod
    def random(players: List["Player"], blank_char: str,num_player: int) -> "RandomAI":
        name = RandomAI.get_name(num_player)
        piece = RandomAI.get_valid_piece(players, blank_char)
        return RandomAI(name, piece)

    @staticmethod
    def get_name(num_player: int) -> str:
        name = "RandomAi " + str(num_player)
        return name

    @staticmethod
    def get_valid_piece(players: List["Player"], blank_char: str, case_matters: bool = False) -> str:
        VISIBLE_CHARACTERS = [chr(i) for i in range(ord('!'), ord('~') + 1)]
        while True:
            AI_piece = random.choice(VISIBLE_CHARACTERS)
            piece = AI_piece
            cmp_piece = piece if case_matters else piece.lower()
            player_pieces = {player.piece if case_matters else player.piece.lower(): player for player in players}

            if cmp_piece == blank_char.lower():
                continue
            elif cmp_piece in player_pieces:
                continue
            else:
                break
        return piece