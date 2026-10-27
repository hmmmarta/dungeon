import random

ENEMY_DATA = [
    {"name": "Goblin", "hp": 60, "attack": 9 },
    {"name": "Skeleton", "hp": 50, "attack": 12 },
    {"name": "Golem", "hp": 110, "attack": 7 },
]

class Enemy:
    def __init__(self, name, hp, attack):
        self.name = name
        self.max_hp = hp
        self._hp = hp
        self.attack = attack
    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = max(0, min(value, self.max_hp))

    def is_alive(self):
        return self._hp > 0

    def take_damage(self, amount):
        self.hp -= amount

    def hit(self, target):
        target.take_damage(self.attack)
        return self.attack

    def __str__(self):
        return f"{self.name} HP {self.hp} / {self.max_hp} ATK {self.attack}"

    def __repr__(self):
        return f"Hero ({self.name!r})"

enemy = Enemy(**random.choice(ENEMY_DATA))

print(enemy)