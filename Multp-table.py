#This project prints out a multiplication table
print("Multiplication table using neted for loop \n Author: Francis Chiputa")
print("________________________________________________________________________________________________")
print("|       0  |   1  |   2  |    3 |    4 |    5 |   6  |    7 |    8  |   9 |  10  |   11 |   12 ")
print("|__________|______|______|______|______|______|______|______|_______|_____|______|______|______|")

for number in range(0, 13):
    print(str(number).rjust(2), end='')#Converting int to str. Align to right just by 2 spaces in a row
    print("  | ", end='')#print bars in the next line in a row

    for number1 in range(0, 13):
        print(str(number * number1).rjust(3), end='')
        print("  | ", end='')
    print()
