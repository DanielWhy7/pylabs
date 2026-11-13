# Laboratory Work No. 2
# Web Scraping

- [Theory](#theory)
  - [csv](#csv)
  - [Creating custom iterators](#creating-custom-iterators)
  - [requests](#requests)
  - [BeautifulSoup](#beautifulsoup)
  - [Useful links](#useful-links)
- [Task](#task)
  - [General task](#general-task)
  - [Variants](#variants)

# Theory

## csv

To work with CSV files in Python, you can use the built-in `csv` module.

Example:

```py
import csv

# data to write
data = [
    ["Name", "Age", "City"],  # Headers
    ["Alexey", 30, "Moscow"],
    ["Maria", 25, "Saint Petersburg"],
    ["Ivan", 22, "Yekaterinburg"]
]

# write data to CSV file
with open('data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data) # write all rows

# append to file
with open('data.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Irina", 33, "Sochi"])
```

## Creating custom iterators

Iterators are objects that allow you to iterate over other objects, such as lists and tuples, without needing to access them by index. To create a custom iterator, you must implement two methods in a class: `__iter__()` and `__next__()`.

- `__iter__()` — returns the iterator instance. Usually, this is just self.
   
- `__next__()` — returns the next element of the sequence. If there are no more elements, it must raise a StopIteration exception to notify that the iteration is complete.

Example of creating a custom iterator:

```py
class SimpleIterator:
    def __init__(self, limit):
        self.limit = limit  # limit
        self.counter = 0  # counter

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.counter
        else:
            raise StopIteration

iterator = SimpleIterator(3)

for val in iterator:
    print(val)
```

Result:

```
1
2
3
```

## requests
**requests** is a Python library for handling HTTP requests. It provides a simple and convenient way to interact with web resources.

Installation:
```
pip install requests
```

**get** is the main HTTP method for retrieving data from a server. It is used when you need to:
- Download a web page
- Retrieve API data
- Download a file
- Perform a search

Example:
```py
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
response = requests.get("https://my-url.com", headers=headers)
if response.ok:
    print(response.content)
```

## BeautifulSoup

**BeautifulSoup** is a Python library for parsing HTML and XML documents. It creates a tree of objects from the parsed page, which allows for easy extraction and manipulation of data.

Installation:
```
pip install beautifulsoup4
```

Key features:
- Parsing "dirty" HTML — works even with incorrect markup
- Simple search — powerful methods for finding elements
- Tree navigation — moving between elements
- Document modification — adding, removing, and modifying tags

Example:
```py
from bs4 import BeautifulSoup
import requests

# Get the HTML page
url = "https://example.com"
response = requests.get(url)
html = response.text

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Extract the page title
title = soup.find('title')
print(f"Page title: {title.text}")

# Find all links
links = soup.find_all('a')
print(f"Links found: {len(links)}")

# Print the text of all links
for link in links:
    print(link.get_text(), link.get('href'))
```

## Useful links

- [csv (doc)](https://docs.python.org/3/library/csv.html)
- [Creating iterators](https://www.pythonforbeginners.com/basics/how-to-create-an-iterator-in-python)
- [requests (doc)](https://requests.readthedocs.io/en/latest/)
- [BeautifulSoup (doc)](https://beautiful-soup-4.readthedocs.io/en/latest/)

# Task
## General task

Variants 1-10: 
- Download at least 30 book cover images (hereinafter referred to as covers for brevity) for your variant using requests and BeautifulSoup from the website https://books.toscrape.com/. 

Variants 11-20:
- Download at least 30 audio files for your variant using requests and BeautifulSoup from the website https://sound-effects.ru/.

For all variants:
- Compile an annotation in the form of a CSV file containing the absolute and relative path to each file.
- Write an iterator over the file paths — use the annotation file or a folder path as a constructor parameter.

Variant-specific parameters, the path to the destination folder, and the path to the annotation file must be passed through command-line arguments.

## Variants

1. Write a program that downloads at least one book cover for each genre presented on the website. The user specifies the number of books per genre.
2. The user specifies one or more book genres. Write a program that downloads an equal number of covers for each specified genre.
3. Write a program that downloads book covers from random genres. The user specifies the number of genres.
4. The user specifies genres to be excluded from the download list. Write a program that downloads book covers from random genres, except those excluded by the user.
5. The user specifies the minimum book price. Write a program that downloads book covers with a price higher than the specified value.
6. Write a program that downloads book covers of the most expensive books on the website. The user specifies the number of books to download.
7. The user specifies the book rating. Write a program that downloads book covers with the specified rating.
8. The user specifies the minimum book rating. Write a program that downloads book covers with a rating not lower than the specified value.
9. The user specifies keywords for search (one or more). Write a program that downloads book covers with one of the keywords in the title.
10. The user specifies the minimum number of books in stock. Write a program that downloads book covers with a stock quantity not less than the specified value.


11. The user specifies one or more sound categories. Write a program that downloads an equal number of sounds for each specified category.
12. Write a program that downloads sounds from random categories. The user specifies the number of sounds.
13. The user specifies categories to be excluded from the download list. Write a program that downloads sounds from random categories, except those excluded.
14. The user specifies the minimum and maximum duration of the audio recording. Write a program that downloads sounds with a duration in the selected range.
15. The user specifies the minimum and maximum file size of the audio. Write a program that downloads sounds with a file size in the selected range.
16. Write a program that downloads the highest-rated sounds in their category. The user specifies the categories (one or more) and the number of sounds to download in each category.
17. Write a program that downloads the sounds with the lowest number of downloads in their category (one category - one sound). The user specifies the number of categories.
18. Write a program that downloads the highest-rated sounds on the website. The user specifies the number of sounds to download.
19. The user specifies keywords for search (one or more). Write a program that downloads sounds with one of the keywords in the title.
20. Write a program that downloads random sounds from the website. The user specifies the number of sounds.
