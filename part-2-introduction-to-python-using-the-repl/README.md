# Part 2 - Introduction to Python using The REPL

[REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop) stands for Read-eval-print-loop. It does what it sounds like it does. You type some input, evaluate it, and print the result. It's a great way to experiment with Python and quickly run some code.

When you execute the `python` command without specifying a script, you start python's REPL. You can exit the REPL by typing `exit()` or `quit()`.

Example:

```bash
    $ python
    Python 3.10.8 (main, Oct 15 2022, 10:48:54) [GCC 9.3.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> exit()
```

## An introduction to Python using the REPL

We will be more or less following the official [Python Tutorial](https://docs.python.org/3/tutorial/introduction.html) here.

To begin, start up the python REPL

```bash
    $ python
    Python 3.10.8 (main, Oct 15 2022, 10:48:54) [GCC 9.3.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
```

All the following code snippets assume you are running them within the REPL.

Python has an inbuilt function `print()` which prints the value of the argument passed to it.

```python
    >>> print('Hello World')
    Hello World
```

When writing a script, you might use this to print some output to the console. When using the REPL, evaluated expressions are printed automatically.

```python
    >>> 'Hello World'
    'Hello World'
```

### What is an expression?

An expression combines values, variables, operators, and calls to functions.

You can run some numerical expressions in the REPL:

```python
    >>> 1 + 1
    2
```

```python
    >>> 12 / 2
    6.0
```

```python
    >>> 1000 / (10 - 2*12) * 4
    -285.7142857142857
```

You can call some inbuilt functions to modify the output:

```python
    >>> int(12 / 2)
    6
```

## Numbers

Python has two types of numbers: integers and floating-point numbers. Integers are whole numbers, and floating point numbers have decimal points.

```python
    >>> 1
    1
    >>> 1.0
    1.0
```

You can use the `type()` function to find out what type a value is:

```python
    >>> type(1)
    <class 'int'>
    >>> type(1.0)
    <class 'float'>
```

Division always returns a floating point number:

```python
    >>> type(1 / 2)
    <class 'float'>
```

You can force the result to be an int with the following:

```python
    >>> type(int(1 / 2))
    <class 'int'>
```

Or using the `//` operator:

```python
    >>> 1 // 2
    0
    >>> type(1 // 2)
    <class 'int'>
```

### Some handy operators

```python
    >>> 8 ** 2  # 8 squared
    64
```

> Note: There's a comment in there. To open a comment in python use `#`. You can do this in a script and you can do this in the REPL. Comments will be ignored during evaluation.

```python
    >>> 8 ** 6  # 8 to the power of 6
    262144
```

```python
    >>> 8 % 2  # Modulo
    0
    >>> 8 % 3
    2
```

```python
    >>> round(1000 / (10 - 2*12) * 4)
    -286
```

See the [python numbers tutorial](https://docs.python.org/3/tutorial/introduction.html#numbers) for more information on python numbers.

## Strings

Python has a built-in class called [`str` for strings](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str). Strings are sequences of characters.

There are a number of ways to create strings in python. You can use single quotes, double quotes, or triple quotes.

```python
    >>> 'Hello World'
    'Hello World'
    >>> "Hello World"
    'Hello World'
    >>> """Hello World"""
    'Hello World'
```

Using single quotes `'` is probably the most common.

```python
    >>> 'With single quotes, you can use "double quotes" inside a string'
    'With single quotes, you can use "double quotes" inside a string'
    >>> 'Or you can use \'escape characters\' to use single quotes inside a string'
    "Or you can use 'escape characters' to use single quotes inside a string"
    >>> "Or you can use \"escape characters\" to use double quotes inside a string"
    'Or you can use "escape characters" to use double quotes inside a string'
```

You can use triple quotes `"""` to create multi-line strings.

```python
    >>> """This is a multi-line string.
    ... It can span multiple lines.
    ... """
    'This is a multi-line string.\nIt can span multiple lines.\n' # \n is a newline character
```

>Note: When using the REPL you can go on to a new line by pressing enter. If the expression you are writing has not been completed, the REPL will prompt you with `...` to indicate that you can continue on the next line.

We learned that strings are a sequence of characters. Python allows you to reference characters in a string directly.

```python
    >>> 'Hello World'[0]
    'H'

    >>> 'Hello World'[10]
    'd'
```

You can also check if a character is in a string.

```python
    >>> 'H' in 'Hello World'
    True
    >>> 'h' in 'Hello World'
    False
```

The str class has many practical methods. Some examples:

```python
    >>> 'h' in 'Hello World'.lower()
    True
    >>> 'Hello World'.replace('World', 'Cruel World')
    'Hello Cruel World'
    >>> '  Hello World  '.strip()
    'Hello World'
```

You can combine strings:

```python
    >>> 'Hello' + ' ' + 'World'
    'Hello World'
```

Get the length of a string:

```python
    >>> len('Hello World')
    11
```

You can insert values into a string using the format method:

```python
    >>> 'Hello {}'.format('World')
    'Hello World'
    >>> 'Hello {0}'.format('World')
    'Hello World'
    >>> 'Hello {0} {1}'.format('Cruel', 'World')
    'Hello Cruel World'
    >>> 'Hello {1} {0}'.format('World', 'Cruel')
    'Hello Cruel World'
    >>> 'Hello {adjective} {place}'.format(place='World', adjective='Cruel')
    'Hello Cruel World'
```

See the official python tutorial on [strings](https://docs.python.org/3/tutorial/introduction.html#strings) for more information.

## Functions

Functions in python, like most other programming languages, are a way to define a reusable block of executable code. Functions can take arguments and return a value.

```python
    >>> def hello_world():
    ...    return 'Hello World'
    ... 
    >>> hello_world()
    'Hello World
```

You begin the definition of a function with the `def` keyword.

The name of the function is followed by brackets `()`. Inside the brackets, you can define arguments. The arguments are separated by commas. e.g.

```python
    >>> def hello(adjective, place):
    ...   return 'Hello {} {}'.format(adjective, place)
    ... 
    >>> hello('Cruel', 'World')
    'Hello Cruel World'
```

The return statement is optional. If you don't use a return statement, the function will return `None`.

```python
    >>> def hello(place):
    ...   print('Hello {}'.format(place))
    ... 
    >>> hello('World')
    Hello World
    >>> hello('World') is None
    Hello World
    True
```

It's also possible to use something called a lambda function. Lambda functions are anonymous functions and can be run inline.

```python
    >>> (lambda place: 'Hello {}'.format(place))('World')     
    'Hello World'
```

## Variables

Variables are a way to make a named space for some object in python. We give it a name so that we can reference it later. In the previous section on functions, we gave a name to a reusable code block. Variables are similar in that you can reference them by their name later, but the name is a reference to an object and not something to execute.

Some examples:

```python
    >>> x = 1
    >>> x
    1
    >>> x = 'Hello World'
    >>> x
    'Hello World'
```

You can also assign multiple variables at once:

```python
    >>> x, y = 1, 2
    >>> x
    1
    >>> y
    2
```

You can also assign lambda functions to variables:

```python
    >>> hello = lambda place: 'Hello {}'.format(place)
    >>> hello('World')
    'Hello World'
```

As the name suggests, variables are... variable. You can change them after they have been assigned.

```python
    >>> x = 1
    >>> x
    1
    >>> x = 2
    >>> x
    2
```

You can even change the type of a variable.

```python
    >>> x = 1
    >>> x
    1
    >>> type(x)
    <class 'int'>
    >>> x = 'Hello World'
    >>> x
    'Hello World'
    >>> type(x)
    <class 'str'>

```

### A note on types

Python is a dynamically typed language. This means that you don't have to declare the type of a variable when you create it. The type of a variable is determined at runtime.

```python
    >>> x = 1
    >>> type(x)
    <class 'int'>
    >>> x = 'Hello World'
    >>> type(x)
    <class 'str'>
```

Recent versions of python do have a concept called [type hints](https://docs.python.org/3/library/typing.html). Type hints did not add or enforce types in python. Python already has types internally, but they are still dynamic in code. Type hints are just a way to add documentation to your code to help other developers understand what types you expect.

```python
    >>> def hello(place: str) -> str: # This adds helpful hints to your code and can be used by IDEs
    ...   return 'Hello {}'.format(place)
    ... 
    >>> hello('World')
    'Hello World'
    >>> hello(1)
    'Hello 1' # Despite using type hints, python doesn't care that we passed an int instead of a str
```

Type hinting is also helpful for IDEs using the type hints to provide better autocomplete and other features.

We will not look at type hints again in this tutorial, but you can read more about them in the official python tutorial on [type hints](https://docs.python.org/3/library/typing.html), and the use of type hints in production code is encouraged.

## Control Flow

There are several ways to control flow in python. Here we will get started by looking at if statements and for statements.

### If Statements

`if` statements are a way to execute code based on a condition. If the condition is `True`, the code block will be executed. If the condition is false, the code block will not be executed.

```python
    >>> if True:
    ...   print('Hello World')
    ... 
    Hello World
```

You can add a condition to execute when the `if` statement is false using `else`.

```python
    >>> if False:
    ...   print('Hello World')
    ... else:
    ...   print('Goodbye World')
    ... 
    Goodbye World
```

The `if` and `else` statements can be chained together using `elif`.

```python
    >>> if False:
    ...   print('Hello World')
    ... elif False:
    ...   print('Goodbye World')
    ... else:
    ...   print('Goodbye Cruel World')
    ... 
    Goodbye Cruel World
```

`if` and `elif` both take an expression that evaluates to a boolean. The expression can be anything that evaluates to a boolean. e.g.

```python
    >>> if 1 == 1:
    ...   print('Hello World')
    ... 
    Hello World
```

## Data Structures

Probably the most common data structures you will use in python are lists and dictionaries. Lists are a sequence of objects. Dictionaries are a collection of key-value pairs.

Other data structures we will briefly look at are tuples and sets.

Data structures are a large subject, and we are only skimming the surface here. You can read more about them in the official python tutorial on [data structures](https://docs.python.org/3/tutorial/datastructures.html).


TOOD

## Challenge

I will put a challenge here to use the REPL and write some python code to fetch data from and API and extract some information from it.
