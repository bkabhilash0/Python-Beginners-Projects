import sys
import time

def main(n):
    isAscending = mode_select()
    l = len(n)

    for i in range(l-1):
        for j in range(l-i-1):
            if isAscending:
                if n[j] > n[j+1]:
                    n[j],n[j+1] = n[j+1],n[j]
            else:
                if n[j] < n[j+1]:
                    n[j],n[j+1] = n[j+1],n[j]
    print(n)

def mode_select():
    print("1. Sort in Ascending Order.")
    print("2. Sort in Decending Order.")
    try:
        mode = int(input(">> "))
    except:
        print("Choose a Valid Mode !!!")
        mode_select()
    if mode == 1:
        print("The Array in Ascending Order is")
        return True
    elif mode==2:
        print("The Array in Decending Order is")
        return False
    else:
        print("Choose a Valid Mode !!!")
        mode_select()

print("******************Bubble Sort Program**************************")
print("Enter the numbers to be sorted separated by commas e.g: 1,2,3,4,2,1,4")
try:
    numbers = input(">> ").split(",")
    numbers = list(map(int, numbers))
except Exception as e:
    print("Enter Valid Inputs!!!")
    print("Exiting....")
    time.sleep(1)
    sys.exit()

main(numbers)
