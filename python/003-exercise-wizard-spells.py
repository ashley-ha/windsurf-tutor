# 003-exercise-wizard-spells.py

# Enhance the Wizard class with the following:
# - Add a magic_power property that starts at 100
# - Add a list of known_spells (passed in during initialization)
# - Create a method called learn_spell that adds a new spell to known_spells
# - Modify cast_spell to:
#   - Take a spell_name parameter
#   - Check if the wizard knows the spell
#   - Use 10 magic_power for each spell cast
#   - Return an error message if magic_power is too low or spell is unknown

class Wizard:
    def __init__(self, name, color, staff_power, known_spells):
        self.name=name
        self.color=color
        self.staff_power=staff_power
        self.known_spells=known_spells

    def learn_spell(self, new_spell):
        # Your code here
        pass

    def cast_spell(self, spell_name):
        if spell_name in self.known_spells:
            pass



# Test your code with:
gandalf = Wizard("Gandalf", "grey", "magical", ["light", "shield"])
print(gandalf.cast_spell("light"))  # Should work
print(gandalf.cast_spell("fireball"))  # Should say spell is unknown
gandalf.learn_spell("fireball")
print(gandalf.cast_spell("fireball"))  # Should work
# Cast many spells until magic_power is too low
for _ in range(10):
    print(gandalf.cast_spell("light"))
