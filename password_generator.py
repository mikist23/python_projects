print("Welcome to the game!!!!")

import string
import random

def generate_password(min_length, numbers = True, special_characters = True):
    letters = string.ascii_letters
    digits = string.digits
    special= string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters == special   

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

   

                  

    



generate_password(10) 