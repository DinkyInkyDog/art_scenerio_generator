#i want to eventually be able to make it so someone could add thier own characters into the generator.

default_characters = ["Dani", "Wren", "Josh", "Logan", "Blaine", "Tuesday", "Lillian", "TJ", "Indigo", "Sage", "Jay", "Dee", "Sarah", "Chiqua", "Nikki", "Weregamer", "Haven"]
default_scenarios = ["goes on a date with", "cooks for", "has to save the life of", "at the funeral of"]

num_characters = len(default_characters)
num_scenarios = len(default_scenarios)

import random
c = random.randint(0, num_characters)
cc = random.randint(0, num_characters)
s = random.randint(0, num_scenarios)

if c == cc:
    c = random.randint(0, num_characters)

character_one = default_characters[c]
character_two = default_characters[cc]
scenario = default_scenarios[s]

#final product for default gen
print("imagine that...")
print(character_one, scenario, character_two)