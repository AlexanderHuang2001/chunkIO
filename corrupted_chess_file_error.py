class CorruptedChessFileError(Exception):

    def __init__(self, message):
        super(CorruptedChessFileError, self).__init__(message)
