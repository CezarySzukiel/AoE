class HealthComponent:
    def __init__(self, health: int):
        self.health = health

    def take_damage(self, damage: int):
        self.health -= damage
        if self.health <= 0:
            print("Object destroyed!")
        return self.health


class MovementComponent:
    def __init__(self, speed: int):
        self.speed = speed

    def move(self, dx: int, dy: int):
        print(f"Moving by ({dx}, {dy}) with speed {self.speed}")


class CombatComponent:
    def __init__(self, attack_damage: int):
        self.attack_damage = attack_damage

    def attack(self, target: HealthComponent):
        print(f"Attacking target with {self.attack_damage} damage")
        target.take_damage(self.attack_damage)


class ResourceComponent:
    def __init__(self, resource_type: str, reserves: int):
        self.resource_type = resource_type
        self.reserves = reserves

    def gather(self, amount: int):
        gathered = min(amount, self.reserves)
        self.reserves -= gathered
        print(f"Gathered {gathered} {self.resource_type}")
        return gathered