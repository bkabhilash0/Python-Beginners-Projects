import sys

# passage = '''During the first part of your life, you only become aware of happiness once you have lost it. Then an age comes,
#     a second one, in which you already know, at the moment when you begin to experience true happiness, that you are, at
#     the end of the day, going to lose it. When I met Belle, I understood that I had just entered this second age. I also
#     understood that I hadn’t reached the third age, in which anticipation of the loss of happiness prevents you from living.'''


def through_input(passage):
    words = passage.split()
    word_frequency = {}

    for word in words:
        word_frequency[word] = word_frequency.get(word,0)+1

    print(word_frequency,end="\n")
    print("-------------------------------------------------------")

def through_file():
    FILE_NAME = input("Enter the File Name: ")
    try:
        with open(FILE_NAME,'r') as fh:
            data = fh.read()
            through_input(data)
    except FileNotFoundError:
        print("File not Found!")
        sys.exit()

running = True
while running:
    print("*******************Word Frequency Finder*****************")
    print("Select a Mode:")
    print("1. Input the text Directly")
    print("2. Input a text file to find the Frequency!")
    print("3. Exit")

    try:
        n = int(input("Enter your Choice: "))
    except Exception as e:
        print(e)
        print("Enter a Valid input!")
        continue
    if n == 1:
        print('Enter the Passage below:')
        passage = input("> ")
        through_input(passage)
    elif n==2:
        through_file()
    elif n==3:
        running = False
        sys.exit()
    else:
        print("Enter a Valid Input!")
        continue
