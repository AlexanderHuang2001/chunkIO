class Player(object):
    """
    This class models a chess player.
    """

    # color of the player
    WHITE = 0
    BLACK = 1


    def __init__(self, name, color):
        """
        Initializes a new player with the given name and color.

        For example :

          player = Player("Matti", Player.BLACK)

        @param name: player's name as a string
        @param color: player's color as a class constant
        """
        ## Underscore means, that the variable should not be touched from outside this class
        self._name = name
        self._set_color( color )


    def get_name(self):
        """
        Returns the name of the player.

        @return: The name of this player.
        """
        return self._name


    def get_color(self):
        """
        Returns the color of this player.

        @return: the color of this player.
        """
        return self._color


    def _set_color(self, color):
        """
        Sets the player color if it is valid.

        Otherwise raises a ValueError.
        """
        if color in [ Player.WHITE , Player.BLACK]:
            self._color = color
        else:
            raise ValueError("Bad color given")


    ## allow accessing these variables directly, i.e. player.name
    name = property( get_name )
    color = property( get_color )
