import random
print("Welcome to the game!! ")

def roll():
    min_value = 1
    max_value = 6

    value = random.randint(min_value,max_value)
    return value

print(roll())