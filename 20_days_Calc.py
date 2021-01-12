from datetime import datetime,date
import sys

def main():
    print("Enter the dates in the format dd-mm-yyyy with/without any spaces")
    print("Enter the start Date:")
    start_date = input(">> ")
    print("Enter the Ending Date:")
    end_date = input(">> ")
    start_date = convert(start_date)
    end_date = convert(end_date)

    differnece = (end_date - start_date).days
    print(f"The number of days between the dates {start_date} and {end_date} is {abs(differnece)} days!")
    sys.exit()

def convert(d):
    print(d)
    try:
        d = map(int,d.split('-'))
        d = list(d)
        d = date(d[-1],d[-2],d[-3])
        return d
    except Exception as e:
        print(e)
        print("Enter a Valid Input as per the format dd-mm-yy")

while True:
    print("****************Days Calculator***********************")
    print("1. Start the Program")
    print("2. Exit")

    n = int(input("Enter the Choice: "))

    if n==1:
        main()
    elif n==2:
        print("Thank you for Using! Good Bye!")
        sys.exit()
    else:
        print("Enter a Valid Input")
        continue
