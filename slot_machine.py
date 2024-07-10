print("Welcome to the game!!!")
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
            print("Please antr a number!!!! ") 
    return amount
deposit()              
