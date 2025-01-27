from interface import *


class ObjectComponent(ObjectInterface):
    def __init__(self, position: list[int, int] = [0, 0], area: tuple[int, int] = (1, 1)):
        self._area = area
        self._position = position

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value


class WalkableComponent(ObjectComponent, WalkableInterface):
    def __init__(self):
        super().__init__()
        self._walkability = True

    @property
    def walkability(self):
        return self._walkability

    @walkability.setter
    def walkability(self, value):
        self._walkability = value


class SwimableComponent(ObjectComponent, SwimableInterface):
    def __init__(self):
        super().__init__()
        self._swimability = True

    @property
    def swimability(self):
        return self._swimability

    @swimability.setter
    def swimability(self, value):
        self._swimability = value


class InteractableObjectComponent(ObjectComponent, InteractableObjectInterface):
    def __init__(self, interaction: bool = True):
        super().__init__()
        self._interaction = interaction

    @property
    def interaction(self):
        return self._interaction

    @interaction.setter
    def interaction(self, value):
        self._interaction = value


class LifeObjectComponent(InteractableObjectComponent, LifeObjectInterface):
    def __init__(self, max_health: int = 50, health: float = 50, player: str = "Gaia"):
        super().__init__()
        self._max_health = max_health
        self._health = health
        self._player = player

    @property
    def max_health(self):
        return self._max_health

    @max_health.setter
    def max_health(self, value):
        self._max_health = value

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = value

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, value):
        self._player = value

    def take_damage(self, damage: int):
        self.health -= damage
        if self.health <= 0:
            print("Object destroyed!")
        return self.health


class MobileObjectComponent(LifeObjectComponent, MobileObjectInterface):
    def __init__(self, speed: int, direction: str = "N"):
        super().__init__()
        self._direction = direction
        self._speed = speed

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value

    def turn(self, value):
        self._direction = value
        print("Object turned")


class ResourceComponent(InteractableObjectComponent, ResourceInterface):
    def __init__(self, resource_type: str, amount: int):
        super().__init__()
        self._amount = amount
        self._resource_type = resource_type

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value: int):
        self._amount = value

    @property
    def resource_type(self):
        return self._resource_type

    @resource_type.setter
    def resource_type(self, value: str):
        self._resource_type = value

    def get_gathered(self, amount: int):
        gathered = min(amount, self.amount)
        self.amount -= gathered
        print(f"Gathered {gathered} {self.resource_type}")
        return gathered


class CombatComponent(CombatInterface):
    def __init__(self, damage: int, attack_range: int = 1):
        self._damage = damage
        self._range = attack_range

    @property
    def attack_range(self):
        return self._range

    @attack_range.setter
    def attack_range(self, value):
        self._range = value

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, value):
        self._damage = value

    def attack(self, target):
        print(f"Attacking {target}")
        target.take_damage(self.damage)
        return target


