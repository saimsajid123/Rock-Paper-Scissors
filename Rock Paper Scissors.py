import os
import random
while True:
    def clearscreen ():
        os.system("cls" if os.name == "nt" else "clear")


    clearscreen()
    print("\n Enter One Of These 3 Options Which Are \nrock/paper/scissors : ")
    use = input()

    com = ["rock", "paper", "scissors"]
    cpu = random.choice(com)
    print(f"\nUser Selected : {use}")
    print(f"\nComputer Selected : {cpu}")
    print("\nYou Result is : ")
    if (use == "rock" and cpu == "rock"):
        print("                 Draw")
    elif (use == "rock" and cpu == "paper"):
        print("                 Computer Won")
    elif (use == "rock" and cpu == "scissors"):
        print("                 You Won")
    elif (use == "paper" and cpu == "paper"):
        print("                 Draw")
    elif (use == "paper" and cpu == "rock"):
        print("                 You Won")
    elif (use == "paper" and cpu == "scissors"):
        print("                 You Won")
    elif (use == "scissors" and cpu == "paper"):
        print("                 You Won")
    elif (use == "scissors" and cpu == "scissors"):
        print("                 Draw")
    elif (use == "scissors" and cpu == "rock"):
        print("                 Computer Won")
