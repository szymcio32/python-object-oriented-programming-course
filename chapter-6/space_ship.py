class SpaceShip:
    def attack(self):
        raise NotImplementedError("Attack method must be implemented")


class LightSpaceShip(SpaceShip):
    dmg = 5

    def attack(self):
        print(f'Light attack: {self.dmg} dmg')


class HeavySpaceShip(SpaceShip):
    dmg = 10

    def attack(self):
        print(f'Heavy attack: {self.dmg} dmg')


class MagicSpaceShip(SpaceShip):
    dmg = 15

    def attack(self):
        print(f'Magic attack: {self.dmg} dmg')


class TankSpaceShip(SpaceShip):
    dmg = 20

    def attack(self):
        print(f'Tank attack: {self.dmg} dmg')


light_ship = LightSpaceShip()
heavy_ship = HeavySpaceShip()
magic_ship = MagicSpaceShip()
tank_ship = TankSpaceShip()

space_ships_array = [light_ship, heavy_ship, magic_ship, tank_ship]

for space_ship in space_ships_array:
    space_ship.attack()
