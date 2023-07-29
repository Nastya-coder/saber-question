
print('Python calculator (print exit to stop):')

while True:
    expression = input('Expression: ')
    if expression == 'exit':
        break
    try:
        result = eval(expression)
        print('Result:', result)
    except Exception as e:
        print('Invalid expression:', expression)
