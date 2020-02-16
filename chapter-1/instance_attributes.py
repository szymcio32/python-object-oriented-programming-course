class Animal:
    pass

cat = Animal()
print(f'cat object: {cat}')

cat.color = 'white'
cat.name = 'Jasper'
print(f'cat name: {cat.name}')
print(f'cat color: {cat.color}')

dog = Animal()
print(f'dog object: {dog}')

dog.color = 'black'
dog.name = 'Max'
print(f'dog name: {dog.name}')
print(f'dog color: {dog.color}')

dog.color = 'grey'
print(f'dog new color: {dog.color}')