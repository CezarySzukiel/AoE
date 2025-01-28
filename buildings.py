from components import LifeObjectComponent, CombatComponent


class Barracks(LifeObjectComponent):
    def __init__(self, max_health=500, health=500, player="player1"):
        super().__init__(max_health=max_health, health=health, player=player,)


class Tower(LifeObjectComponent, CombatComponent):
    def __init__(self, max_health=1000, health=1000, player="player1", damage=20, attack_range=10):
        super().__init__(max_health=max_health, health=health, player=player)
        combat = CombatComponent(damage=damage, attack_range=attack_range)
        self.attack = combat.attack
        self.damage = combat.damage
        self.attack_range = combat.attack_range


barracks = Barracks()
tower = Tower()
tower.attack(barracks)
print(barracks.health)
print(tower)


