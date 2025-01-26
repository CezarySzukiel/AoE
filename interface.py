from abc import abstractmethod, ABC

from surfaces import Surface


class SurfaceInterface(ABC):
    """
    Interface for all surfaces
    """

    @property
    @abstractmethod
    def walkability(self) -> bool:
        """walkability"""
        pass

    @property
    @abstractmethod
    def swimability(self) -> bool:
        """swimability"""
        pass

    @abstractmethod
    def position(self) -> tuple[int, int]:
        """position"""
        pass


class ObjectInterface(SurfaceInterface):
    """
    Base interface for all objects
    """

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def interaction(self) -> bool:
        pass


class LifeObjectInterface(ObjectInterface):
    """
    Base interface for all living objects
    """

    @property
    @abstractmethod
    def hp(self) -> int:
        """health points"""
        pass

    @property
    @abstractmethod
    def speed(self) -> float:
        """speed of object"""
        pass

    @abstractmethod
    def take_damage(self, damage: int):
        """when object is attacked"""
        pass


class MobileObjectInterface(LifeObjectInterface):
    """
    Base interface for all mobile objects
    """

    @abstractmethod
    def move(self):
        pass


class ResourceInterface(ObjectInterface):
    """
    interface for all resources
    """

    @property
    @abstractmethod
    def amount(self) -> int:
        """amount of resource"""
        pass

    @property
    @abstractmethod
    def resource_type(self) -> str:
        """type of resource"""
        pass

    @abstractmethod
    def get_gathered(self, quantity: int) -> None:
        """when resource is gathered"""
        pass


class Resource(ResourceInterface):
    """
    Resource
    """

    def __init__(self, position, walkability, swimability, interaction, area, amount, resource_type):
        super().__init__()
        self._position = (0, 0)
        self._walkability = False
        self._swimability = False
        self._interaction = True
        self._area = area
        self._amount = amount
        self._resource_type = "gold"

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value: tuple[int, int]):
        self._position = value

    @property
    def walkability(self):
        return self._walkability

    @walkability.setter
    def walkability(self, value: bool):
        self._walkability = value

    @property
    def swimability(self):
        return self._swimability

    @swimability.setter
    def swimability(self, value):
        self._swimability = value

    @property
    def interaction(self):
        return self._interaction

    @interaction.setter
    def interaction(self, value: bool):
        self._interaction = value

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value: tuple[int, int]):
        self._area = value

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

    def get_gathered(self, quantity: int) -> None:
        gathered = min(quantity, self.amount)
        self.amount -= gathered
        print(f"Gathered {gathered} {self.resource_type}")


class LifeObject(LifeObjectInterface):
    """
    Base class for all living objects
    """

    # todo trzeba by implementować ponownie metody które ma już klasa Resource, takie jak position, walkability, swimability, interaction, area. jak to zrobić poprawnie by nie łamać DRY?
    # todo czy da się w tym celu użyć kompozycji?
    def __init__(self, hp, speed):
        self._hp = hp
        self._speed = speed

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value: int):
        self._hp = value

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value: float):
        self._speed = value

    def take_damage(self, damage: int):
        self.hp -= damage
        if self.hp <= 0:
            print("Object destroyed!")
        return self.hp


class Animal(Resource):
    """
    All animals who can not fight.
    (deer, sheep)
    """

    def __init__(self):
        super().__init__()

    # todo dziedziczenie plus kompozycja? resource + lifeObject + mobileObject
    # czy nie powinienem najpierw zrobić AnimalInterface


gold = Resource(position=(0, 0), walkability=False, swimability=False, interaction=True, area=(2, 2), amount=800,
                resource_type="gold")

print(vars(gold))
# # todo zastosować gdzieś kompozycję
# todo klasy interface zrobić abstrakcyjne
# todo wilk będzie żołnierzem gracza przyroda, bo nie dało się z niego pozyskiwać jedzenia
# todo klasa AnimalFighter, bo dzik atakował, poza tym niektóre budynki też atakowały, więc nie fighter osobno

#
# print(dir())
