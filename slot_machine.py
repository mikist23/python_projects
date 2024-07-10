print("Welcome to the game!!!")
MAX_LINES = 3




def deposit():
    while True:
        amount = input("Enter ammount you want to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greter than 0")

        else:
            print("Please anter a number!!!! ") 
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter A NUMBER OF LINES YOU WANT TO BEET ON (1-"+ str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")

        else:
            print("Please anter a number!!!! ") 

    return lines

def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance,lines)
main()