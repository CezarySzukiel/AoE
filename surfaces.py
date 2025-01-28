from components import WalkableComponent, SwimableComponent


class Ground(WalkableComponent):
    """
    Ground
    """

    def __init__(self, ):
        super().__init__()


class Water(SwimableComponent):
    """
    Water
    """

    def __init__(self):
        super().__init__()


class Shoal(SwimableComponent, WalkableComponent):
    """
    Shoal
    """

    def __init__(self):
        super().__init__()


class Path(Ground):
    """
    Path
    """

    def __init__(self, movement_bonus):
        super().__init__()
        self.movement_bonus = movement_bonus
