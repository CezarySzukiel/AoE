from abc import ABC


class Surface(ABC):
    """
    Surface like ground, or water
    """

    def __init__(self, walkability: bool, swimability: bool, position_x: int | None = None, position_y: int | None = None):
        self.walkability = walkability
        self.swimability = swimability
        self.position_x = position_x
        self.position_y = position_y

    def describe(self):
        """
        Describe method
        """
        return f'I am a {self.__class__} !'


class Ground(Surface):
    """
    Ground
    """

    def __init__(self, walkability: bool = True, swimability: bool = False):
        super().__init__(walkability=walkability, swimability=swimability)


class Water(Surface):
    """
    Water
    """

    def __init__(self, walkability: bool = False, swimability: bool = True):
        super().__init__(walkability=walkability, swimability=swimability)


class ImpassableSurface(Surface):
    """
    Impassable surface
    """

    def __init__(self, walkability: bool = False, swimability: bool = False):
        super().__init__(walkability=walkability, swimability=swimability)


class Shoal(Surface):
    """
    Shoal
    """

    def __init__(self, walkability: bool = True, swimability: bool = True):
        super().__init__(walkability=walkability, swimability=swimability)


class Mud(Ground):
    """
    Mud
    """

    def __init__(self, movement_bonus=0.8):
        super().__init__()
        self.movement_bonus = movement_bonus


class Path(Ground):
    """
    Path
    """

    def __init__(self, movement_bonus):
        super().__init__()
        self.movement_bonus = movement_bonus
