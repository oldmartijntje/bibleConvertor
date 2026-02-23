import os
from pathlib import Path
import json

def writeMarkdown():
    pass

def readTemplate():
    pass

def generateMarkdownFile():
    pass

def readJsonFile(name, onError):
    my_file = Path("./bible/" + name)
    if my_file.is_file() == False:
        onError()
    else: 
        with open('./bible/index.json') as f:
            return json.load(f)

def errorOut(text):
    print(text + "\nExiting...")
    exit()

print("The bible folder is the folder that should contain your bible data.")
print("This bible data should be in the .json format. Read the README.md for more information.")
while True:
    correct = input("Is your setup correct? (Y/N): ")
    if correct.capitalize() == "Y":
        break
    elif correct.capitalize() == "N":
        print("Make sure it is setup correctly.")
        exit()
    else:
        print("That is not a valid input.")

old_testament_amount = 39

newpath = "./output"
if not os.path.exists(newpath):
    os.makedirs(newpath)
newpath = "./bible"
if not os.path.exists(newpath):
    os.makedirs(newpath)

data = readJsonFile("index.json", lambda: errorOut("Missing an index.json in bible/"))




