# Created by Emma Hodor on 12/30/2022
# ASCII art generated using patorjk.com
heading = """
 _______  _______  _        _______           _        _______ _________ _______  _______ 
(  ____ \(  ___  )( \      (  ____ \|\     /|( \      (  ___  )\__   __/(  ___  )(  ____ )
| (    \/| (   ) || (      | (    \/| )   ( || (      | (   ) |   ) (   | (   ) || (    )|
| |      | (___) || |      | |      | |   | || |      | (___) |   | |   | |   | || (____)|
| |      |  ___  || |      | |      | |   | || |      |  ___  |   | |   | |   | ||     __)
| |      | (   ) || |      | |      | |   | || |      | (   ) |   | |   | |   | || (\ (   
| (____/\| )   ( || (____/\| (____/\| (___) || (____/\| )   ( |   | |   | (___) || ) \ \__
(_______/|/     \|(_______/(_______/(_______)(_______/|/     \|   )_(   (_______)|/   \__/
                                                                                          """

print(heading)
print('Welcome to this simple calculator app!')


def calculator(num1=None, num2=None):
    def add(num1, num2):
        return num1 + num2

    def sub(num1, num2):
        return num1 - num2

    def mult(num1, num2):
        return num1 * num2

    def div(num1, num2):
        return num1 / num2

    operations = {
        '+': add,
        '-': sub,
        '*': mult,
        '/': div
    }
    if num1 is None:
        while True:
            first = input('What is your first number? ')
            if first.isdigit():
                first = int(first)
                break
            else:
                print('Please enter valid number.\n')
    else:
        first = int(num1)

    for operation in operations:
        print(operation)

    while True:
        chosen_operation = input('Choose an operation from one of the above. ')
        if chosen_operation in operations:
            break
        else:
            print('Please enter valid operation.\n')

    if num2 is None:
        while True:
            sec = input('What is your second number? ')
            if sec.isdigit():
                sec = int(sec)
                break
            else:
                print('Please enter valid number.\n')
    else:
        sec = int(num2)

    chosen_op = operations[chosen_operation]

    evaluation = chosen_op(first, sec)
    print(f'{first} {chosen_operation} {sec} = {evaluation}')

    while True:
        next_step = input(f"Enter 'c' to do calculation with {evaluation}, 'n' to do new calculation, or 'e' to quit. ")
        if next_step == 'c' or next_step == 'n' or next_step == 'e':
            break
        else:
            print(f'Please enter valid command.\n')

    if next_step == 'c':
        while True:
            first_or_sec = input(f"Should {evaluation} be the 'first' or 'second' number used? ")
            if first_or_sec == 'first' or first_or_sec == 'second':
                break
            else:
                print('Please enter valid command.\n')
        if first_or_sec == 'first':
            calculator(evaluation)
        else:
            calculator(None, evaluation)
    elif next_step == 'n':
        calculator()


calculator()
