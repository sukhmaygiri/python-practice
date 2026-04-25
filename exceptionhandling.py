1) Check valid integer input
try:
    n = int(input("Enter an integer: "))
    print("You entered:", n)
except ValueError:
    print("Invalid input! Not an integer.")
🔶 2) Square root with negative check
import math

try:
    n = int(input("Enter number: "))
    print("Square root:", math.sqrt(n))
except ValueError:
    print("Cannot find square root of negative number!")
🔶 3) Handle KeyboardInterrupt (Ctrl+C)
import math

try:
    r = float(input("Enter radius: "))
    area = math.pi * r * r
    print("Area:", area)
except KeyboardInterrupt:
    print("\nInput cancelled by user!")
🔶 4) Division with try-except-else-finally
def division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    else:
        print("Result:", result)
    finally:
        print("Execution completed")

a = int(input("Enter a: "))
b = int(input("Enter b: "))
division(a, b)
🔶 5) Custom Exception (InvalidAge)
class InvalidAge(Exception):
    pass

try:
    age = int(input("Enter age: "))
    
    if age < 18:
        raise InvalidAge("Too young for job")
    elif age > 60:
        raise InvalidAge("Too old for job")
    else:
        print("Selected for job")
        
except InvalidAge as e:
    print(e)
🔶 6) Factorial with negative check
import math

try:
    n = int(input("Enter number: "))
    if n < 0:
        raise ValueError("Negative number not allowed")
    print("Factorial:", math.factorial(n))
except ValueError as e:
    print(e)
🔶 7) FormulaError (custom)
class FormulaError(Exception):
    pass

try:
    exp = input("Enter formula (e.g. 2 + 3): ")
    parts = exp.split()

    if len(parts) != 3:
        raise FormulaError("Must contain 3 elements")

    a, op, b = parts

    if op not in ['+', '-', '*', '/']:
        raise FormulaError("Invalid operator")

    a = float(a)
    b = float(b)

    if op == '/' and b == 0:
        raise FormulaError("Division by zero")

    if op == '+': print(a + b)
    elif op == '-': print(a - b)
    elif op == '*': print(a * b)
    elif op == '/': print(a / b)

except FormulaError as e:
    print("Error:", e)
🔶 8) TypeError example
def add(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Only integers allowed")
    return a + b

try:
    print(add(5, "a"))
except TypeError as e:
    print(e)
🔶 9) Multiple custom exceptions
class NegativeError(Exception):
    pass

class OverflowList(Exception):
    pass

try:
    n = int(input("Enter number: "))
    if n < 0:
        raise NegativeError("Negative number not allowed")

    lst = []
    max_size = 3

    for i in range(5):
        if len(lst) >= max_size:
            raise OverflowList("List overflow")
        lst.append(int(input("Enter value: ")))

except NegativeError as e:
    print(e)

except OverflowList as e:
    print(e)

except Exception as e:
    print("Some other error:", e)
