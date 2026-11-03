from items import Item, Weapon, Potion

items = [
    Weapon("Rusty Sword", 3, "common"),
    Weapon("Steel Sword", 8, "rare"),
    Potion("Small Potion", 20, "common"),
    Potion("Large Potion", 60, "epic"),
    Item("Amulet of Wisdom", 5, "rare"),
]

# sorted + lambda: сортуємо за силою, від найбільшої
by_power = sorted(items, key=lambda item: item.power, reverse=True)
print("By power:", [item.name for item in by_power])

# filter + lambda: залишаємо лише рідкісні
rare = list(filter(lambda item: item.rarity == "rare", items))
print("Rare items:", [item.name for item in rare])

# map + lambda: беремо лише назви
names = list(map(lambda item: item.name, items))
print("Names:", names)