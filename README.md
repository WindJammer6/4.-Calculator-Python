# Calculator-Python :fax: 
A simple Calculator in Python (Add, Subtract, Multiply, Divide of 2 numbers). Python libraries used: NIL

## Thoughts on starting this project
My fourth programming project, in Python.

Fairly simple project compared to the previous 2 projects.

![Semantic description of image](https://i.pinimg.com/736x/cb/75/33/cb7533438bf2c436fe0636b3b1d579ce.jpg)

<br>

Computer program used for coding: VS Code

## Code description
Let's start with:
1. Self-defined functions
2. Main code

<br>

<br>

**1. Self-defined functions**
```python
def get_user_choice():
    while True:
        try:
            n = int(input("0. Addition\n"
                "1. Subtraction\n"
                "2. Multiplication\n"
                "3. Division\n"
                "Choose the corresponding number: "))
            if n == 0 or n == 1 or n == 2 or n == 3:
                break
        except ValueError:
            print("Please enter a valid integer!")
        except:
            print("Please enter a number from 0 to 3!")
    return n
```
The 'get_user_choice()' function is to get user to choose a number 0 to 3, represented by what mathematical operator they want to use, as well as check
if the user did put in a number 0 to 3 and not something funny.

<br>

```python
def addition(a, b):
    n = a + b
    return n
```
Takes in 2 parameters/arguments, conatining 2 numbers user has given in the main code and adding them together.

Returns the result back to the main code.

<br>

```python
def subtraction(a, b):
    n = a - b
    return n
```
Takes in 2 parameters/arguments, conatining 2 numbers user has given in the main code and subtracting them.

Returns the result to back to the main code.

<br>

```python
def multiplication(a, b):
    n = a * b
    return n
```
Takes in 2 parameters/arguments, conatining 2 numbers user has given in the main code and multiplying them.

Returns the result to back to the main code.

<br>

```python
def division(a, b):
    n = a / b
    return 
```
Takes in 2 parameters/arguments, conatining 2 numbers user has given in the main code and dividing them.

Returns the result to back to the main code.

<br>

<br>

**2. Main code**
```python
def main():
    x = get_user_choice()

    print("")
    print(f"You have chosen option {x}!")
```
Gets the user's choice on which mathematical operator the user wants. Tells the user what the option he/she has chosen.

<br>

```python
    print("Please type in 2 numbers:")
    a = float(input("First number: "))
    b = float(input("Second number: "))

    if x == 0:
        c = addition(a, b)
        print(f"Answer: {c:.2f}")
    if x == 1:
        d = subtraction(a, b)
        print(f"Answer: {d:.2f}")
    if x == 2:
        e = multiplication(a, b)
        print(f"Answer: {e:.2f}")
    if x == 3:
        f = division(a , b)
        print(f"Answer: {f:.2f}")
```
Gets 2 numbers (can be a number of up to infinite deciaml points, basically what a float is) from the user that the user wants
to perform a mathematical operator on.

And based on the option for which mathematical operator the user has chosen, perform the corresponding action, and returns user the result. Gives result
up to 2 deciaml places to take in considerations for results with up to infinitely many decimal points.

<br>

<br>

## Output
```
Welcome to Simple Calculator!
Please select your choice:
0. Addition
1. Subtraction
2. Multiplication
3. Division
Choose the corresponding number: 3

You have chosen option 3!
Please type in 2 numbers:
First number: 4.58754
Second number: 2      
Answer: 2.29
```
(Addition, Subtraction and Multiplication has a different output)

## Thoughts after the project
The aim was for this project is to get familiar with mathematical-related commands in Python e.g. mathematical operators, decimals points, float, int.

Idea of the layout of this calculator taken from online, but code was made by me. I viewed the output, then try to make said output of the calculator
on my own.

<br>

To be improved:
* Like all code, more features can definitely be added e.g. with GUI such as tkinter, take in more than 2 numbers, however many numbers the user wants,
add other mathematical operations such as squaring (^2) or logarithms, trigonometry and mathematical symbols such as pi and e, brackets etc.

<br>

Have a gif:

![Semantic description of image](https://media.tenor.com/PFqmrAS7tTUAAAAd/cat.gif)
