# Summary

How to Run
Wait, how do you actually run Python code?

Before we build anything, we should learn some basic concepts about Python. A good place 
to start would be figuring out how to run, or execute, code. There are two primary ways we 
can run code: line by line or in self-contained scripts called modules. Sometimes, executing 
lines is sufficient for answering a quick and simple question (much like a SQL query). Other 
times, the problem at hand is simply too complex to manage with line-by-line executions. Such 
problems can be broken down into modules, denoted by the .py file extension. Indeed, the ability 
to abstract components of a broader problem is what makes programming so powerful.

If you followed Part 1, then you should have what's called the Python Interpreter pinned to the 
bottom of the PyCharm window. We can enter commands here line by line. For example, we could do 
some quick math and get its ouput right away. We can also create variables that store a value 
at the command-line as well. We are also able to call functions. Overall, this is a very simple 
way of executing single lines of code with an immediate response.

![python download image](../../setup/Python Setup/website/assets/basics/pythonInterpreter.png)

For something more involved, we might consider creating a Python file that can be run all at once. 
Take for example a module called hello.py. This code will prompt the user for their name and greets 
them accordingly. To run this simple program, you can press the green arrow at the top right corner 
of the PyCharm window. You can also right click anywhere on the script and select Run 'hello'. To 
create a new file, use this hotkey: Alt + Insert + Enter or by right clicking on the Project folder 
in the explorer.

```
# This is a file called: hello.py (# denotes comments)

# Store the user input in a viarable
user_input = input("Please type your name: ")  

# Return a formatted string of text characters
print("Hello, {}!".format(user_input))
```
              
There is a third, hybrid approach that really only applies to the PyCharm IDE. It allows the developer to 
run a chunck of code within a module. PyCharm calls this trick "Execute Selection in Console". Simply highlight 
the desired code and then use the hotkey: Alt + Shift + E or right click and select Execute Selection in Console. 
This is similar to how we tend to run code in SQL Studio. Pro-tip: re-map the "Execute Selection in Console" 
hotkey to Alt + X as to match the hotkey in SQL Studio (look under Settings -> Keymap). While running blocks of 
code is both fast and familiar, writing self-contained modules is best practise as problem grow in scope and 
complexity.

# Python Semantics

This is a language, afterall

One of the most important aspects of writing Python is that indentation matters. There are several programming 
constructs that will be introduced that depend on it. The scope of code is also defined by indentation. That 
is to say, pay attention to where an indent is included because it is likely that the code will not behave as 
expected or not run at all without the correct aligntment. Indentations are generally four whitespaces, but the 
tab usually works the same.

```python
# GOOD
x = 5
if x > 0:
  print('x is positive')
else:
  print('x is negative')
```          
                          
```python
# BROKEN
x = 5
if x > 0:
print('x is positive')
else:
print('x is negative')
```

Variable assignment is very easy in Python. If you have ever declared a variable in SQL, you had to define its 
data type before assigning its value. Many languages are like this but Python tries to infer the data type for 
you. As such, you simply write the name of the variable followed by an equals sign and the value to be assigned.

Operators are a fundamental part of any programming language as well. While the typical operators like +, -, *, 
/ work as expected, below are a few other operators available:

```python
x = 5
# Arithmetic Operators
x // 2  # returns 2 Floor Division - Remove the remainder
x % 2  # returns 1 Modulus - Remainder of a division
x ** 2  # returns 25 Exponentiation - Raise x to the power of n
-x  # returns -5 Negation - Return the negative of x

# Comparison and Boolean Operators
x == 5  # return True
x > 0  # returns True
x < 0  # returns False
(x > 0) or (x < 0)  # returns True
(x > 0) and (x < 0)  # returns False
not (x < 10)  # returns False
```

# Data Types and Structures
The building blocks of doing anything useful

Most of the data types you may be used to seeing in SQL or Excel are also available in Python. Data types like 
Integers (int), Floats (float32), Varchars/Strings/Text (str), and Booleans (bool) are all basic data types in 
Python. On top of these, there are what are known as data structures. These are essentially containers for the 
aforementioned data types. The most prevalent of these is the list. It is denoted by square brackets wherein 
each element is seperated by a comma. There are many things that we can do with lists as follow:

```python
x = [1, 2, 3]
len(x)  # Returns the Length of a list, in this case, 3
x.append(4)  # Adds a new element to the same list
x.extend([5, 6, 7])  # Adds each element of another list to the target list
x.sort(reverse=True)  # Sorts the list in reverse order
```

An important concept to understand when using data structures like a list is indexing. It is the ability to 
access any element of an array by its position. So if I want to do something with the first element, I can 
access it by its index likeso: my_list[0]. The important thing here is that Python is zero-indexed, meaning 
the language starts counting at 0, not 1! Therefore, the second element is at index, or position, 1 as such: 
my_list[1]. Also, the colon operator allows us to pull ranges within the list, referred to as slicing. We can 
also assign values to specific indexes. This would look something like this: x[0] = 100.

```python
x[0:3]  # Returns [1, 2, 3]
x[:3]  # Shorthand for the same result
x[-1]  # Returns the last element, 7
x[:-3]  # Return the last 3 elements as a list
x[2:4]  # Return a subset from the middle of the list
x[::-1]  # This special syntax will reverse the list
```            
          
Another useful data structure is called a dictionary. It is essentially a mapping between a named key and 
its value. The concept of a dictionary is the basis for an extremely versatile and popular data processing 
and analysis package called pandas. Unlike a list, a Python dictionary is denoted with curly braces and each 
element is comprised of a key:value pair. Below is an example that represents some table wherein each field 
is a key that maps to an array of values.

```python
datatable = {
    'col1': [10, 2, 30, 5],
    'col2': ['NJ', 'DC', 'VA', 'CA'],
    'col3': [600, 50, 100, 750]
}
```           

# Conditional Logic
If and only if this is true, do something

These are statements that require a condition to be met for a certain block of code to be executed. The most 
basic conditional statement is the if statement; it checks if a condition is true (i.e. x == 20), then the 
following indented line or lines are executed. If the condition is not true, the indented lines are skipped 
and the next non-indented line is run.

You may choose to include the optional else and elif statements along with the if statement. An else statement 
designates a block of code to be run when the condition in the if statement isn’t met. Elif statements work the 
same way as if statements, but are placed in between the if and else statements to test for multiple conditions 
before resorting to the else block of code.

```python
x = 20

if x > 0:
    print("x is positive")
else:
    print("x is negative")
```
         
```python                
x = 20

if x > 0:
    print("x is positive")
elif X < 0:
    print("x is negative")
else:
    print("x is zero")
```

# Iteration
Repeat code again, and again, and again...

Many programming problems tend to require repetitive actions. Rather than writing the same commands over and 
over again, programming languages have the ability to perform iterative processes. These contructs are called 
Loops and they come in different flavors. In Python, it is sufficient to understand the For Loop and While Loop. 
The first will repeat a set of executions for n number of iterations. The latter construct will instead perform 
a set of executions for as long as some condition is true.

Consider an example where we have a list of names. We would like our program to simply greet each person. The 
novice solution would simply repeat the code for each and every name in the list. Instead, we can just tell 
Python, for each name in this container, execute the following code:

```python            
# Good Solution
names = ['Holly', 'Wayne', 'Peter']
for name in names:
    print('Hello, ', name)
```

```python
# Bad Solution
names = ['Holly', 'Wayne', 'Peter']
print('Hello, ', names[0])
print('Hello, ', names[1])
print('Hello, ', names[2])
```

While three elements in a list is trivial, imagine if there were 100 or 1,000 or 1,000,000 names, files, 
rows, or anything where you had to repeat some set of actions! Throwing conditional logic into the mix is 
also a powerful concept. We can do so using a While Loop. Here, we are telling Python that so long as some 
condition is valid, repeat some set of actions. Let's say we want to prompt the user for an input value. It 
must be an integer, so as long as the user inputs a non-integer we will continue prompting them again.

```python
while True:
    try:
        user_input = int(input("Give me a whole number: "))
    except ValueError:
        print("Sorry, that's not a number!")
        continue
    else:
        break
print("Was your number: ", user_input, "?")
```

Although it seems like a lot is going on, this block of code is simply asking for a number. It checks if 
it is indeed a number. If not, it prompts the user again. Otherwise, it moves on. Notice the semantics of 
the code. Python will try to coerce the input into an integer data type. If doing so is not possible because 
the user input something other than a number, it raises a ValueError and will continue to prompt the user again. 
Once the user inputs a number, the code will break, or exit, from the loop.

# File Input-Output
Reading and writing with Python

Reading the contents of files into Python is extremely common. Likewise, writing Python objects out to files is 
also common. The Python language has several built-in primitives for file input-ouput. That said, it is also very 
common to use third-party packages to do similar tasks as well. That said, the concepts here will translate to 
those applications.

Let's pretend that there is a pipe-delimited text file in the same directory as your Python file. As such, we 
would like to store its contents in memory and peform some preprocessing and analysis on it. The general paradigm 
for accessing these contents is by using the with open(filepath, 'r') as f construct. This tells Python to open 
the file at a given location and enter "read" mode. We assign an alias, f, for easy reference. Within the scope 
of this block, we can proceed to read in the text data line by line, splitting each row by the known delimiter.

```python
fpath = "path/to/file.txt"
data = []
with open(fpath, 'r') as f:
    for row in f:
        data.append(row.split(r'\t'))
```
            
          
Likewise, we may have some data that was processed or analyzed in Python and we would like to persist this 
object to memory; that is, we want to save it so when Python closes, we do not lose this information. We can 
use a very similar construct, excpet we feed the open() function a path to a file we want to create and enter 
"write" mode. Note, this will overwrite the file in this path. to avoid that, you can also enter "append" mode 
(denoted by 'a').

```python
fpath = "path/to/new_file.txt"
data = ['some', 'data', 'to', 'write']
with open(fpath, 'w') as f:
    for row in data:
        f.write(row + '\n')
```
            
          
Notice we are iterating over the data we want to write whereas before we were iterating over the file object 
itself. Furthermore, we explicitely need to concatenate the end-of-line token, in this case a newline-feed 
(denoted as '\n'). If writing data like this, it is also a good idea to make sure each row is a string data 
type, otherwise this concatenation will fail. In the next section, you will see a trick for adding in delimiters 
as well. Note, however, there are many third party packages that abstract these low-level implementation details 
when working with standard data formats suchas csv or JSON. When that is not the case, however, knowing how to 
read and write raw data at a lower level is valuable.


# String Manipulation
How do we deal with text?

Dealing with text is a very common task in any programming language. A lot of data, for example, will be stored 
as text and knowing how to extract information from it is very powerful. This falls under a much larger topic 
called Regular Expressions but even knowing its basics can prove useful in many workflows. In fact, Python 
contains several high level wrappers for processing and parsing text information.

We can split text based on some matching character. Consider the example below. We have a sentence which is 
considered a single data type. We can treat it as a list of individual characters, including special characters 
like whitespaces and line seperators. We could also parse out the sentences contained therein based on punctuation. 
Given those sentences, we can parse out some words and build a vocabulary of unique words using the set() data 
structure. This is all very useful for learning some statistics of text-based data.

```python
text = "This is an example of string data in Python. This is another sentence."
print(len(text))  # Strings are just arrays of characters

text = text.lower()  # Make all letters lowercase. Use the .toupper() method for uppercase
print(text)

sentences = text.split('. ')  # How many sentences were parsed?
print(sentences)

words = []
for sentence in sentences:
    words.extend(sentence.split(' '))  # Add each word to a list
vocab = set(words)  # Creating a vocabulary of words from our sentences
print(len(vocab))
```

Maybe we need to clean up some text data. In this case, we can use methods such as .strip() method to remove 
all leading and trailing whitespaces. The .replace() method is useful for normalizing text data. Let's say 
some of the data has a bunch of phone numbers in different formats. We could use this method and several others 
to standardize the data into a consistent format. Notice how we can chain several methods and indexers in a single 
line of code. We also take advantage of list concatenation to append substrings together.

```python
raw_phone_numbers = [
    '111-234-4896    ',
    '  222.333-4456',
    '333 999.9999 '
]

# Desired Format: (###) ###-####

clean_phone_numbers = []
for nmbr in raw_phone_numbers:
    area_code = nmbr.strip()[:3]  # First 3 characters (no leading whitespace)
    number = nmbr.strip()[-8:].replace('.', '-')  # Last 8 characters (no trailing whitespace)
    clean_phone_numbers.append('(' + area_code + ') ' + number)
print(clean_phone_numbers)
```

# Modules and Packages
When base Python just isn't enough

Python was designed to be "batteries included" meaning it has a lot of built-in functionality. Likewise, there is a plethora of third-party software packages freely available and open-source that can also be leveraged if installed. Most of this additional functionality has to be referenced explicitely with what is called an import statement. Take for example the Python Data Analysis Library, or Pandas. If installed in your Python environment, you need to access it as such: import pandas as pd.

After this line, you have access to all of its functionality. Note, the as statement aliases the package name such that you can simply use pd to access its contents rather than writing out the entire package name. Sometimes you only want a specific module or function from a package. We can tell Python to reference it as such: from pckgname import module.

```python
# Top of your script
import os  # Import the os module
import pandas as pd  # Import the Pandas library

from datetime.datetime import today()   # Import the today() function from the datetime module
                                        # contained in the datetime package
            
``` 

# Functions and Abstraction
Programmer are lazy, so don't repeat yourself

Functions are a useful way to create blocks of code that can be easily reused throughout your scripts. One of 
the most common methods to define a function is using a def statement. This statement names the function and 
lists the inputs needed in parentheses, and the block of code the function will execute is indented beneath. 
To call a function, simply list the function's arguments, or inputs, in parentheses after the name of the 
function. Keep in mind that the arguments must be entered in the same order they appear in the def statement. 
Arguments can also be assigned default values in the function's def statement. These values will be used 
automatically if no arguments are entered when the function is called but give the user the flexibility to 
input different values if necessary.

When writing functions, the goal is to abstract some process such that it only needs to be implemented once 
but reused indefinitely. Some thought and effort should therefore be put into designing function definitions. 
A one-off, ad-hoc piece of code may not require abstraction, but what about a process that is executed multiple 
times with slight variations? In the latter case, one could factor out the common logic into a function. Those 
variations in the process would become the function arguments.

**Example 1**
```python
def square(x):
    return x * x

# Call square().
square(2)
```

**Example 2**
```python
def exponentiate(x, power=2):
    return x ** power

# Call exponentiate().
exponentiate(2, power=3)
```

**Example 3**
```python
def scale(x, scale_by=3):
    return x * scale_by

# Call scale().
scale(2, scale_by=10)
```


