print("Welcome to Simple Calculator!")
print("Please select your choice:")

def main():
    x = get_user_choice()

    print("")
    print(f"You have chosen option {x}!")

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

def addition(a, b):
    n = a + b
    return n

def subtraction(a, b):
    n = a - b
    return n

def multiplication(a, b):
    n = a * b
    return n

def division(a, b):
    n = a / b
    return n

main()
