import random
# hero = {
#     "name": "John",
#     "class": "Warrior",
#     "hp": 80,
#     "attack": 14,
# }
#
# print("Name: ", hero["name"])
# print("Class: ", hero["class"])
# print("HP: ", hero["hp"])
# print("Attack: ", hero["attack"])

CLASSES = {
    "Warrior": {"hp": (100, 140), "attack": (10, 16)},
    "Mag": {"hp": (70, 90), "attack": (16, 20)}
}

def create_hero(name, hero_class):
    stats = CLASSES[hero_class]
    return {
        "name": name,
        "class": hero_class,
        "hp": random.randint(*stats["hp"]),
        "attack": random.randint(*stats["attack"])
    }

def show_hero(hero):
    print(f"{hero['name']} - {hero['class']}")
    print(f"HP: {hero['hp']}")
    print(f"Attack: {hero['attack']}")

hero = create_hero("John", "Mag")
show_hero(hero)