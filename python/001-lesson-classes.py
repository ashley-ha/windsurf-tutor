# 001-lesson-classes.py

class Character:
    def __init__(self, name, race, weapon):
        self.name = name
        self.race = race
        self.weapon = weapon
    
    def introduce(self):
        return f"I am {self.name}, a {self.race}, and I wield a {self.weapon}."

# Example usage
aragorn = Character("Aragorn", "Human", "sword")
print(aragorn.introduce())
