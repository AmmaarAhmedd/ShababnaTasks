def calculator(a, b, operation):
    if operation == 'add':
        print(a+b)
    if operation == 'sutract':
        print(a-b)
    if operation == 'multiply':
        print(a*b)
    if operation == 'divide':
        print(a/b)

a = int(input('Please enter the first number: '))
b = int(input('Please enter the second number: '))
operation = input('Please enter the desired operation (add/subtract/multiply/divide): ')
calculator(a,b,operation)
