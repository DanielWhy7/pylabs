# Rules for Completing Laboratory Work

This guide describes the basic rules for completing laboratory work. All examples are exaggerated and are used to clearly demonstrate the rules.

Basic rules:
1. Follow PEP8.
2. All code must be formatted as functions and classes.
3. Use type-hinting (specifying data types in functions and classes).
4. Write docstrings (function descriptions).
5. Separate the program into individual modules.
6. Call functions inside the condition `if __name__ == '__main__'`
7. Use the exception handling mechanism (mandatory after the corresponding lecture).

These rules are broken down with examples below.

## 1. Functions

Code must be formatted as functions. Each function must perform a single task. Global code is unacceptable, except for constants.

Let's look at an example of a program that adds two numbers:
```py
a = int(input())
b = int(input())
c = a + b
print(c)
```

It consists only of global code. Let's write the correct version using functions:
```py
def enter_number():
    return int(input())

def sum(a, b):
    return a + b

def main():
    a = enter_number()
    b = enter_number()
    c = sum(a, b)
    print(c)
```
Each function here performs its own task:
`enter_number()` - gets a number and converts it to int, `sum()` - adds two values, `main()` - combines all functions into a program.


## 2. Type-hinting

The lack of explicit data types can lead to errors. To avoid such problems, it is better to use type hints.

```py
def sum(a: int, b: int) -> int:
    return a + b
```

`a: int` - data type of the function argument

`-> int` - data type of the return value

If the function returns nothing, it is better to specify `None` as the return type:

```py
def print_hello(name: str) -> None:
    print(f"Hello, {name}!")
```

If the argument is a container containing a single data type, this can also be explicitly specified in the hints:

```py
def sum(numbers: list[int]) -> int:
    res = 0
    for num in numbers:
        res += num
    return res
```

`list` - container type, `int` - type of the container's contents.

If there are multiple acceptable types for an argument, use `|`:

```py
def sum(a: int | float, b: int | float) -> int | float:
    return a + b
```

## 3. Docstring

A docstring is documentation inside the code. It is especially useful when multiple people are working with the code (or when your code is being checked by a teacher...)

Example of a docstring for simple functions:

```py
def sum(a: int, b: int) -> int:
    """
    Sum of a and b.
    """
    return a + b
```

Example of a docstring for more complex functions:
```py
def sum(a: int, b: int) -> int:
    """
    Sum of numbers.
    :param a: first term
    :param b: second term
    :return: sum
    """
    return a + b
```
In the second case, we explicitly write out each parameter and the return value. 


## 4. Program Start

When a module is imported, all of its global code is executed. Suppose we have a module `my_sum.py` containing the following code:
```py
def sum(a: int, b: int) -> int:
    """
    Sum of a and b.
    """
    return a + b

print(sum(1, 2))
```

`print(sum(1, 2))` is global code.
Let's import this module into another file:

```py
import my_sum

print(my_sum.sum(3, 4))
```
When run, instead of one result, two will be printed at once - from the imported file and from the running one:

```
3
7
```

To avoid such a situation, one should use the construct `if __name__ == '__main__'`:

```py
def sum(a: int, b: int) -> int:
    """
    Sum of a and b.
    """
    return a + b


if __name__ == "__main__":
    print(sum(1, 2))
```

Now the code `print(sum(1, 2))` will only execute if we run the file `my_sum.py`; if this file is imported, the code will not be executed. However, do not forget that the code written after `if __name__ == '__main__'` is still global code, so it is undesirable to write too much in it. Ideally, you should create a separate `main()` function and call only it:

```py
if __name__ == "__main__":
    main()
```


## 5. Exception Handling

Even if your code is absolutely correct, errors can occur when working with data whose format is unknown in advance:

```py
a = int(input("Enter number: "))
```

```
Enter number: some string

ValueError: invalid literal for int() with base 10: 'some string'
```

In this example, we entered a string instead of the expected number and got a `ValueError` exception.
To prevent such situations, use the exception handling mechanism:

```py
a = input("Enter number: ")
try:
    a = int(a)
except:
    print("Error!")
```
```
Enter number: some string
Error!
```

If you know what type of exception to expect, explicitly write it in the `except` block - this will give the user more information about the error:
```py
a = input("Enter number: ")
try:
    a = int(a)
except ValueError as exc:
    print(f"Error: {exc}")
```

```
Enter number: some string
Error: invalid literal for int() with base 10: 'some string'
```

If you want to throw an exception yourself, use the `raise` keyword:

```py
if not a.isdigit():
    raise ValueError("Value is not integer number")
```
```
Enter number: some string
Error: Value is not integer number
```

## Conclusion

So, let's look at the code we had at the beginning:

```py
a = int(input())
b = int(input())
c = a + b
print(c)
```

And apply all the rules discussed above to it:

```py
def enter_number() -> int:
    """
    Entering a number from the console.
    """
    num = input()
    if not num.isdigit():
        raise ValueError("Value is not integer number")
    return int(num)

def sum(a: int, b: int) -> int:
    """
    Sum of a and b.
    """
    return a + b

def main():
    try:
        a = enter_number()
        b = enter_number()
        c = sum(a, b)
        print(c)
    except ValueError as exc:
        print(f"Error: {exc}")
    
if __name__ == "__main__":
    main()
```

As a result, we got ~~disgustingly long~~ correct code that will be understandable to your colleagues (and the teacher) and will not cause errors.
