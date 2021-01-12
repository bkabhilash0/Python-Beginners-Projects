import sys

def main():
    print("Enter the String to be Reversed!")
    word = input(">> ")
    reversed_word = ""
    for letter in reversed(word):
        reversed_word += letter
    print(f"The reverse of the word {word} is {reversed_word}\n")

running = True
while running:
    print("*************Welcome to String Reversal Program************************")
    print("1. Start the Program")
    print("2. Exit")

    try:
        n = int(input("Enter your Choice: "))
    except:
        print("Enter a valid input!")
        continue
        
    if n==1:
        main()
    elif n==2:
        print("Thank you for Using! Good Bye!")
        sys.exit()
        running = False
    else:
        print("Enter a Valid Input")
        continue
