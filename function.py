#1. Multiply numbers in a list
def multiply_list(lst):
    result = 1
    for i in lst:
        result *= i
    return result

print(multiply_list([1, 2, 3, 4]))
#2.Twin prime numbers
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return n > 1

for i in range(2, 100):
    if is_prime(i) and is_prime(i+2):
        print(i, i+2)
#3. Reverse a string
def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))
# 4. Count upper & lower case
def count_case(s):
    upper = lower = 0
    for ch in s:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
    return upper, lower

print(count_case("Hello World"))
#5. Distinct elements list
def distinct_list(lst):
    return list(set(lst))

print(distinct_list([1,2,2,3,4,4]))
# 6. Print odd numbers from list
def odd_numbers(lst):
    return [i for i in lst if i % 2 != 0]

print(odd_numbers([1,2,3,4,5]))
#7. Greatest using lambda
greatest = lambda a, b, c: max(a, b, c)

print(greatest(10, 20, 15))
#8. Lambda operations
add = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
div = lambda a, b: a / b
mod = lambda a, b: a % b

print(add(5,3), sub(5,3), mul(5,3), div(5,3), mod(5,3))
#9. Factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))
#10. Fibonacci (recursive & non-recursive)

#Recursive:

def fib_rec(n):
    if n <= 1:
        return n
    return fib_rec(n-1) + fib_rec(n-2)

for i in range(10):
    print(fib_rec(i), end=" ")

#Non-recursive:

def fib_nonrec(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

fib_nonrec(10)
#11. Reverse number using recursion
def reverse_num(n, rev=0):
    if n == 0:
        return rev
    return reverse_num(n//10, rev*10 + n%10)

print(reverse_num(1234))
#12. Filter odd numbers
lst = [1,2,3,4,5]
odd = list(filter(lambda x: x % 2 != 0, lst))
print(odd)
#13. Cube using map()
lst = [1,2,3,4,5]
cube = list(map(lambda x: x**3, lst))
print(cube)
# 14. Area module (SHAPES)
# shapes.py
def circle(r):
    return 3.14 * r * r

def square(a):
    return a * a

def rectangle(l, b):
    return l * b

def triangle(b, h):
    return 0.5 * b * h
# main.py
import shapes

print(shapes.circle(5))
print(shapes.rectangle(4,6))
#15. Employee module
# employee.py
def da(basic):
    return 0.1 * basic

def hra(basic):
    return 0.2 * basic

def it(gross):
    return 0.1 * gross
# main.py
import employee

basic = 10000
gross = basic + employee.da(basic) + employee.hra(basic)
net = gross - employee.it(gross)

print("Gross:", gross)
print("Net:", net)
# 16. Swap numbers (menu)
def swap(a, b):
    return b, a

def main():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    print("Before:", a, b)
    a, b = swap(a, b)
    print("After:", a, b)

main()
