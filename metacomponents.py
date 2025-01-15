import inspect
from abc import ABCMeta, abstractmethod


class ObjectInterfaceMeta(ABCMeta):
    # @classmethod
    # def __prepare__(mcs, name, bases):
    #     print("TracingMeta.__prepare__")
    #     print(f"{mcs=}")
    #     print(f"{name=}")
    #     print(f"{bases=}")
    #     namespace = super().__prepare__(name, bases)
    #     print(f"{namespace=}")
    #     print()
    #     return namespace

    def __new__(mcs, name, bases, namespace):
        print("TracingMeta.__new__")
        print(f"{mcs=}")
        print(f"{name=}")
        print(f"{bases=}")
        print(f"{namespace=}")

        cls = super().__new__(mcs, name, bases, namespace)
        print(f"{cls=}")
        print()
        return cls

    def __init__(cls, name, bases, namespace):
        print("TracingMeta.__init__")
        if not inspect.isabstract(cls) and '__init__' not in namespace:
            raise AttributeError("No __init__ method")
        print("*-" * 50)
        print(f"{name=}")
        # print(dir(cls))
        print(cls.__dict__)
        # print(bases[0].__static_attributes__)
        # print(cls.__static_attributes__)
        # print(cls.__dict__)
        # print(type(cls.__abstractmethods__))
        print("*-" * 50)

        print(f"{cls=}")
        print(f"{bases=}")
        print(f"{namespace=}")
        super().__init__(name, bases, namespace)
        print()


