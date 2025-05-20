from game_objects import Player, Weapon, Enemy 
import random 
import time

player_character1 = Player('Gimli', 'Dwarf', 'Fighter', 3, 180)
player_character2 = Player('Alfred', 'Hybrid', 'Support', 20, 500)
player_character3 = Player('Lruke', 'Barbarian', 'Fighter', 10, 2000)
player_weapon1 = Weapon('Lil Jit', 'Melee', random.randint(12, 15))
player_weapon2 = Weapon('AK47', 'Short Range', random.randint(16, 20))
player_enemy1 = Enemy('Those Who Know', 'Elf Lord',  random.randint(50, 100), random.randint(50, 100))
player_enemy2 = Enemy('The Unknown', 'Gorick',  random.randint(100, 500), random.randint(200, 500))
print("Welcome to the game")
print("1. Name: Gimli \n Class: Dwarf \n Type: Fighter \n Attack: 3 \n Health: 180")
print("2. Name: Alfred \n Class: Hybrid \n Type: Support \n Attack: 20 \n Health: 500")
print("3. Name: Lruke \n Class: Barbarian \n Type: Fighter \n Attack: 10 \n Health: 2000")
time.sleep(5)
character_selection = int(input("What Character Would you like to play as: "))

if character_selection == 1:
    selected = player_character1
elif character_selection == 2:
    selected = player_character2
else:
    selected = player_character3

print(f"you have selected \n Name: {selected.name}\n Class: {selected.race}\n Type: {selected.cls}\n Attack: {selected.atk}\n Health:{selected.health}")
time.sleep(5)
print("Now which weapon would you like to use,")
print("1. Name: Lil Jit \n Type: Melee \n Random Damage: 12 - 15")
print("2. Name: AK47 \n Type: Short Range \n Random Damage: 16 - 20")
time.sleep(5)
weapon_selection = int(input("Select A Number"))

if weapon_selection == 1:
    selected1 = player_weapon1
else:
    selected1 = player_weapon2

print(f"you have selected \n Name: {selected1.name}\n Category: {selected1.category}\n Damage: {selected1.damage}")
time.sleep(5)
print("Now which enemy would you like to fight,")
print("1. Name: Those Who Know \n Type: Elf Lord \n Random Damage: 50 - 100 \n Random Health: 50 - 100")
print("2. Name: The Unknown \n Type: Gorick \n Random Damage: 100 - 500 \n Random Health: 200 - 500")
time.sleep(5)
enemy_selection = int(input("Select A Number: "))

if enemy_selection == 1:
    selected2 = player_enemy1
else:
    selected2 = player_enemy2

time.sleep(5)
print(f"You have choosen the character \n Name: {selected.name}\n Class: {selected.race}\n Type: {selected.cls}\n Attack: {selected.atk}\n Health:{selected.health} \n with the weapon \n Name: {selected1.name}\n Category: {selected1.category}\n Damage: {selected1.damage} \n and the enemy \n Name: {selected2.name}\n Type: {selected2.race}\n Damage: {selected2.damage}\n Health: {selected2.health}")

