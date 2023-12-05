class Unit:
    """
    Base class for all units including resources
    """
    def __init__(self, name, hp=0, attack=999, armor=0, speed=0, area=1, attack_range=1):
        self.name = name
        self.attack_range = attack_range
        self.hp = hp
        self.attack = attack
        self.armor = armor
        self.speed = speed
        self.area = area

    def describe(self):
        description = (
            f'name: {self.name}, '
            f'attack: {self.attack}, '
            f'attack range: {self.attack_range}, '
            f'hp: {self.hp}, armor: {self.armor}, '
            f'speed: {self.speed}, '
            f'area: {self.area}'
        )
        return description


class Wild(Unit):
    """
    Wild units
    """
    # todo zamieniłem kolejność argumentów (przeniosłem area wcześniej) sprawdź, czy to ma znaczenie
    def __init__(self, name, area, hp=0, attack=0, speed=0):
        super().__init__(name, hp=hp, attack=attack, speed=speed, area=area)

    def describe(self):
        description = super().describe()
        return f'{description}, I am wild'


class Civilized(Unit):
    """
    Human units
    """
    def describe(self):
        description = super().describe()
        return f'I am human unit! {description}'


class WildStationary(Wild):
    """
    Wild stationary units
    """

    def __init__(self, name, area):
        super().__init__(name, area=area)

    def describe(self):
        description = super().describe()
        return f'{description}, I am stationary'


# class Resource(Wild):
#     """
#     Resource units
#     """
#
#     def __init__(self, amount, name, hp, attack, armor, speed, area, attack_range):
#         super().__init__(name, hp, attack, armor, speed, area, attack_range)
#         self.amount = amount
#
#     def describe(self):
#         description = super().describe()
#         return f'{description}, amount: {self.amount}'


# class WildMobile(Wild):
#     """
#     Wild mobile units
#     """
#     def __init__(self, meat, name, hp, attack, armor, speed, area, attack_range):
#         super().describe()
#         self.meat = meat
#
#
# class Animal(WildMobile):
#     """
#     animal units
#     """
#     def __init__(self, run):
#         self.run = run
#     description = "I am an animal"
#
#
# class Predator(Animal):
#     def __init__(self, attack):
#         # super(self,)
#         description = "I am biting"
#         self.attack = attack
#
#
# class GameAnimal(Animal):
#     pass


# class Fossil(WildStationary):
    # def __init__(self, resource):
    #     self.resource = resource


# class Tree(Fossil):
#     pass


# rock = Fossil(600, '2x2')
# gold = Fossil(800)


example_unit = Unit(name='example unit', attack=1, attack_range=1, hp=100, armor=0, speed=20, area=2)

one_wild_unit = Wild(name='example Wild', attack=0, hp=100, speed=20, area=2)

print(example_unit.describe())
print(one_wild_unit.describe())

ex_wild_stationary = WildStationary('tree', 100)
print(ex_wild_stationary.describe())
# civilized = Civilized(name='civilized unit', attack=100, attack_range=10, hp=100, armor=10, speed=10, area=1)

# wild_stationary = WildStationary(name='cliff', area=10)
# print(example_unit.describe())

# example_resource = Resource(name='example resource', attack=0, attack_range=0, hp=0, armor=0, speed=0, area=2, amount=800)

# print(example_resource.describe())

# print(civilized.describe())