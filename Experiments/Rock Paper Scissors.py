import random

options = ("rock", "paper" , "scissors")
player = None
computer = random.choice(options)


while player not in options:
    player = input("Enter your choice(rock, paper, scissors): ")

print(f"player: {player}")
print(f"computer: {computer}")

if player == computer:
    print("Holy smokes it's a tie!")
elif player == "rock" and computer == "scissors":
    print("Well damn you win!") 
elif player == "paper" and computer == "rock":
    print("Well damn you win!")  
elif player == "scissors" and computer == "paper":
    print("Well damn you win!")  
else:
    print("Sorry you lose! Wanna try another game?")          
