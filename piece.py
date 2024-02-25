class Piece(object):
    """
    This class models one single chess piece.
    """

    """
    Class constants listing all possible chess piece types.

    Referring to e.g. the value KING from outside the class Piece
    looks like this:

      Piece.KING

    The letters corresponding to the pieces are :

    King     : K
    Queen    : D
    Rook     : T
    Bishop   : L
    Knight   : R
    Pawn     : (nothing)
    """

    KING = 0
    QUEEN = 1
    BISHOP = 2
    KNIGHT = 3
    ROOK = 4
    PAWN = 5


    def __init__(self, owner, type):
        """
        Initializes a new Piece with the given owner and the given type.

        @param owner: The player who owns this piece
        @param type: The type of this piece
        """
        self._owner = owner # player object who owns this piece
        self._set_type(type)   # type of this piece(KING,...)


    def get_player(self):
        """
        Returns the player who owns this piece.

        @return: the owner (player object) of this piece
        """
        return self._owner


    def get_type(self):
        """
        Returns the type of this piece.

        @return: the type of the piece (KING, QUEEN, BISHOP, KNIGHT, ROOK or PAWN)
        """
        return self._type


    def _set_type(self, type ):
        if type in [ Piece.KING, Piece.QUEEN, Piece.BISHOP, Piece.KNIGHT, Piece.ROOK, Piece.PAWN ]:
            self._type = type
        else:
            raise ValueError("Invalid piece type")


    owner = property( get_player )
    type = property( get_type )
