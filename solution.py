import requests
import json
date = input("Enter the date of the Wordle for which you would like the solution to. \nNote that the New York Times have not uploaded solutions for Wordles in the distant future yet.\nIMPORTANT: Use the format YYYY-MM-DD for the date\nDate: ")
baseString = f"https://www.nytimes.com/svc/wordle/v2/{date}.json"
response = json.loads(requests.get(baseString).text)["solution"]
print(f"That day's wordle solution was \"{response}\"")

