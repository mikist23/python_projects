import turtle
import random
WIDTH , HEIGHT = 500, 500

COLORS = ["red","green","blue","orange", "yellow", "black", "pink", "brown", "purple","cyan" ]


def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2 - 10 ): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric  try again!! ")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Number not in range !!! Try again")

def init_turtle():
    screen = turtle.Screen().setup(WIDTH, HEIGHT)
    screen = turtle.title("Turtle Racing Game !! ")
    # screen.title("Turtle Racing Game! ")

racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS)