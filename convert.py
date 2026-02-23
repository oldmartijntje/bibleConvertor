import os
from pathlib import Path
import json

class Variation:
    def __init__(self, first, default, last):
        self.first = first
        self.default = default
        self.last = last

def writeMarkdown(content, name, appendedPath = ""):
    with open(f"./output/{appendedPath}{name}", "w") as f:
        f.write(content)
        f.close()
    print(f"Written: ./output/{appendedPath}{name}")

def readTemplate(name, onError):
    my_file = Path("./templates/" + name)
    if my_file.is_file() == False:
        onError()
    return my_file.read_text()

def replaceKey(content, key, value):
    return content.replace("{" + f"{key}" + "}", f"{value}")

def replaceIndexData(content, book_list, indexData):
    print(book_list)
    book_list_old = ""
    book_list_new = ""
    for x in range(len(indexData["books"])): 
        if x + 1 <= old_testament_amount:
            book_list_old = book_list_old + replaceKey(
                replaceKey(
                    book_list, 
                    "book", 
                    indexData["books"][x]["name"]
                ), 
                "book_chapters", 
                indexData["books"][x]["chapters"]
            ) + "\n"
        else:
            book_list_new = book_list_new + replaceKey(
                replaceKey(
                    book_list, 
                    "book", 
                    indexData["books"][x]["name"]
                ), 
                "book_chapters", 
                indexData["books"][x]["chapters"]
            ) + "\n"
    book_list_full = book_list_old + book_list_new
    content = replaceKey(content, "book_list", book_list_full)
    content = replaceKey(content, "book_list_old", book_list_old)
    content = replaceKey(content, "book_list_new", book_list_new)
    content = replaceKey(content, "source", indexData["source"])
    content = replaceKey(content, "version", indexData["version"])
    writeMarkdown(content, "index.md")

def replaceBookData(variation, bookData):
    pass

def replaceChapterData(variation, bookData, chapterNumber):
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

def missingFile(file, folder):
    errorOut(f"Missing an {file} in the {folder}/ folder.")

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

indexData = readJsonFile("index.json", lambda: missingFile("index.json", "bible/"))
index = readTemplate("index.md", lambda: missingFile("index.md", "templates"))
newIndex = replaceIndexData(index, readTemplate("book_list.md", lambda: missingFile("book_list.md", "templates")), indexData)



