# Custom Book Guide

This guide explains how to structure and add custom books to the bibleConvertor tool. While this tool was originally designed for converting Bible translations, it can also be used for other multi-chapter, verse-based texts or even non-traditional books.

## Overview

To add a custom book, you need to:
1. Create a JSON file for each book/text with the proper structure
2. Create or update an `index.json` file that references all your books
3. Place these files in the `bible/` folder

## Index Structure

The `index.json` file serves as the main configuration for all books in your collection. Here's what you need:

### Required Fields

```json
{
  "version": "Your Collection Name",
  "source": "https://example.com",
  "old_testament_amount": 0,
  "books": [
    {
      "name": "Book Name",
      "filename": "BOOK.json",
      "chapters": 5
    }
  ]
}
```

### Field Descriptions

- **`version`** (string): The name of your collection (e.g., "My Custom Bible", "My Book Series", "Reformed Bible")
- **`source`** (string): The URL or source where the original content came from (e.g., "bibleapi.com" or "https://mybooksite.com"). This will be automatically converted to include `https://` if missing.
- **`old_testament_amount`** (number): The number of books to consider as "part one". This is used for the `{old_new_testament}` and `{oude_nieuwe_testament}` template variables. For non-traditional books, you can set this to any number (e.g., the total number of books if you don't want a distinction, or 0 to have all books be "new").
- **`books`** (array): An array of book objects, each containing:
  - **`name`** (string): The display name of the book (e.g., "Genesis", "Chapter One")
  - **`filename`** (string): The JSON filename for this book (e.g., "GEN.json")
  - **`chapters`** (number): The total number of chapters in this book

### Example index.json

```json
{
  "version": "My Custom Collection",
  "source": "https://example.com/mybookdata",
  "old_testament_amount": 2,
  "books": [
    {
      "name": "Book One",
      "filename": "BOOK1.json",
      "chapters": 3
    },
    {
      "name": "Book Two",
      "filename": "BOOK2.json",
      "chapters": 5
    },
    {
      "name": "Book Three",
      "filename": "BOOK3.json",
      "chapters": 2
    }
  ]
}
```

## Book File Structure

Each book referenced in `index.json` needs a corresponding JSON file. The file structure is as follows:

### Required Fields

```json
{
  "book": "Book Name",
  "version": "Your Collection Name",
  "source": "https://example.com",
  "chapters": {
    "1": [
      {
        "verse": 1,
        "text": "The content of verse 1..."
      },
      {
        "verse": 2,
        "text": "The content of verse 2..."
      }
    ],
    "2": [
      {
        "verse": 1,
        "text": "The content of chapter 2, verse 1..."
      }
    ]
  }
}
```

### Field Descriptions

- **`book`** (string): The name of the book (must match the `name` field in `index.json`)
- **`version`** (string): The collection name (should match the `version` in `index.json`)
- **`source`** (string): The source URL (should match the `source` in `index.json`)
- **`chapters`** (object): An object where:
  - Keys are chapter numbers as strings (e.g., "1", "2", "3")
  - Values are arrays of verse objects, each containing:
    - **`verse`** (number): The verse number within the chapter
    - **`text`** (string): The actual content of the verse

### Example Book File (BOOK1.json)

```json
{
  "book": "Book One",
  "version": "My Custom Collection",
  "source": "https://example.com/mybookdata",
  "chapters": {
    "1": [
      {
        "verse": 1,
        "text": "Chapter one begins with this introductory verse."
      },
      {
        "verse": 2,
        "text": "Here is the second verse of the first chapter."
      },
      {
        "verse": 3,
        "text": "And here is the third verse."
      }
    ],
    "2": [
      {
        "verse": 1,
        "text": "This is chapter two, and the first verse starts here."
      }
    ],
    "3": [
      {
        "verse": 1,
        "text": "The final chapter of Book One delivers this message."
      }
    ]
  }
}
```

## Special Cases

### Books Without Verses

If your custom book doesn't use a traditional verse structure (e.g., it's a narrative novel or article-based), **you must still create at least one "verse" entry** in each chapter. This ensures the tool can process the content correctly.

**Example:** A single-chapter book with no verses

```json
{
  "book": "My Story",
  "version": "My Custom Collection",
  "source": "https://example.com/mystory",
  "chapters": {
    "1": [
      {
        "verse": 1,
        "text": "The entire content of this chapter goes here as a single verse. The tool requires at least one verse entry per chapter."
      }
    ]
  }
}
```

### Non-Bible Books

If you're using this tool for content that isn't Bible-related, you may want to hide the Old Testament/New Testament distinction. Here's how:

1. In your `index.json`, set `old_testament_amount` to 0 (or any value that makes sense for your content)
2. Remove the `{old_new_testament}` and `{oude_nieuwe_testament}` template variables from your template files

This is already explained in more detail in the main README.md under the Customization section.

## File Naming Convention

While there's no strict requirement for how you name your JSON files, we recommend using short, uppercase codes (e.g., `BOOK.json`, `CH01.json`). The tool uses the `filename` field in `index.json` to locate these files, so be consistent and accurate.

## Complete Workflow Example

Here's a complete example of adding a 2-book custom collection:

### Directory Structure
```
bible/
├── index.json
├── STORY1.json
└── STORY2.json
```

### bible/index.json
```json
{
  "version": "My Novel Series",
  "source": "https://mywebsite.com/novels",
  "old_testament_amount": 1,
  "books": [
    {
      "name": "Part One: The Beginning",
      "filename": "STORY1.json",
      "chapters": 2
    },
    {
      "name": "Part Two: The Conclusion",
      "filename": "STORY2.json",
      "chapters": 1
    }
  ]
}
```

### bible/STORY1.json
```json
{
  "book": "Part One: The Beginning",
  "version": "My Novel Series",
  "source": "https://mywebsite.com/novels",
  "chapters": {
    "1": [
      {
        "verse": 1,
        "text": "This is the opening scene of my novel..."
      }
    ],
    "2": [
      {
        "verse": 1,
        "text": "The story continues in chapter two..."
      }
    ]
  }
}
```

### bible/STORY2.json
```json
{
  "book": "Part Two: The Conclusion",
  "version": "My Novel Series",
  "source": "https://mywebsite.com/novels",
  "chapters": {
    "1": [
      {
        "verse": 1,
        "text": "The final chapter wraps everything up..."
      }
    ]
  }
}
```

After setting up these files, run the converter to generate your Obsidian vault!

## Troubleshooting

- **Missing files**: Ensure every book referenced in `index.json` has a corresponding JSON file in the `bible/` folder
- **Chapter count mismatch**: The `chapters` number in `index.json` must match the number of chapter entries in your book JSON file
- **Empty chapters**: Every chapter must have at least one verse entry
- **Template variables**: If using custom books, remember to update your templates (remove `{old_new_testament}` if not needed)

## Questions or Issues?

Refer back to the main README.md for information on customizing templates and template variables.
