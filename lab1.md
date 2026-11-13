# Laboratory Work No. 1
# Regular Expressions

- [Theory](#theory)
  - [Reading from a file](#reading-from-a-file)
  - [Command-line arguments](#command-line-arguments)
  - [Regular expressions](#regular-expressions-and-the-re-library)
  - [Useful links](#useful-links)
- [Task](#task)
  - [General task](#general-task)
  - [Variants](#variants)

# Theory

Below is the minimal theory that may be useful while completing the lab. For more detailed information, see the course lectures and the "useful links" section.

## Reading from a file

To read from a file, you need to open a file stream by calling the `open()` function:

```py
file = open("file_name.txt", "r")
```

`"file_name.txt"` — path to the file;

`"r"` — file reading mode (read);

`file` — file stream variable.

You can read information from the file using one of the following file stream methods:

- `readline()` — reads one line from the file

- `read()` — reads the entire contents of the file into a single string

- `readlines()` — reads all lines of the file into a list

After reading, the file stream must be closed using the `close()` method:

```py
file.close()
```

However, a more optimal approach is to use the `with` construct, which automatically closes the file stream:

```py
with open("my_file.txt", "r") as file:
    text = file.read()
```

## Command-line arguments

To pass arguments through the command line, the built-in `argparse` module is used:

```py
import argparse
```

Example of use:
```py
import argparse

parser = argparse.ArgumentParser()  # create the parser instance
parser.add_argument('name', type=str, help='your name')  # add a positional command-line argument
args = parser.parse_args()  # parse the arguments
print(f"Hello, {args.name}!")  # use the obtained argument value
```

`'name'` — argument name (required parameter)

`type` — argument data type (optional parameter)

`help` — help text for the argument (optional parameter)


Running the program:

```
python my_program.py Ivan
Hello, Ivan!
```

There can be any number of command-line arguments; they can be **positional (required)** and **optional**.
An optional argument is added as follows:
```py
parser.add_argument("-s", "--surname", type=str, help="your surname")
```

`"--surname"` — full argument name (required parameter)
`"-s"` — short name (optional parameter)

In the command line, to add an optional argument, you must specify either the full or the short name:

```
my_program.py Ivan -s Ivanov
```
or
```
my_program.py Ivan -surname Ivanov
```

Also, before using, you must check whether such an argument exists:

```py
if args.surname is not None:  # check whether a value exists
    print(f"Hello, {args.name} {args.surname}!")
else:
    print(f"Hello, {args.name}!")
```


## Regular expressions and the re library

Regular expressions in Python are used to search, process, and manipulate strings that match specified patterns.
Any string can be considered a regular expression pattern — in that case, a regular substring search will be performed. If we want to create a more complex pattern, we need to use special characters.

### Patterns matching a single character

- `.` — Any single character except a newline `\n`.
- `\d` — Any digit
- `\s` — Any whitespace character (space, tab, end of line, etc.)
- `\w` — Any letter (something that can be part of a word), as well as digits and `_`
- `[..]` — One of the characters in brackets,
or any character from the range `a-b`
- `[^..]` — Any character except the listed ones

### Quantifiers (specifying the number of repetitions)

- `{n}` — Exactly n repetitions
- `{m,n}` — From m to n repetitions inclusive
- `{m,}` — At least m repetitions
- `{,n}` — At most n repetitions
- `?` — Zero or one occurrence, synonym for {0,1}
- `*` — Zero or more, synonym for {0,}
- `+` — One or more, synonym for {1,}

### Functions of the re library

The `re` library in Python provides functions for working with regular expressions.

`re.search(pattern, string)` — Find in the string the first substring matching the pattern;

`re.fullmatch(pattern, string)` — Check whether the string matches the pattern;

`re.split(pattern, string, maxsplit=0)` — Analogous to str.split(), but splitting is done by substrings matching the pattern;

`re.findall(pattern, string)` — Find in the string all non-overlapping occurrences of the pattern;

`re.finditer(pattern, string)` — Iterator over all non-overlapping occurrences of the pattern in the string (returns match objects);

`re.sub(pattern, repl, string, count=0)` — Replace in the string all non-overlapping occurrences of the pattern with repl;

Example of searching by pattern:

```py
import re

text = "List of numbers: 123, 456, 789 and 123"  # search string
pattern = r'\d+'  # pattern
numbers = re.findall(number_pattern, text)
print(numbers)
```

Result:

```
['123', '456', '789', '123']
```

Example of splitting a string by pattern:

```py
import re

text = "one, two, three; four. five! six"  # search string

# Split the string by delimiters: semicolon, comma, period, exclamation mark, whitespace
parts = re.split(r'[;,.!\s]+', text)

print(parts)
```

Result:
```
['one', 'two', 'three', 'four', 'five', 'six']
```

## Useful links
- [Reading from a file (doc)](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [argparse (doc)](https://docs.python.org/3/library/argparse.html)
- [re (doc)](https://docs.python.org/3/library/re.html)


# Task
## General task

Open and read a file. The file name is entered through command-line arguments. Using regular expressions, complete the task according to your variant. Output the result to the screen.

The file `data.txt` contains a list of people's profiles with the following structure:

- Surname
- First name
- Sex
- Date of birth
- Phone number or email
- City

Valid formats for each item:

1. Surname and first name:
   - Start with an uppercase letter
2. Sex:
   - М, м, Мужской, мужской, Ж, ж, Женский, женский
3. Date of birth:
   - Formats:
      - 01/01/2000
      - 01-01-2000
      - 01.01.2000
      - 1/1/2000
      - 1-1-2000
      - 1.1.2000
   - There must be a correct range of days and months, year — from 1900 to the current year.
4. Phone number or email:
   - Phone number:
      - 11 digits
      - Starts with 8 or +7
      - Format:
         - 8 (012) 345-67-89
         - 80123456789
         - 8 012 345-67-89
         - 8 (012) 345 67 89
         - 8 012 345 67 89
   - email:
     - Domains: gmail.com, mail.ru, yandex.ru
     - Local part (name):
        - Letters (A-Z, a-z)
        - Digits (0-9)
        - Symbols: . _ % + -
        - Length: up to 64 characters
5. City:
   - Format: Москва, г. Москва

## Variants

1. Count the number of male profiles in the list. Print their count to the screen and save the profiles to a new file.
2. Count the number of people born in the 21st century. Print their count to the screen and save the profiles to a new file.
3. Count the number of people aged 30 to 40. Print their count to the screen and save the profiles to a new file.
4. Find the oldest and the youngest person. Print their age and profiles to the screen.
5. Find all people with the surname Иванов(а). Print their count to the screen and save the profiles to a new file.
6. Find all people with surnames ending in "ов(а)". Print their count to the screen and save the profiles to a new file.
7. Find all people whose phone numbers have the city code 927. Print their count to the screen and save their profiles to a new file.
8. Find all people living in the city of Москва. Print their count to the screen and save their profiles to a new file.
9. Count which first name occurs most frequently. Print the name and the number of repetitions to the screen.
10. Find all female names starting with the letter А. Print their count to the screen and save the profiles to a new file.
11. The user enters a person's name through command-line arguments. Count the number of people with that name. Print the count to the screen and save the profiles to a new file.
12. Determine which operator code occurs most frequently among the phone numbers. Print the code and the number of its repetitions to the screen.
13. Find profiles of people who have a phone number (in a correct format). Print their count to the screen and save the found profiles to a new file.
14. Find profiles of people who have an email (in a correct format). Print their count to the screen and save the found profiles to a new file.
15. Verify that phone numbers are unique. Print the profiles with duplicates to the screen.
16. Verify that email addresses are unique. Print the profiles with duplicates to the screen.
17. Verify that all first names and surnames start with an uppercase letter. If a first name or surname starts with a lowercase letter — fix it and save the result to a new file.
18. Find phone numbers with an incorrect format. Print the found profiles to the screen. Delete the found profiles and save the result to a new file.
19. Find email addresses with an incorrect format. Print the found profiles to the screen. Delete the found profiles and save the result to a new file.
20. Find dates of birth with an incorrect format. Print the found profiles to the screen. Delete the found profiles and save the result to a new file.
21. Compose a list of surnames and first names in the format "Surname I.". Sort the resulting list in alphabetical order and save it to a new file. All first names and surnames must be in a correct format.
22. Create a list in the format "Surname: phone number" and save it to a new file. All numbers must be in a correct format.
23. Create a list in the format "Surname: email address" and save it to a new file. All addresses must be in a correct format.
24. Create a list in the format "Surname: date of birth". Sort it by age and save it to a new file. All dates of birth must be in a correct format.
25. Sort the original list by surnames and first names in alphabetical order and save the result to a new file (the structure of the list is unchanged).
26. Bring all data to a single template (any of the allowed ones). Save the result to a new file. If the data is incorrect — put a dash.
27. Calculate statistics by email domains: create a list in the format "Domain: count", sort it by the number of people and save it to a new file.
28. Calculate statistics by cities: count the number of people from each city, create a list in the format "City: count", sort it by the number of people and alphabetical order and save it to a new file.
29. Calculate statistics by age: create two lists — for men and women, in the format "Range — count" and save it to a new file. Ranges for men: 0-17, 18-64, 65+, for women: 0-17, 18-59, 60+.
30. Save the data as a table in CSV format. The table must contain the columns: Surname, First name, Sex, Date of birth, Phone number (dash if absent), Email (dash if absent), City. If the data in a column is incorrect — put a dash.
