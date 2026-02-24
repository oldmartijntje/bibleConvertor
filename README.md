# bibleConvertor
a simple script for me to format bile json files into markdown

## Installation

You need to copy your bible json files into the `bible/` folder. This folder must contain 1 json file per bible book + an index.json.

You can check if you have setup correctly by counting, there should be 67 json files, because there are 66 bible books.

A good way to gain these json files is by using a tool like [this](https://github.com/oldmartijntje/BibleDownloader).

Keep in mind that you are only allowed to download information that you already own. Piracy is not allowed.

## Customization

You can convert your bible.json into your personalised markdown format by editing the template files in the `templates/` folder.

### Template Variables

Each template file supports different variables depending on where that content is used. Variables are referenced using curly braces, e.g., `{variable_name}`.

#### Index Template (`index.md`)
The main index page of the bible. Available variables:
- `{version}`: The bible translation version name
- `{source}`: The source/URL where the bible data came from
- `{book_list_old}`: The list of all Old Testament books
- `{book_list_new}`: The list of all New Testament books
- `{book_list}`: All books combined (Old + New Testament)
The `{book_list}` will be formatted in the way you customize `book_list.md`.

#### Book Templates (`book.md`, `book_first.md`, `book_last.md`)
Pages for each individual bible book. Available variables:
- `{book}`: The name of the book (e.g., Genesis, Matthew)
- `{book_previous}`: The name of the previous book (or "null" if first book)
- `{book_next}`: The name of the next book (or "null" if last book)
- `{version}`: The bible translation version name
- `{source}`: The source/URL where the bible data came from
- `{book_chapters}`: The number of chapters in this book
- `{old_new_testament}`: Either "old" or "new" (for the testament type)
- `{oude_nieuwe_testament}`: Dutch equivalent: either "oude" or "nieuwe"
- `{chapter_list}`: A formatted list of all chapters in this book
The `{chapter_list}` will be formatted in the way you customize `chapter_list.md`.

**Variations**: Use `book_first.md` for the first book, `book_last.md` for the last book, and `book.md` as the default template for all other books.

#### Chapter Templates (`chapter.md`, `chapter_first.md`, `chapter_last.md`, `chapter_single.md`)
Pages for each chapter within a book. Available variables:
- `{chapter_number}`: The chapter number (e.g., 1, 2, 3)
- `{book}`: The name of the book this chapter belongs to
- `{chapter_previous}`: The previous chapter number (or 0 if first chapter)
- `{chapter_next}`: The next chapter number (or higher than max if last chapter)
- `{book_previous}`: The name of the previous book (or "null" if in first book)
- `{book_next}`: The name of the next book (or "null" if in last book)
- `{version}`: The bible translation version name
- `{source}`: The source/URL where the bible data came from
- `{book_chapters}`: The total number of chapters in this book
- `{old_new_testament}`: Either "old" or "new" (for the testament type)
- `{oude_nieuwe_testament}`: Dutch equivalent: either "oude" or "nieuwe"
- `{chapter_text}`: The formatted verses of this chapter

**Variations**: Use `chapter_first.md` for the first chapter of a book, `chapter_last.md` for the last chapter, `chapter_single.md` when a book has only one chapter, and `chapter.md` as the default for all other chapters. These variations are mostly usefull for if you want a pagenav at the top of the page.

#### Chapter List Template (`chapter_list.md`)
Used to format each chapter entry in a book's chapter list. Available variables:
- `{book}`: The name of the book
- `{chapter_number}`: The chapter number

#### Book List Template (`book_list.md`)
Used to format each book entry in the index's book list. Available variables:
- `{book}`: The name of the book
- `{book_chapters}`: The number of chapters in this book

#### Verse Template (`verse.md`)
Used to format each individual verse within a chapter. Available variables:
- `{verse}`: The text of the verse
- `{verse_number}`: The verse number within the chapter (e.g., 1, 2, 3)
- `{book}`: The name of the book (for context)