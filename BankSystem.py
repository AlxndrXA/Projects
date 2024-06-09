import random

card_list = []


def withdraw_funds():
    while True:
        card_number = int(input("Enter your card number: "))

        if card_number == 0:
            break

        card_found = False
        for card in card_list:
            if card[0] == card_number:
                card_found = True
                break
        if card_found:
            card_in_system_pin_withdraw(card_number)
            break
        else:
            print("not in system")
            continue

def check_card_info():
    while True:
        card_number = int(input("Enter your card number: "))

        if card_number == 0:
            break

        card_found = False
        for card in card_list:
            if card[0] == card_number:
                card_found = True
                break
        if card_found:
            print(f"Balance : {card[2]}")
            break
        else:
            print("not in system")
            continue


def deposit_funds():
    while True:
        card_number = int(input("Enter your card number: "))

        if card_number == 0:
            break

        card_found = False
        for card in card_list:
            if card[0] == card_number:
                card_found = True
                break
        if card_found:
            card_in_system_pin_deposit(card_number)
            break
        else:
            print("not in system")
            continue

def card_in_system_pin_deposit(card_number):
    while True:
        pin = int(input("Enter pin: "))

        if pin == 0:
            break

        piniscorrect = False

        for card in card_list:
            if card[0] == card_number and card[1] == pin:
                piniscorrect = True
                break

        if piniscorrect:
            print("Logging in...")
            print(f"Balance : {card[2]}")
            funds = int(input("Enter funds to deposit : "))

            if funds > 0:
                card[2] += funds
                print(f"Successfully deposited {funds}")
                break
            else:
                print("Input can't be lower than 0.")
                break
def card_in_system_pin_withdraw(card_number):
    while True:
        pin = int(input("Enter pin: "))

        if pin == 0:
            break

        piniscorrect = False

        # card info
        balance = 0
        #

        for card in card_list:
            if card[0] == card_number and card[1] == pin:
                piniscorrect = True
                break
        if piniscorrect:
            print("Logging in...")
            print(f"Balance : {card[2]}")
            funds = int(input("Enter funds to withdraw : "))

            if funds < card[2]:
                card[2] -= funds
                print(f"Successfully withdrew {funds}")
            else:
                print("No available funds to withdraw.")

            break
        else:
            print("pin not correct")

def create_card():
    print("Creating card.")
    card_number = 0
    card_pin = 0
    while True:
        card = random.randint(0, 9999999999)
        if card < 1000000000:
            continue
        else:
            card_number = card
            break
    print(f"Created card number : {card_number}")
    print("-------------")
    while True:
        pin = random.randint(0,9999)
        if pin < 1000:
            continue
        else:
            card_pin = pin
            break
    print(f"PIN CREATED : {pin}")
    print("Adding card to database...")
    card_list.append([card_number,card_pin,0])
    print("Exiting...")
    exit = input("Click enter to continue.")

def main():
    while True:
        print("Welcome to IBank")
        print("[1] Create a card")
        print("[2] Withdraw funds")
        print("[3] Deposit funds")
        print("[4] Check balance")
        print("--")
        print("0 to exit a menu")
        command = input("Choose option : ")

        if command == "1":
            create_card()
        elif command == "2":
            withdraw_funds()
        elif command == "3":
            deposit_funds()
        elif command == "4":
            check_card_info()
        elif command == "adminpass":
            print(card_list)
        elif command == "0":
            break

if __name__ == '__main__':
    main()
