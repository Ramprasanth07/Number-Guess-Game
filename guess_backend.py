#Basic Structure :
import random

def get_difficulty():
    print("choose difficulty:")
    print("1.Easy (1-50, 10 attempts)")
    print("2.Medium (1-100, 7 attempts)")
    print("3.Hard (1-200, 5 attempts)")

    choice = input("Enter 1, 2 or 3:")
    if choice =="1":
        return 50 ,10
    elif choice =="2":
        return 100, 7
    elif choice =="3":
        return 200, 5
    else:
        print("Invalid chioce, defaulting to medium.")
        return 100, 7
    
#step-2 The guessing logic
def play_game():
    limit, attempts = get_difficulty()
    number = random .randint(1,limit)
    print(f"\nI picked a number 1 and {limit}. You have {attempts} attempts!\n")
    for i in range(attempts):
        remaining = attempts - i
        guess = int(input(f"Attempt {i+1} | {remaining} left - Your guess: "))

        if guess < number:
            print("Too Low!\n")
        elif guess > number:
            print("Too High!\n")
        else:
            print(f"👌Correct! You won in {i+1} attempts! ")
            return 
        
    print(f"😥Out of attempts! The number was {number}.")    

#Step3-Play again loop:
while True:
    play_game()
    again = input("\nPlay again? (yes/no): ")
    if again.lower() != "yes":
        print("Thanks for playing!")
        break