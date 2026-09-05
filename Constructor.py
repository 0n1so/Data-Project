import random
import os

class build:
    def __init__(self, material1 = None, material2 = None):
        self.material1 = material1
        self.material2 = material2

    

    def generate_materials(self):
        self.material1 = random.choice(["Wood", "Metal", "Plastic"])
        self.material2 = random.choice(["Wood", "Metal", "Plastic"])
        return f"Material 1: {self.material1}, Material 2: {self.material2}"

b = build()

print(b.generate_materials())

if b.material1 == "Wood" and b.material2 == "Wood":
    print("Both materials are Wood")
    os.system('cls' if os.name == 'nt' else 'clear' )
