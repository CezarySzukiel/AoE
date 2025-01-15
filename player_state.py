class Player:
    def __init__(self, name: str, player_id: int, color: str = "blue"):
        self._name: str = name
        self._id_: int = player_id
        self._color: str = color
        self._civilization: str | None = None
        self._age: int = 0
        self._units_number: int = 0
        self._wood: int = 0
        self._food: int = 0
        self._gold: int = 0
        self._stone: int = 0
        self._technology: set[str] = set()
        self._units_limit: int = 10
        self._technology_effect: dict = dict()

        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, value):
            self._name = value

        @property
        def color(self):
            return self._color

        @color.setter
        def color(self, value):
            """"""
            self._color = value

        @property
        def civilization(self):
            return self._civilization

        @civilization.setter
        def civilization(self, value):
            self._civilization = value

        @property
        def age(self):
            return self._age

        @age.setter
        def age(self, value):
            """age can be only increased"""
            self._age = value

        @property
        def units_number(self):
            return self._units_number

        @units_number.setter
        def units_number(self, value):
            """units cant units limit"""
            self._units_number = value

        @property
        def wood(self):
            return self._wood

        @wood.setter
        def wood(self, value):
            """wood count can't be negative"""
            self._wood = value

        @property
        def food(self):
            return self._food

        @food.setter
        def food(self, value):
            """food count can't be negative"""
            self._food = value

        @property
        def gold(self):
            return self._gold

        @gold.setter
        def gold(self, value):
            """gold count can't be negative"""
            self._gold = value

        @property
        def stone(self):
            return self._stone

        @stone.setter
        def stone(self, value):
            """stone count can't be negative"""
            self._stone = value

        @property
        def technology(self):
            return self._technology

        @technology.setter
        def technology(self, value: str):
            """technology can be only added"""
            self._technology.add(value)









# todo add validation for setters
# todo add Play class, when keep for example players, or global_units_limit
# todo add list of available colors of players