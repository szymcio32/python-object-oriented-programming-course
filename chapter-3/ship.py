class Ship:
    def __init__(self, damage):
        self.damage = damage

    def deal_damage(self):
        print(f'{self.__class__.__name__} dealt {self.damage} damage')


class BattleShip(Ship):
    def __init__(self, special_damage, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.special_damage = special_damage

    def deal_special_damage(self):
        print(f'{self.__class__.__name__} dealt extra {self.special_damage} damage')


class BigBattleShip(BattleShip):
    def __init__(self, bomb_damage, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bomb_damage = bomb_damage

    def deal_special_damage_twice(self):
        for _ in range(2):
            super().deal_special_damage()

    def use_bomb(self):
        print(f'{self.__class__.__name__} used a bomb and dealt {self.bomb_damage} damage')


class CargoShip(Ship):
    def __init__(self, capacity, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.capacity = capacity

    def transport(self):
        print(f'{self.__class__.__name__} transported {self.capacity} TEU')


ship = Ship(5)
battle_ship = BattleShip(special_damage=10, damage=5)
big_battle_ship = BigBattleShip(special_damage=10, damage=5, bomb_damage=20)
cargo_ship = CargoShip(capacity=10000, damage=0)

ship.deal_damage()
print('---------')
battle_ship.deal_damage()
battle_ship.deal_special_damage()
print('---------')
big_battle_ship.deal_damage()
big_battle_ship.deal_special_damage_twice()
big_battle_ship.use_bomb()
print('---------')
cargo_ship.deal_damage()
cargo_ship.transport()