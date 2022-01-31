# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import csv
from States import *

def print_hi(name):
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        f = open('States.csv', 'r')
    except IOError:
        print('cannot open it')
    lines = csv.reader(f)
    for line in lines:
        print(','.join(line[1]))
    f.close()
    print_hi('PyCharm')


