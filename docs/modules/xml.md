# XML

XML (eXtensible Markup Language) is a markup language for storing and transporting structured data. Python's `xml.dom.minidom` module provides a lightweight DOM (Document Object Model) interface for parsing and creating XML.

## XML Structure

An XML document consists of elements organised in a tree structure:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<catalogue>
    <book id="1">
        <title>Python Basics</title>
        <author>Alice Smith</author>
        <price>29.99</price>
    </book>
    <book id="2">
        <title>Data Science</title>
        <author>Bob Jones</author>
        <price>39.99</price>
    </book>
</catalogue>
```

Key concepts:

- **Element**: A node defined by opening and closing tags (e.g., `<title>...</title>`)
- **Attribute**: A name-value pair within an opening tag (e.g., `id="1"`)
- **Text content**: The data between opening and closing tags

## Reading XML

```python
from xml.dom.minidom import parse

# Parse an XML file
doc = parse("catalogue.xml")

# Get all book elements
books = doc.getElementsByTagName("book")

for book in books:
    # Get attribute value
    book_id = book.getAttribute("id")

    # Get text content of child elements
    title = book.getElementsByTagName("title")[0].firstChild.nodeValue
    author = book.getElementsByTagName("author")[0].firstChild.nodeValue
    price = book.getElementsByTagName("price")[0].firstChild.nodeValue

    print(f"ID: {book_id}, Title: {title}, Author: {author}, Price: {price}")
```

## Writing XML

```python
from xml.dom.minidom import parse

# Parse existing file
doc = parse("catalogue.xml")

# Modify an attribute
books = doc.getElementsByTagName("book")
books[0].setAttribute("id", "100")

# Modify text content
title_elem = books[0].getElementsByTagName("title")[0]
title_elem.firstChild.replaceWholeText("Advanced Python")

# Write back to file
with open("catalogue_modified.xml", "w", encoding="utf-8") as f:
    doc.writexml(f, indent="", addindent="    ", newl="\n", encoding="utf-8")
```

## Methods Reference

| Method | Description |
|--------|-------------|
| `doc.getElementsByTagName(name)` | Returns a list of all elements with the given tag name |
| `elem.getAttribute(name)` | Returns the value of an attribute |
| `elem.getAttributeNode(name)` | Returns the attribute node object |
| `elem.setAttribute(name, value)` | Sets or creates an attribute |
| `elem.firstChild.nodeValue` | Gets the text content of an element |
| `elem.firstChild.replaceWholeText(text)` | Replaces the text content |
| `elem.hasAttribute(name)` | Checks if an attribute exists |
| `elem.removeAttribute(name)` | Removes an attribute |

## Complete Example

```python
from xml.dom.minidom import parse

# Parse the file
doc = parse("catalogue.xml")

# Find all books
books = doc.getElementsByTagName("book")
print(f"Found {len(books)} books\n")

# Print each book's details
for book in books:
    book_id = book.getAttribute("id")
    title = book.getElementsByTagName("title")[0].firstChild.nodeValue
    author = book.getElementsByTagName("author")[0].firstChild.nodeValue
    price = float(book.getElementsByTagName("price")[0].firstChild.nodeValue)
    print(f"[{book_id}] {title} by {author} — ${price:.2f}")

# Find a specific book by attribute
for book in books:
    if book.getAttribute("id") == "2":
        title = book.getElementsByTagName("title")[0].firstChild.nodeValue
        print(f"\nBook with id=2: {title}")
```

!!! note "Alternative: ElementTree"
    For most use cases, `xml.etree.ElementTree` provides a simpler and more Pythonic API:
    ```python
    import xml.etree.ElementTree as ET

    tree = ET.parse("catalogue.xml")
    root = tree.getroot()

    for book in root.findall("book"):
        title = book.find("title").text
        print(title)
    ```
