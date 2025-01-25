from surfaces import Surface


class ObjectInterface(Surface):
    """
    Base class for all objects
    """

    def __init__(self, area: tuple[int, int] = (1, 1), interaction: bool = True,
                 walkability: bool = False, swimability: bool = False):
        super().__init__(walkability, swimability)
        self.interaction = interaction
        self.area = area


o = ObjectInterface()
# print(vars(o))
# print(dir(o))


class ResourceInterface(ObjectInterface):
    """
    Resource units
    """

    def __init__(self, reserves: int = 0, type_: str | None = None):
        super().__init__()
        self.reserves = reserves
        self.type_ = type_


# r = ResourceInterface()
# print(vars(r))
# print(dir(r))


class UnitInterface(ObjectInterface):
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


class FoodResource(ResourceInterface):
    """
    Food resource
    """

    def __init__(self, reserves: int, area: tuple[int, int] = (1, 1), unit: UnitInterface = None):
        super().__init__()
        # self.type_ = "food"
        self.unit = unit


gold = ResourceInterface(1000)
fish = FoodResource(reserves=1000, area=(2, 2))
deer = FoodResource(reserves=100, area=(1, 2), unit=UnitInterface(hp=10))

# print(vars(gold))
# print(dir(gold))
print(vars(fish))
print(fish.reserves)
print(vars(deer))
print(deer.hp)

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
# todo klasy interface zrobić abstrakcyjne

#
# print(dir())
