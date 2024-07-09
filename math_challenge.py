print("Welcome to the game!!! ")
import random
import time

OPERAORS = ["+","-","*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND,MAX_OPERAND)
    right = random.randint(MIN_OPERAND,MAX_OPERAND)
    operator = random.choice(OPERAORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    # print(expr, answer)
    return expr, answer
wrong = 0
input('Press enter to start ')
print("------------Start----------------")
start_time = time.time()
for i in range(TOTAL_PROBLEMS):
    expr , answer = generate_problem()
    while True:
        guess = input("Problem # "+ str(i+1)+ ": " + expr + " = ")
        if guess == str(answer):
            wrong += 1
            break
print("------------End----------------")  
end_time = time.time()  
total_time = time.ctime(end_time - start_time)
print(f"You finished in {end_time :.2}")      
      