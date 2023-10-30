#i want to eventually be able to make it so someone could add thier own characters into the generator.

default_characters = ["Dani", "Wren", "Josh", "Logan", "Blaine", "Tuesday", "Lillian", "TJ", "Indigo", "Sage", "Jay", "Dee", "Sarah", "Chiqua", "Nikki", "Weregamer", "Haven"]
default_scenarios = ["goes on a date with", "cooks for", "has to save the life of", "at the funeral of"]

import tkinter as tk

def run_script():
    num_characters = len(default_characters)-1
    num_scenarios = len(default_scenarios)-1

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
    text_box.insert(tk.END,"imagine that... ")
    text_box.insert(tk.END, character_one + ' ' + scenario +' ' +character_two)
    text_box.insert(tk.END,"\n")
    
    

root = tk.Tk()
root.title("Art Scenario Generator")
button = tk.Button(root, text="Run Script", command=run_script)
button.pack()

text_box = tk.Text(root)
text_box.pack()

root.mainloop()