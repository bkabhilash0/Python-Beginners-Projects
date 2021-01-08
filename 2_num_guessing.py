import random
import time

def main(lives,g):
    global n
    if lives != 0:
        print(f"You have {lives} guesses left!")
        lives -= 1

        try:
            n = int(input("Guess the Number: "))
        except ValueError:
            print("Enter a valid guess!")
            time.sleep(2)
            main(lives+1,g)         # Dont redude the life for a invalid input

        if n > g:
            print("The Actual number is less than you guess!")
            main(lives,g)
        elif n < g:
            print("The Actual number is greater than you guess!")
            main(lives,g)
        else:
            print(f"The generated number: {g}")
            print(f'The number you Guessed: {n}')
            print("Congrats! You guessed the correct number!")
            replay()

    else:
        print("Your guesses have exhausted!")
        fail(g,n)

def replay():
        global lives
        choice = input("Do you want to continue?\nY:Yes\nN:No\nEnter you choice: ")
        if choice.lower() == 'y':
            main(lives,random.randint(0,11))
        elif choice.lower() == 'n':
            print("Thank you for playing!")
        else:
            print("Enter a Valid Choice!")
            time.sleep(1)
            replay()

def fail(g,n):
        print(f"The generated number: {g}")
        print(f'The number you Guessed: {n}')
        print("Opps! The number you guess was wrong!")
        replay()

n = 0
g = random.randint(0,10)
lives = 5
main(lives,g)
