#TODO
# Create OrcRace class which has following attributes and methods:
#   - class attribute:
#       BATTLE_CRY
#   - instance attributes:
#       name
#       damage
#       health
#       production_cost
#   - instance methods:
#       deal_damage() - the method will print information about dealt damage, name of the unit and use battle cry
#       go_to() - the method accepts two arguments (coordinates) and print the information about unit movement


class OrcRace:
    BATTLE_CRY = "Lok'tar!"

    def __init__(self, name, damage, health, cost):
        self.name= name
        self.damage = damage
        self.health = health
        self.production_cost = cost

    def deal_damage(self):
        print(self.BATTLE_CRY)
        print(f'Unit {self.name} dealt {self.damage} damage!')

    def go_to(self, x, y):
        print(f'Unit {self.name} is going to {x}, {y}')


orc = OrcRace('orc', 20, 20, 10)
troll = OrcRace('troll', 25, 10, 8)
tauren = OrcRace('tauren', 35, 40, 25)

units = []
units.append(orc)
units.append(troll)
units.append(tauren)

for unit in units:
    unit.go_to(50, 50)
    unit.deal_damage()
