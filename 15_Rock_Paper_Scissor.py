import random
import sys

choices = ['Rock','Paper','Scissors']
max = int(input("Enter the Maximum number of score for the game...\>> "))
score = 0
while score <= max:
    print(f"Score: {score}")
    print("Enter your Choice (as the index number):")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    n = int(input(">> ")) - 1
    if n == 3:
        print("Thank You for Playing! See you Soon...")
        sys.exit()
    choice = random.choice(choices)
    i = choices.index(choice)

    print(n)
    print(i)

    print(f'You choose {choices[n]}')
    print(f'Opponent Choose {choice}')

    if n == i:
        continue
    elif n == 0:
        if i == 1:
            print("Oops! Rock was covered by the Paper! You lose 1 point.")
            score -= 1
        else:
            print("Great! You crushed the Scissors with the Rock! You get 1 Point!!")
            score += 1
    elif n == 1:
        if i == 0:
            print("Great! You covered the rock with the Paper! You get 1 Point!!")
            score += 1
        else:
            print("Opps! The Scissor cut your Paper into Pieces! You lose 1 Point!")
            score -= 1
    else:
        if i == 0:
            print("Oops! You Scissors got crushed by the rock! You lose 1 Point!!")
            score -= 1
        else:
            print("Great! You cut the paper into Pieces! You get 1 Point!")
            score += 1
    if score < 0:
        score = 0
    elif score == max:
        print("Congrats! You won the game")
        print("Game Over")
        sys.exit()
