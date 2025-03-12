# 002-exercise-character-class.py

# Create a class called Wizard that should have:
# - Properties for name, color (of their robes), and staff_power
# - A method called cast_spell that returns a message like:
#   "[name] casts a powerful spell with their [staff_power] staff!"

# Your code here:


class Wizard:
    def __init__(self, name, color, staff_power):
        self.name=name
        self.color=color
        self.staff_power=staff_power

    def cast_spell(self):
        return f"{self.name} casts a powerful spell with their {self.staff_power} staff!"
        



# Test your code with:
gandalf = Wizard("Gandalf", "grey", "magical")
print(gandalf.cast_spell())
