#i want to eventually be able to make it so someone could add thier own characters into the generator.

default_characters = ["Dani", "Wren", "Josh", "Logan", "Blaine", "Tuesday", "Lillian", "TJ", "Indigo", "Sage", "Jay", "Dee", "Sarah", "Chiqua", "Nikki", "Weregamer", "Haven"]
default_scenerios = [" goes on a date with ", " cooks for ", " has to save the life of ", " at the funeral of "]

num_characters = len(default_characters)
num_scenerios = len(default_scenerios)

import random
character_one = random.randint(0, num_characters)
character_two = random.randint(0, num_characters)
scenerio = random.randint(0, num_scenerios)

if character_one == character_two:
    character_one = random.randint(0, num_characters)


#final product for default gen
print("imagine that...")
print(default_characters[character_one], default_scenerios[scenerio], default_characters[character_two])