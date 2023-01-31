# f = open('D:\\Royal\\Royal_Website.txt')
# f = open('batch.txt')
# content = f.read()
# print(content)

# print(f.read(25))

# f.close()

'''
file_pointer_name = open('file_path', 'Mode1Mode2')

Mode1   Name        Description                                                 Mode2       Name
r       read        Opens the file for reading only.                            t           text        Default
                    Does not create the file if it doesn't exist.
                    Does not erase the content of the file.
                    Cursor is placed at the begining of the file.

w       write       Opens the file for writing only.                            b           binary
                    Creates the file if it doesn't exist.
                    Erases the entire content of the file as soon as it opens.
                    Cursor is placed at the begining of the file.

a       append      Opens the file for writing only.
                    Creates the file if it doesn't exist.
                    Does not erase the content of the file.
                    Cursor is placed at the END of the file.

x       Exclusively Creates the file and enable writing only.
        create      Raises FileExistsError if the file already exists.
                    Cursor is placed at the begining of the file.

r+      read plus   Opens the file for reading and writing both.
                    Does not create the file if it doesn't exist.
                    Does not erase the content of the file.
                    Cursor is placed at the begining of the file.

w+      write plus  Opens the fiel for writing and reading both.
                    Creates the file if it doesn't exist.
                    Erases the entire content of the file as soon as it opens.
                    Cursor is placed at the begining of the file.

a+      append plus Opens the file for writing and reading both.
                    Creates the file if it doesn't exist.
                    Does not erase the content of the file.
                    Cursor is placed at the END of the file.

'''

# f = open('batch.txt', 'w')
# f.write('Happy birthday to unknown!')

# f.close()
'''
fileName = input("Enter file name: ")
fileMode = input("Mode: ")

f = open(fileName, fileMode)
"""
print('cursor =', f.tell())
print(f.read(25))
print('cursor =', f.tell())
print(f.read(30))
print('cursor =', f.tell())
print(f.read())
print('cursor =', f.tell())

f.seek(26)
print('cursor =', f.tell())
print(f.read())
"""

# first_line = f.readline()
# second_line = f.readline()
# print(first_line)
# print(second_line)

# print(f.readable())
if f.readable():
    print(f.readlines())

print(f.closed)

f.close()
print(f.closed)
'''
'''
f = open('friday.txt', 'w')

# f.write('These days come just before the weekends.')
# text = [
#     'These days come just before the weekends.\n',
#     'We have Python class on every firday.\n',
#     'Attendees were 193 in the first lecture.\n',
#     'In the process, 122 died and 71 left.'
# ]
# f.writelines(text)
print(f.writable())

f.close()
'''
'''
f = open('batch.txt', 'a')
f.write('\n6\tSujal\tTeacher')
f.close()
'''
'''
f = open('friday.txt', 'x')
f.write('Today is saturday.')
f.close()
'''
'''
f = open('batch.txt', 'r+')     # same as: f = open('batch.txt', 'r+t')
# print(f.read())
f.read()
f.write('\n7\tMadhav\tSinger')
f.close()
'''

f = open('batch.csv', 'r')
data = f.readlines()
f.close()

offset = 5
print("Press 1 to view a student's details")
print("Press 2 to update a student's details")
print("Press 3 to delete a student")
print("Press 4 to add a new student")
choice = int(input())
if choice == 1:
    index_no = int(input("Enter sr no: ")) + offset
    print('Sr\tName\tRole')
    print(data[index_no].replace(',', '\t'))

elif choice == 2:
    pass

elif choice == 3:
    pass

elif choice == 4:
    pass

else:
    print('invalid')