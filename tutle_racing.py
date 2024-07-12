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

def create_turtles(color):
    turtles = []
    spacingx = WIDTH // (len(colors)+1)
    for i , color in enumerate(color):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1) * spacingx, -HEIGHT // 2 + 20 )
        racer.pendown()
        turtles.append(racer)
    return turtles    



def init_turtle():
    screen = turtle.Screen().setup(WIDTH, HEIGHT)
    screen = turtle.title("Turtle Racing Game !! ")
    # screen.title("Turtle Racing Game! ")

racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]
print(colors)
create_turtles(colors)