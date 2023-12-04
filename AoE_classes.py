class Wild:
    """
    Wild units
    """
    description = "I am wild"


class Civilized:
    """
    Human units
    """
    description = "I am civilized"

class Resource:
    """
    Resource units
    """
    def __init__(self, amount):
        self.amount = amount



class Mobile:
    """
    Mobile units
    """
    def __init__(self, speed):
        description = "I am mobile"
        self.speed = speed


class Stationary:
    """
    Stationary units
    """
    def __init__(self, area):
        self.area = area
        description = "I am stationary"


class Animal(Wild, Mobile):
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



class Fossil(Wild, Stationary):
    def __init__(self, resource):
        self.resource = resource



class Tree(Fossil):
    pass


rock = Fossil(600, '2x2)
gold = Fossil(800)


