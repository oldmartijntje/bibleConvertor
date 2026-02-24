import os
from pathlib import Path
import json

class Variation:
    def __init__(self, first, default, last, single = None):
        self.first = first
        self.default = default
        self.last = last
        self.single = single

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
            )
        else:
            book_list_new = book_list_new + replaceKey(
                replaceKey(
                    book_list, 
                    "book", 
                    indexData["books"][x]["name"]
                ), 
                "book_chapters", 
                indexData["books"][x]["chapters"]
            )
    book_list_full = book_list_old + book_list_new
    content = replaceKey(content, "book_list", book_list_full)
    content = replaceKey(content, "book_list_old", book_list_old)
    content = replaceKey(content, "book_list_new", book_list_new)
    content = replaceKey(content, "source", httpsify(indexData["source"]))
    content = replaceKey(content, "version", indexData["version"])
    createFolderIfNotExist(lowerSpaceless(f"./output/{indexData["version"]}"))
    writeMarkdown(content, f"Bible - {indexData["version"]}.md", lowerSpaceless(indexData["version"]) + "/")

def lowerSpaceless(string):
    return string.replace(" ", "_").lower()

def lookupBook(id, indexData):
    if id < 0:
        return "null"
    elif id +1 > book_amount:
        return "null"
    return indexData["books"][id]["name"]

def replaceBookData(book_variation, bookData, bookNumber, chapter_list, indexData, chapter_variation, verse_template):
    content = book_variation.default
    if bookNumber == 0 and bookNumber + 1 == book_amount:
        content = book_variation.single
    elif bookNumber == 0:
        content = book_variation.first
    elif bookNumber + 1 == book_amount:
        content = book_variation.last
    chapter_list_exported = ""

    for x in range(len(bookData["chapters"])): 
        chapter_list_exported = chapter_list_exported + replaceKey(
            replaceKey(
                chapter_list, 
                "book", 
                bookData["book"]
            ), 
            "chapter_number", 
            x+1
        )

    content = replaceKey(content, "chapter_list", chapter_list_exported)
    content = replaceKey(content, "book", bookData["book"])
    content = replaceKey(content, "book_lower", lowerSpaceless(bookData["book"]))
    content = replaceKey(content, "book_previous", lookupBook(bookNumber - 1, indexData))
    content = replaceKey(content, "book_previous_lower", lowerSpaceless(lookupBook(bookNumber - 1, indexData)))
    content = replaceKey(content, "book_next", lookupBook(bookNumber + 1, indexData))
    content = replaceKey(content, "book_next_lower", lowerSpaceless(lookupBook(bookNumber + 1, indexData)))
    content = replaceKey(content, "version", bookData["version"])
    content = replaceKey(content, "book_chapters", len(bookData["chapters"]))
    content = replaceKey(content, "old_new_testament", "old" if bookNumber + 1 <= old_testament_amount else "new")
    content = replaceKey(content, "oude_nieuwe_testament", "oude" if bookNumber + 1 <= old_testament_amount else "nieuwe")
    content = replaceKey(content, "source", httpsify(bookData["source"]))
    createFolderIfNotExist(lowerSpaceless(f"./output/{bookData["version"]}/{bookData["book"]}"))
    writeMarkdown(content, f"{bookData["book"]}.md", lowerSpaceless(f"{bookData["version"]}/{bookData["book"]}/"))
    for y in range(len(bookData["chapters"])):
        replaceChapterData(chapter_variation, bookData, bookNumber, y+1, verse_template)

def httpsify(link):
    if "http" not in link:
        link = f"https://{link}"
    return link

def replaceChapterData(chapter_variation, bookData, bookNumber, chapterNumber, verse_template):
    chapterData = bookData["chapters"][f"{chapterNumber}"]
    verses = ""
    content = chapter_variation.default
    if chapterNumber == 1 and chapterNumber == len(bookData["chapters"]):
        content = chapter_variation.single
    elif chapterNumber == 1:
        content = chapter_variation.first
    elif chapterNumber == len(bookData["chapters"]):
        content = chapter_variation.last
    for x in range(len(chapterData)): 
        verses = verses + replaceKey(
            replaceKey(
                replaceKey(
                    verse_template, 
                    "verse", 
                    chapterData[x]["text"]
                ), 
                "book", 
                bookData["book"]
            ), 
            "verse_number", 
            chapterData[x]["verse"]
        )
    content = replaceKey(content, "chapter_text", verses)
    content = replaceKey(content, "chapter_number", chapterNumber)
    content = replaceKey(content, "book", bookData["book"])
    content = replaceKey(content, "book_lower", lowerSpaceless(bookData["book"]))
    content = replaceKey(content, "chapter_previous", chapterNumber - 1)
    content = replaceKey(content, "book_previous", lookupBook(bookNumber - 1, indexData))
    content = replaceKey(content, "book_previous_lower", lowerSpaceless(lookupBook(bookNumber - 1, indexData)))
    content = replaceKey(content, "chapter_next", chapterNumber + 1)
    content = replaceKey(content, "book_next", lookupBook(bookNumber + 1, indexData))
    content = replaceKey(content, "book_next_lower", lowerSpaceless(lookupBook(bookNumber + 1, indexData)))
    content = replaceKey(content, "version", bookData["version"])
    content = replaceKey(content, "book_chapters", len(bookData["chapters"]))
    content = replaceKey(content, "old_new_testament", "old" if bookNumber + 1 <= old_testament_amount else "new")
    content = replaceKey(content, "oude_nieuwe_testament", "oude" if bookNumber + 1 <= old_testament_amount else "nieuwe")
    content = replaceKey(content, "source", httpsify(bookData["source"]))

    writeMarkdown(content, f"{bookData["book"]} - {chapterNumber}.md", lowerSpaceless(f"{bookData["version"]}/{bookData["book"]}/"))

def createFolderIfNotExist(path):
    if not os.path.exists(path):
        os.makedirs(path)

def readJsonFile(name, onError):
    my_file = Path("./bible/" + name)
    if my_file.is_file() == False:
        onError()
    else: 
        with open("./bible/" + name) as f:
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
book_amount = 66

createFolderIfNotExist("./output")
createFolderIfNotExist("./bible")

indexData = readJsonFile("index.json", lambda: missingFile("index.json", "bible/"))
index = readTemplate("index.md", lambda: missingFile("index.md", "templates"))
newIndex = replaceIndexData(index, readTemplate("book_list.md", lambda: missingFile("book_list.md", "templates")), indexData)

for x in range(len(indexData["books"])):
    book = indexData["books"][x]
    bookData = readJsonFile(book["filename"], lambda: missingFile(book["filename"], "bible/"))
    book_variation = Variation(
        readTemplate("book_first.md", lambda: missingFile("book_first.md", "templates")),
        readTemplate("book.md", lambda: missingFile("book.md", "templates")),
        readTemplate("book_last.md", lambda: missingFile("book_last.md", "templates"))
    )
    chapter_variation = Variation(
        readTemplate("chapter_first.md", lambda: missingFile("chapter_first.md", "templates")),
        readTemplate("chapter.md", lambda: missingFile("chapter.md", "templates")),
        readTemplate("chapter_last.md", lambda: missingFile("chapter_last.md", "templates")),
        readTemplate("chapter_single.md", lambda: missingFile("chapter_single.md", "templates"))
    )
    replaceBookData(book_variation,
                        bookData, 
                        x, 
                        readTemplate("chapter_list.md", lambda: missingFile("chapter_list.md", "templates")), 
                        indexData, 
                        chapter_variation,
                        readTemplate("verse.md", lambda: missingFile("verse.md", "templates"))
                    )

