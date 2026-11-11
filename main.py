
import random

superheroes = ["Iron Man", "Thor", "Hulk", "Spider-Man", "Black Widow"]
villains = ["Loki", "Doc Ock", "Thanos", "Green Goblin", "Red Skull"]

def calculate_attack(character):
    return 10 + random.randint(0, len(character))



hero = random.choice(superheroes)
villain = random.choice(villains)

hero_attack = calculate_attack(hero)
villain_attack = calculate_attack(villain)

print(f"{hero} vs {villain}")
print(f"{hero} hits {hero_attack}")
print(f"{villain} hits {villain_attack}")

if hero_attack > villain_attack:
    print(f"{hero} wins!")
elif hero_attack == villain_attack:
    print("It's a draw!")
else:
    print(f"{villain} wins!")