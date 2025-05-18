print("Characters: Lil jit, big jit, long jit, jit bit")
selection = input("Choose Character")


from game_objects import Player, Weapon, Enemy # MUST have this in the program
import random #For random damage and health
# Create an instance of Player
player_character = Player('Gimli', 'Dwarf', 'Fighter', 3, 180)

# TODO: Create an instance of Weapon with random damage between 12 and 15
player_weapon = Weapon('Lil jit', 'melee', random.randint(12, 15))

# TODO: Create an instance of Enemy with random damage between 15 and 18, and random health between 80 and 140
player_enemy = Enemy('Those Who Know', 'Elf',  random.randint(15, 18), random.randint(80, 140))

# Print the player character details
print(f"Player Name: {player_character.name}")
print(f"Player Race: {player_character.race}")
print(f"Player Class: {player_character.cls}")
print(f"Player Attack: {player_character.atk}")
print(f"Player Health: {player_character.health}")

# TODO: Print the player weapon details
print(f"Weapon Name: {player_weapon.name}")
print(f"Weapon Category: {player_weapon.category}")
print(f"Weapon Damage: {player_weapon.damage}")

# TODO: Print the enemy character details

print(f"Enemy Name: {player_enemy.name}")
print(f"Enemy Race: {player_enemy.race}")
print(f"Enemy Damage: {player_enemy.damage}")
print(f"Enemy Health: {player_enemy.health}")