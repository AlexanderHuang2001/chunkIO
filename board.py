class Board(object):
    """
    This class models a chess board.
    """

    def __init__(self):
        """
        Initiates a new empty board. C{board} is an internal array for holding the chess pieces.
        """
        self._board = [None] * 8
        for i in range(8):
            self._board[i] = [None] * 8


    def set_piece(self, piece, column, row):
        """
        Places a new piece in the given location.

        @param piece: the piece object being placed.
        @param column: the column in which to place the piece
        @param row: the row in which to place the piece
        @raises: ValueError
        """
        if self.is_free(column, row):
            self._board[column][row] = piece
        else:
            # This is an unchecked exception. Therefore it is not marked in the
            # method signature.

            raise ValueError("Tried to place a piece in an occupied square.")


    def get_piece(self, column, row):
        """
        Returns the piece object located in the given coordinates.

        @param column: the column of interest
        @param row: the row of interest
        @return: the piece object located in the coordinates or None if the location was empty
        """
        return self._board[column][row]


    def is_free(self, column, row):
        """
        Tests if the given location was free.

        @param column: the column of interest
        @param row: the row of interest
        @return: true if and only if the location was empty
        """
        return self._board[column][row] == None


    @staticmethod ## we can now call this method without an instance
    def column_char_to_integer(column):
        """
        Converts the letters a,b,c,d,e,f,g,h to positions 0-7.
        @param row the character representation of a column.
        @return the integer representation.
        """
        return ord(column) - ord('a')


    @staticmethod ## we now can call this method even without an instance!
    def row_char_to_integer(row):
        """
        Converts the characters '1','2','3'..... to positions 0-7.
        @param row: the character representation of a row.
        @return: the integer representation.
        """
        return ord(row) - ord('1')


    def __getitem__(self, key):
        """ This method allows board to be used like a dictonary.
        E.g. print board['a', '1']

        Note: key should be in column, row -format.
        """
        ## assuming key to be a double (column, row)
        row = self.row_char_to_integer( key[1] )
        column = self.column_char_to_integer( key[0] )
        if 0 <= column < len( self._board ) and 0 <= row < len( self._board[0] ):
            return self.get_piece( column , row )
        else:
            raise KeyError("Invalid key!")


    def __setitem__( self, key, item):
        """ This method allows board to be used like a dictonary.
        E.g. board['a', '1'] = 0.

        Note: key should be in column, row -format.
        """
        ## assuming key to be a double (column, row)
        row = self.row_char_to_integer( key[1] )
        column = self.column_char_to_integer( key[0] )
        if 0 <= column < len( self._board ) and 0 <= row < len( self._board[0] ):
            self.set_piece( item , column , row )
        else:
            raise KeyError("Invalid key!")
