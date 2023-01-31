# Exception handling
'''
while True:
    try:
        a = int(input('Enter a:  '))
        b = int(input('Enter b:  '))
    
    except ValueError:
        print("Only integers please... please try again")
    
    else:
        option = input('Enter operation + or - or * or / or press "q" to quit: ')
        if option == '+':
            c = a + b
            print(c)
        elif option == '-':
            c = a - b
            print(c)
        elif option == '*':
            c = a * b
            print(c)
        elif option == '/':
            try:
                c = a/b
                print(c)
            except ZeroDivisionError:
                print("Oops! I think you're trying to divide by zero! Please try again")
        elif option == 'q':
            break
        else:
            print('Sorry, invalid option. Try again...')

    finally:
        print("Thanks for using this program.") # terminate database connection/ closing a file etc
'''

'''
while True:
    try:
        a = int(input('Enter a: '))
        b = int(input('Enter b: '))
        c = a / b
    
    except ZeroDivisionError:
        print("Don't try to divide by zero.")

    except ValueError:
        print('Integers please, try again...')

    else:
        print(c)
'''
'''
while True:
    try:
        a = int(input('Enter a: '))
        b = int(input('Enter b: '))
        c = a / b
    
    # Handling ALL THE EXCEPTIONS INCLUDING keyBoardInterrupt
    except:
        print('Something went wrong, please retry...')

    else:
        print(c)
'''
'''
while True:
    try:
        a = int(input('Enter a: '))
        b = int(input('Enter b: '))
        c = a / b
    
    # Handling ALL THE EXCEPTIONS EXCLUDING keyBoardInterrupt
    except Exception:
        print('Something went wrong, please retry...')

    else:
        print(c)
'''
'''
while True:
    try:
        a = int(input('Enter a: '))
        b = int(input('Enter b: '))
        c = a / b
    
    # Handling ALL THE EXCEPTIONS EXCLUDING keyBoardInterrupt
    except Exception as e:
        print(e)

    else:
        print(c)
'''

# Resource Management using 'with' statement
'''
with open('batch.csv', 'a+') as f:      # is same as f = open('batch.csv', 'a+')
    f.seek(0)
    print(f.read())
    print(f.closed)
print(f.closed)
'''

# Using 'with' statement in conjunction with OOP:

from email import contentmanager

class ContextManager():
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode

    def __enter__(self):
        fp = open(self.file_path, self.mode)
        return fp

    def __exit__(self, exc_type, exc_value, traceback):
        f.close()

file_path = input("Enter file path with extension: ")
mode = input("Enter mode: ")
# f = ContextManager(file_path, mode)
with ContextManager(file_path, mode) as f:
    print(f.read())
    print(f.closed)
print(f.closed)