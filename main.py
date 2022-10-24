import random

food = [
    'Pizza',
    'Pasta',
    'Schnitzel',
    'Kebap',
    'Sushi',
    'Burger',
]

# random.randint(1, 5) --> random number between 1 and 5
# random.choice(array) --> random item in this array

selected = random.choice(food) # randomly choose a friend

print('What should I eat today?')
print(selected)
