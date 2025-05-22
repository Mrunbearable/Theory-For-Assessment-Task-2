from weapons import weapon, sword, bow, long_bow

PC = weapon("PC", "long-range", 1000)
cool_sword = sword("cool sword", "melee", 456, "slashing")
wow_bow = bow("wow_bow", "long-range", 777, "piercing")
wooooooow_bow = long_bow("wooooooow_bow", "long-range", 7777, "piercing", 150)
ow_bow = long_bow("ow_bow", "short-range", 7, "piercing", 80)

print(PC)