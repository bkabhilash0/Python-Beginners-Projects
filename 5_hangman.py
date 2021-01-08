import random

lives = 7
words_and_clues = {"Apple":["It's a Fruit","It's red in colour"],
                    "Orange":["It's a Fruit","It's orange in colour"],
                    "Mango":["It's a Fruit","It's green or yellow in colour"],
                    "Toyota":["It's a car brand","Starts with T"],
                    "Suzukhi":["It's a car brand","Starts with S"],
                    "Python":["It's a Programming Language","Easy to learn"],
                    "JavaScript":["It's a Programming Language","Used in web development"],
                    "Java":["It's a Programming Language","Used in Android Apps"]}

def main(words_and_clues,lives,HANGMAN_PICS):
    HANGMAN_PICS
    word,clues = random.choice(list(words_and_clues.items()))
    guessed = ("_ "*len(word)).split()
    print(" ".join(guessed))
    while(lives>0):
        print(HANGMAN_PICS[len(HANGMAN_PICS)-lives])
        c = -1
        print(f"You have {lives} left!")
        print("Press 1 for a clue")
        choice = input(">> ")
        if choice == "1":
            if len(clues):
                clue = random.choice(clues)
                print(f'Clue 1 is {clue}')
                clues.remove(clue)
            else:
                print("No more clues left")
        elif choice.lower()==word.lower():
            print("Wow! You found the word and the word is",word)
            break
        else:
            choice = choice.lower()
            if choice in word.lower():
                print("The guess was right!")
                for i in word.lower():
                    c += 1
                    if i == choice:
                        guessed[c] = choice
            else:

                print("Sorry! It was a wrong guess")
                lives -= 1

        if result(word,guessed):
            break
    if lives == 0:
        print("You have no lives left")
        print("The word was",word)


def result(word,guessed):
        if word.lower() == ''.join(guessed):
            print("Wow! You found the word and the word is",word)
            return True
        print(" ".join(guessed))

HANGMAN_PICS = ['''
   +---+
       |
       |
      ===''','''
   +---+
   O   |
       |
       |
      ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']

main(words_and_clues,lives,HANGMAN_PICS)
