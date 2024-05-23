import random

player_input = input("Choose [r]ock, [p]aper, [s]cissors: ")


computer_move = None
player_move = None

computer_choosemove = random.randint(1,3)

if computer_choosemove == 1:
    computer_move = "Rock"
elif computer_choosemove == 2:
    computer_move = "Paper"
else:
    computer_move = "Scissors"

if player_input == "r":
    player_move = "Rock"
elif player_input == "p":
    player_move = "Paper"
elif player_input == "s":
    player_move = "Scissors"
else:
    raise SystemExit("Invalid Player Input. Try again.")

if (player_move == "Rock" and computer_move == "Scissors") or \
        (player_move == "Paper" and computer_move == "Rock") or \
        (player_move == "Scissors" and computer_move == "Paper"):
    print(f"Computer chose {computer_move}, you chose {player_move} that means...")
    print("YOU WIN!")
elif player_move == computer_move:
    print(f"Computer chose {computer_move}, you chose {player_move} that means...")
    print("ITS A TIE!")
else:
    print(f"Computer chose {computer_move}, you chose {player_move} that means...")
    print("You lost... :(")