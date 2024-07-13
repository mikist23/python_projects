print("Welcome to the game!!!!")

import string
import random

def generate_password(min_length, numbers = True, special_characters = True):
    letters = string.ascii_letters
    numbers = string.digits
    special= string.punctuation

    print(letters , numbers , special)



generate_password(10)