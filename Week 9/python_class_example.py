# Class - This is a blueprint for all players in out game.
class Player:
    #Create a constructor to build the object from the class.
    def __init__(self, name ,level,):
        # These are attributes. They belong to the specific player being created.
        self.name = name
        self.health = 100 # All Players start with 100 health.
        self.level = level
        self.inventory = [] # Start with an empty inventory

    # This is a method. It defines behavior
    def take_damage(self, amount):
        self.health -= amount #notice we use self to modify THIS object's health.
        print(f"{self.name} takes {amount} damage! Current health: {self.health}")

    #Another method for healling
    def heal(self, amount):
        self.health += amount
        if self.health > 100:
            self.health = 100 # Limits over healing to max health
        print(f"{self.name} heals for {amount}! Current health: {self.health}")

# Create two separate Player Objects from Our Blueprint Above

player1 = Player("JFK", 35)
player2 = Player("Me", 58)
enemy1 = Player("Hasan Piker", 1)

#Each Object has its OWN data
print(f"{player1.name} is level {player1.level}, has {player1.health}.")
print(f"{player2.name} is level {player2.level}, has {player2.health}.")
player2.level = 69000
print(f"{player2.name} is level {player2.level}, has {player2.health}.")

player1.take_damage(100)

print(f"{player1.name} now has {player1.health} left after getting no scoped")
print(f"{player2.name} got {player1.name}'s reboot card.")
player1.heal(100)