from items import Item, Weapon, Potion

items = [
    Weapon("Rusty Sword", 3, "common"),
    Weapon("Steel Sword", 8, "rare"),
    Potion("Small Potion", 20, "common"),
    Potion("Large Potion", 60, "epic"),
    Item("Amulet of Wisdom", 5, "rare"),
]

# те саме, що filter + lambda, але читається як речення
rare = [item.name for item in items if item.rarity == "rare"]
print("Rare items:", rare)

# топ-3 найсильніших предмети
top3 = sorted(items, key=lambda item: item.power, reverse=True)[:3]
print("Top 3:", [f"{item.name} ({item.power})" for item in top3])

# словник: назва -> сила
power_by_name = {item.name: item.power for item in items}
print("Power:", power_by_name)