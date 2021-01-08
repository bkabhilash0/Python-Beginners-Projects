import sys

email = input("Enter the Email Id: ").strip()

if '@' not in email:
    print("Enter a valid email!!")
    sys.exit()

splitted = email.split("@")

print(f'email: {email}')
print(f'username: {splitted[0]}')
print(f'domain: {splitted[1]}')
