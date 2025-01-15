from abc import abstractmethod, ABC

from metacomponents import ObjectInterfaceMeta


class ObjectInterface(ABC, metaclass=ObjectInterfaceMeta):
    """
    Base interface for all objects
    """
    # def __init__(self, position: tuple[int, int] = (0, 0), area: tuple[int, int] = (1, 1)):
    #     self._position = position
    #     self._area = area

    @abstractmethod
    def position(self) -> tuple[int, int]:
        pass

    @abstractmethod
    def area(self) -> tuple[int, int]:
        pass


class WalkableInterface(ObjectInterface):
    """
    Interface for all walkable objects.
    Use this to give units the ability to walk around this object.
    """
    # def __init__(self):
    #     super().__init__()
    #     self._walkability = True

    @property
    @abstractmethod
    def walkability(self) -> bool:
        """Walking units can walk over me"""
        pass


class SwimableInterface(ObjectInterface):
    """
    Interface for all swimable objects.
    Use this to give units the ability to swim around this object.
    """
    # def __init__(self):
    #     super().__init__()
    #     self._swimability = True

    @property
    @abstractmethod
    def swimability(self) -> bool:
        """Swimming units can swim over me"""
        pass


class InteractableObjectInterface(ObjectInterface):
    """
    Interface for all interactable objects
    """
    # def __init__(self):
    #     super().__init__()
    #     self._interactable = True

    @property
    @abstractmethod
    def interaction(self) -> bool:
        """interaction"""
        pass


class LifeObjectInterface(InteractableObjectInterface):
    """
    Base interface for all living objects
    """
    # def __init__(self, max_health: int, health: int, player: str):
    #     super().__init__()
    #     self._health = health
    #     self._max_health = max_health
    #     self._player = player

    @property
    @abstractmethod
    def max_health(self) -> int:
        """health points"""
        pass

    @property
    @abstractmethod
    def health(self) -> int:
        """health points"""
        pass

    @abstractmethod
    def take_damage(self, damage: int):
        """when object is attacked"""
        pass

    @property
    @abstractmethod
    def player(self):
        """Defines which player the object belongs to"""
        pass


class MobileObjectInterface(LifeObjectInterface):
    """
    Base interface for all mobile objects
    """
    # def __init__(self, speed: float, direction: str):
    #     super().__init__()
    #     self._speed = speed
    #     self._direction = direction

    @property
    @abstractmethod
    def speed(self) -> float:
        """speed of object"""
        pass

    @property
    @abstractmethod
    def direction(self) -> str:
        """direction of object"""
        pass

    @abstractmethod
    def turn(self, value: str) -> None:
        """Object can turn around"""
        pass


class WalkingObjectInterface(MobileObjectInterface):
    """
    Interface for all walking objects
    """

    @abstractmethod
    def walk(self):
        """Object walking"""
        pass


class SwimmingObjectInterface(MobileObjectInterface):
    """
    Interface for all swimming objects
    """

    @abstractmethod
    def swim(self):
        """Object swimming"""
        pass


class ResourceInterface(ObjectInterface):
    """
    interface for all resources
    """
    # def __init__(self, resource_amount: int, resource_type: str):
    #     super().__init__()
    #     self._resource_amount = resource_amount
    #     self._resource_type = resource_type

    @property
    @abstractmethod
    def resource_amount(self) -> int:
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


class CombatInterface(ABC):
    """
    Interface for all combat objects
    """

    @property
    @abstractmethod
    def damage(self) -> int:
        """damage dealt by object"""
        pass

    @property
    @abstractmethod
    def attack_range(self) -> int:
        """range of attack"""
        pass

    @abstractmethod
    def attack(self, target: LifeObjectInterface) -> None:
        """attacking"""
        pass
