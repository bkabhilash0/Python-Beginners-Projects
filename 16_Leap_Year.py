import sys

print("***********************************Leap Year Finder*******************************************")
print("Enter a Year to check if it is a leap year or Not?")

leap_years = [2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060, 2064, 2068,
            2072, 2076, 2080, 2084, 2088, 2092, 2096]

def leap_checker(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a Leap Year!!")
                return year
            else:
                print(f"{year} is not a Leap Year!!")
        else:
            print(f"{year} is a Leap Year!!")
            return year
    else:
        print(f"{year} is not a Leap Year!!")


def leap_checker_range(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return year
        else:
            return year

while True:
    print("Welcome to Leap Year Calculater")
    print("1. Check an year for a leap year.")
    print("2. Check leap year for a range of years.")
    print("3. Exit")
    print("Enter you choices:")
    choice = int(input(">> "))

    if choice == 1:
        try:
            print("Enter the year to be checked: ")
            year = int(input(">> "))
            leap_checker(year)
        except:
            print("Enter a Valid Year!")

    elif choice == 2:
        try:
            x = int(input("Enter the starting range for the year: "))
            y = int(input("Enter the ending range for the year: "))
            print(f'The list of Leap years in the range {x} to {y} are:')
            results = map(leap_checker_range,range(x,y))
            final_leap_years = [x for x in list(results) if x]
            print(final_leap_years)
        except:
            print("Enter a Valid Input")
    elif choice == 3:
        print("Thank You for Using!")
        sys.exit()

    else:
        print("Enter a Valid choice!")
        continue
