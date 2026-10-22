import random

CLASSES = {
    "Warrior": {"hp": (110, 140), "attack": (10, 16)},
    "Mag": {"hp": (70, 90), "attack": (16, 24)},
}


def create_hero(name, hero_class):
    stats = CLASSES[hero_class]
    return {
        "name": name,
        "class": hero_class,
        "hp": random.randint(*stats["hp"]),
        "attack": random.randint(*stats["attack"]),
    }


def show_hero(hero):
    print(f"  {hero['name']} — {hero['class']}")
    print(f"  HP:     {hero['hp']}")
    print(f"  Attack:  {hero['attack']}")