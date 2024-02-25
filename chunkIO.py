from game import Game
from corrupted_chess_file_error import *
from player import Player
from piece import Piece
from board import Board


class ChunkIO(object):

    def load_game(self, input):
        """
        @note:This is the game object this method will fill with data. The object
               is returned when the END chunk is reached.
        """
        self.game = Game()

        try:

            # Read the file header and the save date

            header = self.read_fully(8, input)
            date = self.read_fully(8, input)

            # Process the data we just read.
            # NOTE: To test the line below you must test the class once with a broken header

            header = ''.join(header)
            date = ''.join(date)
            print(date)
            if not str(header).startswith("SHAKKI"):
                raise CorruptedChessFileError("Unknown file type")

            # The version information and the date are not used in this
            # exercise

            # *************************************************************
            #
            # EXERCISE
            #
            # ADD CODE HERE FOR READING THE
            # DATA FOLLOWING THE MAIN HEADERS
            #
            #
            # *************************************************************

            while True:
                chunk_header = self.read_fully(5, input)
                chunk_type = self.extract_chunk_name(chunk_header)
                chunk_size = self.extract_chunk_size(chunk_header)

                if chunk_type == 'END':
                    break
                data = self.read_fully(chunk_size, input)
                data = ''.join(data)

                if chunk_type == 'CMT':
                    # Process comment if necessary
                    pass
                elif chunk_type == 'PLR':
                    self.process_player_chunk(data)
                else:
                    # Skip unknown or unhandled chunk types
                    continue
            # If we reach this point the Game-object should now have the proper players and
            # a fully set up chess board. Therefore we might as well return it.

            return self.game

        except OSError:
            # To test this part the stream would have to cause an
            # OSError. That's a bit complicated to test. Therefore we have
            # given you a "secret tool", class BrokenReader, which will throw
            # an OSError at a requested position in the stream.
            # Throw the exception inside any chunk, but not in the chunk header.
            raise CorruptedChessFileError("Reading the chess data failed 1.")




    # HELPER METHODS -------------------------------------------------------
    def map_piece_type_to_constant(self, piece_char):
        # Example mapping, adjust according to the Piece class constants
        piece_type_mapping = {
            'K': Piece.KING,  # Assuming Piece.KING is a constant in Piece class
            'Q': Piece.QUEEN,
            'B': Piece.BISHOP,
            'N': Piece.KNIGHT,
            'R': Piece.ROOK,
            'P': Piece.PAWN
        }
        return piece_type_mapping.get(piece_char, Piece.PAWN)  # Default to PAWN

    def process_player_chunk(self, data):
        color = data[0]
        if color == 'M':
            color = Player.BLACK
        elif color == 'V':
            color = Player.WHITE
        else:
            raise ValueError("Invalid player color in chunk data")

        name_length = int(data[1])
        name = data[2:2 + name_length]
        pieces_data = data[2 + name_length:]
        print(pieces_data)

        player = Player(name, color)
        self.game.add_player(player)
        self.add_pieces_to_board(pieces_data, player)

    def add_pieces_to_board(self, pieces_str, player):
        i = 0

        while i < len(pieces_str):
            if pieces_str[i] in 'KDTLR':
                print(pieces_str[i])
                piece_type = self.map_piece_type_to_constant(pieces_str[i])
                print(piece_type)
                column = pieces_str[i + 1]
                row = pieces_str[i + 2]
                print(column)
                print(row)
                i += 2
            else:
                piece_type = self.map_piece_type_to_constant(pieces_str[i])
                print(piece_type)
                column = pieces_str[i + 1]
                row = pieces_str[i + 2]
                print(column)
                print(row)
                i += 2
            column_index = Board.column_char_to_integer(column)
            row_index = Board.row_char_to_integer(row)
            piece = Piece(player, piece_type)
            print(piece)
            #self.game.set_board()

            self.game.board.set_piece(piece, column_index, row_index)

    def extract_chunk_size(self, chunk_header):
        """
        Given a chunk header (an array of 5 chars) will return the size of this
        chunks data.

        @param chunk_header:
                   a chunk header to process (str)
        @return: the size (int) of this chunks data
        """


        # subtracting the ascii value of the character 0 from
        # a character containing a number will return the
        # number itself

        return int( ''.join( chunk_header[3:5] ) )


    def extract_chunk_name(self, chunk_header):
        """
        Given a chunk header (an array of 5 chars) will return the name of this
        chunk as a 3-letter String.

        @param chunk_header:
                   a chunk header to process
        @return: the name of this chunk
        """
        return ''.join( chunk_header[0:3] )


    def read_fully(self, count, input):
        """
        The read-method of the Reader class will occasionally read only part of
        the characters that were requested. This method will repeatedly call read
        to completely fill the given buffer. The size of the buffer tells the
        algorithm how many bytes should be read.

        @param count:
                   How many characters are read
        @param input:
                   The character stream to read from
        @raises: OSError
        @raises: CorruptedChessFileError
        """
        read_chars = input.read( count )

        # If the file end is reached before the buffer is filled
        # an exception is thrown.
        if len(read_chars) != count:
                raise CorruptedChessFileError("Unexpected end of file.")

        return list(read_chars)
