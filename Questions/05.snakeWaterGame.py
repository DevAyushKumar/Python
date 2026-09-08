import random

listOfItems = ["water", "gun", "snake"]

def game():
    print("Welcome to the gun, snake and water game! \n")
    user_choice = input("Choose what you want to take: \nGun \nwater \nSnake \n")

    computer_choice = random.choice(listOfItems)

    if user_choice.upper() == computer_choice.upper():
        print("draw")

    elif user_choice == "gun" and computer_choice == "water":
        print("Computer won") 

    elif user_choice == "water" and computer_choice == "snake":
        print("computer won")

    elif user_choice == "snake" and computer_choice == "gun":
        print("computer won")

    elif user_choice == "water" and computer_choice == "gun":
        print("user won")

    elif user_choice == "snake" and computer_choice == "water":
        print("user won")

    elif user_choice == "gun" and computer_choice == "snake":
        print("user won")

    else:
        print("invalid choice")

game()
a = int(input("Want to continue ? Enter 1 to continue and 2 to not"))
if a == 1:
    game()
