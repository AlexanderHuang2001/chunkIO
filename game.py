from player import Player
from board import Board


class Game(object):
    """
    This class serves as a facade for the chess game.
    """

    def __init__(self):
        ## initialize values
        self._black = None
        self._white = None
        self._board = None


    def get_black(self):
        """
        Returns the black player for this game.
        @return: the black player.
        """
        if self._black:
            return self._black
        raise ValueError("Black player has not been added!")


    def get_white(self):
        """
        Returns the white player for this game.
        @return: the white player.
        """
        if self._white:
            return self._white
        raise ValueError("White player has not been added!");


    def get_board(self):
        """
        Returns the chess board of this game.
        @return: the chess board.
        """
        return self._board


    def add_player(self, player):
        """
        Adds a player to a game.
        @param player: the player object to be added
        """
        ## note, here instead of calling the method get_color(), a getter
        ## we use the variable directly: player.color calls, due to
        ## color = property( get_color ), method get_color
        if player.color == Player.BLACK:
            self._black = player
        else:
            self._white = player


    def set_board(self, board):
        """
        Sets the game board for this game.
        @param board: the new board object for this game
        """
        self._board = board


    white = property( get_white )
    black = property( get_black )
    board = property( get_board, set_board )
