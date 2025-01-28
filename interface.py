from abc import abstractmethod, ABC


class ObjectInterface(ABC):
    """
    Base interface for all objects
    """

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

    @property
    @abstractmethod
    def swimability(self) -> bool:
        """Swimming units can swim over me"""
        pass


class InteractableObjectInterface(ObjectInterface):
    """
    Interface for all interactable objects
    """

    @property
    @abstractmethod
    def interaction(self) -> bool:
        """interaction"""
        pass


class LifeObjectInterface(ObjectInterface):
    """
    Base interface for all living objects
    """

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
