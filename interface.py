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


class Object(Surface):
    """
    Base class for all objects
    """

    def __init__(self, area: tuple[int, int] = (1, 1), interaction: bool = True,
                 walkability: bool = False, swimability: bool = False):
        super().__init__(walkability, swimability)
        self.interaction = interaction
        self.area = area


class Resource(Object):
    """
    Resource units
    """

    def __init__(self, area: tuple[int, int] = (1, 1), interaction: bool = True, reserves: int = 0):
        super().__init__(area, interaction)
        self.reserves = reserves


class Unit(Object):
    """
    Base class for all moving units
    """

    def __init__(self, hp: int):
        super().__init__()
        self.hp = hp

    def run(self, x, y):
        """
        Run method
        """
        print("I am running")
        self.position_x += x
        self.position_y += y


class FoodResource(Resource):
    """
    Food resource
    """

    def __init__(self, reserves: int, area: tuple[int, int] = (1, 1), unit: Unit = None):
        super().__init__(reserves=reserves, area=area,)
        self.type_ = "food"
        self.unit = unit


gold = Resource(1000)
fish = FoodResource(reserves=1000, area=(2, 2))
deer = FoodResource(reserves=100, area=(1, 2), unit=Unit(hp=10))

print(vars(gold))
print(vars(fish))
print(vars(deer))

# grass = Ground()
# sand = Ground()
# water = Water()
# mud = Mud()
#
# cliff = Object()
# rock = Object()
#
#
# mud_path = Path(1.2)
# sand_path = Path(1.4)
# stone_path = Path(1.6)
#
# print(vars(mud_path))
#
# a = Mud()
# print(vars(a))
# print(dir(a))
# # todo zastosować gdzieś kompozycję
# todo czy klasy takie jak Object nie powinny być abstrakcyjne?

#
# print(dir())
