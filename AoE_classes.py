class Unit:
    """
    Base class for all units including resources
    """
    def __init__(self, hp, attack, armor, speed, area, attack_range):
        self.attack_range = attack_range
        self.hp = hp
        self.attack = attack
        self.armor = armor
        self.speed = speed
        self.area = area

    def describe(self):
        print(
            f'attack: {self.attack}, '
            f'attack range: {self.attack_range}, '
            f'hp: {self.hp}, armor: {self.armor}, '
            f'speed: {self.speed}, '
            f'area: {self.area}'
        )

class Wild(Unit):
    """
    Wild units
    """
    description = "I am wild"


class Civilized(Unit):
    """
    Human units
    """
    description = "I am civilized"


class Resource(Wild):
    """
    Resource units
    """
    def __init__(self, amount):
        self.amount = amount


class WildMobile(Wild):
    """
    Wild mobile units
    """
    def __init__(self, speed):
        description = "I am mobile"
        self.speed = speed


class WildStationary(Wild):
    """
    Wild stationary units
    """
    def __init__(self, area):
        self.area = area
        description = "I am stationary"


class Animal(WildMobile):
    """
    animal units
    """
    def __init__(self, run):
        self.run = run
    description = "I am an animal"


class Predator(Animal):
    def __init__(self, attack):
        # super(self,)
        description = "I am biting"
        self.attack = attack


class GameAnimal(Animal):
    pass


# class Fossil(WildStationary):
    # def __init__(self, resource):
    #     self.resource = resource


# class Tree(Fossil):
#     pass


# rock = Fossil(600, '2x2')
# gold = Fossil(800)


one_wild_unit=Wild(attack=1, attack_range=1, hp=100, armor=0, speed=20, area=2)
# one_wild_unit.describe
unit = Unit()