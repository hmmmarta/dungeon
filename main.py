from heroes import Warrior, Mag
from enemies import Boss
from items import Weapon, Potion

CLASSES = {"1": Warrior, "2": Mag}

choice = input("Choose your hero: 1 — Warrior, 2 — Mag: ")
name = input("Hero name: ")
hero = CLASSES.get(choice, Mag)(name)

sword = Weapon("Beginner sword", 4)
hero.inventory.add(sword)
hero.inventory.add(Potion("Small potion", 30))
sword.equip(hero)

boss = Boss("King of Goblins", 120, 11)
print(hero)
print(boss)

round_no = 1
while hero.is_alive() and boss.is_alive():
    print(f"\n--- Round {round_no} ---")
    if round_no % 3 == 0:
        damage = hero.special(boss)
        print(f"{hero.name} — special hit! -{damage}  (Boss has {boss.hp} HP)")
    else:
        damage = hero.hit(boss)
        print(f"{hero.name} hits {boss.name}: -{damage}  (Boss has {boss.hp} HP)")

    if boss.is_alive():
        damage = boss.hit(hero)
        print(f"{boss.name} hits {hero.name}: -{damage}  (hero has {hero.hp} HP)")

    if hero.is_alive() and hero.hp < hero.max_hp * 0.4:
        potion = hero.inventory.use_potion(hero)
        if potion:
            print(f"{hero.name} drinks «{potion.name}»: HP {hero.hp}")

    round_no += 1

print("\nVictory!" if hero.is_alive() else "\nGame over...")