import requests
import json

n = int((input("Enter the number of words to be generated: ")))
try:
    URL = f"https://random-word-api.herokuapp.com/word?number={n}"
    print(f"Retriving Data from {URL}")
    print(f"Retriving............")
    req = requests.get(URL)
    data = req.json()
    print(f"Total number of words generated = {len(data)}")
    for i in data:
        print(i)
except:
    print("Check you internet connection or check the URL Entered!")
