print("Welcome to the game!!! ")
import random

OPERAORS = ["+","-","*"]
MIN_OPERAND = 3
MAX_OPERAND = 12

def generate_problem():
    left = random.randint(MIN_OPERAND,MAX_OPERAND)
    right = random.randint(MIN_OPERAND,MAX_OPERAND)
    operator = random.choice(OPERAORS)

    expr = str(left) + " " + operator + " " + str(right)
    print(expr)
    return expr
    


generate_problem()