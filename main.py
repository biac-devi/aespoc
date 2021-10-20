# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Crypto.Cipher import AES

def print_hi(x, y):
    # Use a breakpoint in the code line below to debug your script.
    return x + y # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
#    print_hi('PyCharm')
#     L = ["Geeks\n", "for\n", "Geeks\n"]
#
#     # writing to file
#     file1 = open('myfile.txt', 'w')
#     file1.writelines(L)
#     file1.close()

    # Using readlines()
    file1 = open('myfile.txt', 'r')
    Lines = file1.readlines()

    count = 0
    # Strips the newline character
    for line in Lines:
        count += 1
        print("Line{}: {}".format(count, line.strip()))

    line = Lines[0]
    x,y = line.split()
    print(x)
    print(y)

    splitedstr = line.split()
    print(splitedstr[0])
    print(splitedstr[1])
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
