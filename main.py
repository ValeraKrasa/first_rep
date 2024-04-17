
def add_numbers(num1, num2):

    num1 = int(input('Enter number 1 - '))
    num2 = int(input('Enter number 1 - '))
    result = add_numbers(num1, num2)
    return num1 + num2




print(f'Result {add_numbers()}')