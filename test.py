file = open("SudokuInput", 'r')

contents = file.read().splitlines()

s = ""
for line in contents:
    line += " "
    s += line
print(contents)
print(s)
print(len(s) - 81)
