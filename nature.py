from components import ResourceComponent, CombatComponent, SwimableComponent, WalkingObjectComponent


class Tree(ResourceComponent):
    """Tree is a resource of wood"""

    def __init__(self, position=(1, 1)):
        super().__init__("wood", 100)
        self.area = (1, 1)
        self.position = position


# palm = Tree()
# print(palm)
# palm.get_gathered(50)
# palm.position = (3, 3)
# print(palm)
# works fine


class Gold(ResourceComponent):
    """Gold is a resource of gold"""

    def __init__(self, amount=100):
        super().__init__("gold", amount)
        self.area = (2, 2)
        self.position = [3, 3]


class Stone(ResourceComponent):
    """Stone is a resource of stone"""

    def __init__(self, amount=100):
        super().__init__("stone", amount)
        self.area = (2, 2)
        self.position = [1, 1]


class Fish(ResourceComponent):
    """Fish is a resource of food and is stationary object"""

    def __init__(self, amount=100, area=(2, 2), position=(1, 1)):
        super().__init__("food", amount)
        self.area = area
        self.position = position
        self.swimability = SwimableComponent().swimability


class Deer(WalkingObjectComponent):
    """Deer can walk, and is food resource"""

    def __init__(self, position=(1, 1)):
        super().__init__(speed=5, direction="N")
        resource = ResourceComponent("food", 100)
        self.resource_type = resource.resource_type
        self.resource_amount = resource.resource_amount
        self.area = (1, 1)
        self.position = position
        self.health = 10


class Sheep(WalkingObjectComponent):
    """Sheep can walk, and is food resource"""

    def __init__(self, position=(1, 1)):
        super().__init__(speed=2, direction="N")
        resource = ResourceComponent("food", 100)
        self.resource_type = resource.resource_type
        self.resource_amount = resource.resource_amount
        self.area = (1, 1)
        self.position = position
        self.health = 2


class Boar(WalkingObjectComponent):
    """Boar can walk, attack, and is food resource"""

    def __init__(self, position=(1, 1)):
        super().__init__(speed=3, direction="N")
        resource = ResourceComponent("food", 100)
        self.resource_type = resource.resource_type
        self.resource_amount = resource.resource_amount
        self.area = (1, 1)
        self.position = position
        self.health = 30
        self.attack = CombatComponent(5).attack


class Wolf(WalkingObjectComponent):
    """Wolf can walk, attack, and is NOT food resource"""

    def __init__(self, position=(1, 1)):
        super().__init__(speed=4, direction="N")
        self.area = (1, 1)
        self.position = position
        self.health = 20
        self.attack = CombatComponent(10).attack
