#banking program
#show balance, deposit and withdraw

def main():
    def show_balance():
        print(f"Your balance is ${account:.2f}")

    def deposit():
        deposit = float(input("How much do you want to deposit?: "))
        if deposit < 0:
            print("Please enter a valid number")
        else:
            return deposit

    def withdraw():
        withdraw = float(input("How much do you want to withdraw?: "))
        if withdraw <= 0:
            print("Please enter a valid number")
        else:
            return withdraw

    account = 0.0

    print("------------------------------")
    print("       YOUR ACCOUNT")
    print("------------------------------")
    print("Options: ")
    print("1.Show balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    print()

    while True:
        operation = input("What operation you want to execute?: ")
        operation = operation.capitalize()
        if operation == "Show balance":
            show_balance()
        elif operation == "Deposit":
            account += deposit()
        elif operation == "Withdraw":
            account -= withdraw()
        elif operation == "Exit":
            break
        else:
            print("Please enter a valid operation")

    print()
    print("Thank you! Have a nice day!")

if __name__ == "__main__":
    main()