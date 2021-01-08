def binary_search(n,x):
    n = sorted(n)
    print(n)
    low = 0
    high = len(n) - 1

    while low <= high:
        mid = (low + high)//2
        if n[mid] > x:
            high = mid - 1
        elif n[mid] < x:
            low = mid + 1
        else:
            return mid

    return -1

# Test array
# arr = [2, 3, 4, 10, 40]
# x = 10

print("Enter the elements of array seperated by a space")
arr = list(map(int,input(">>").split(" ")))
print("Enter the element to search!")
x = int(input(">>"))

# Function call
result = binary_search(arr, x)

if result != -1:
    print(f"Element found at position {result}!")
else:
    print("Element not found!")
