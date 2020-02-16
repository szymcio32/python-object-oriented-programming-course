class MineralWater:
    def __init__(self, sodium, calcium):
        self.sodium = sodium
        self.calcium = calcium

    def __eq__(self, other):
        return self.sodium == other.sodium and self.calcium == other.calcium

    def __lt__(self, other):
        return self.sodium < other.sodium and self.calcium < other.calcium

    def __ne__(self, other):
        return not self == other

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        return not self < other and not self == other

    def __ge__(self, other):
        return not self < other


mineral_water_1 = MineralWater(32.50, 124)
mineral_water_2 = MineralWater(10, 114)
mineral_water_3 = MineralWater(10, 114)

print(f'mineral_water_1 == mineral_water_2: {mineral_water_1 == mineral_water_2}')
print(f'mineral_water_1 < mineral_water_2: {mineral_water_1 < mineral_water_2}')
print(f'mineral_water_1 != mineral_water_2: {mineral_water_1 != mineral_water_2}')
print(f'mineral_water_1 <= mineral_water_2: {mineral_water_1 <= mineral_water_2}')
print(f'mineral_water_1 > mineral_water_2: {mineral_water_1 > mineral_water_2}')
print(f'mineral_water_1 >= mineral_water_2: {mineral_water_1 >= mineral_water_2}')
print('---------------')
print(f'mineral_water_2 == mineral_water_3: {mineral_water_2 == mineral_water_3}')
print(f'mineral_water_2 < mineral_water_3: {mineral_water_2 < mineral_water_3}')
print(f'mineral_water_2 != mineral_water_3: {mineral_water_2 != mineral_water_3}')
print(f'mineral_water_2 <= mineral_water_3: {mineral_water_2 <= mineral_water_3}')
print(f'mineral_water_2 > mineral_water_3: {mineral_water_2 > mineral_water_3}')
print(f'mineral_water_2 >= mineral_water_3: {mineral_water_2 >= mineral_water_3}')

