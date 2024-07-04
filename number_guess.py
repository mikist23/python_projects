print("Welcome to the Game! ") 

import random

top_range = input("Type a number ? ")

if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0 :
        print("Plesase type a number larger than zero next time")
        quit()

else:
    print("Plesase type a number next time")
    quit()
