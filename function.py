#1. Multiply numbers in a list
def multiply_list(lst):
    result = 1
    for i in lst:
        result *= i
    return result

print(multiply_list([1, 2, 3, 4]))
