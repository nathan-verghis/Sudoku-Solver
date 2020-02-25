
# initiating the column lists
col1 = []
col2 = []
col3 = []
col4 = []
col5 = []
col6 = []
col7 = []
col8 = []
col9 = []

# initiating the row lists
row1 = []
row2 = []
row3 = []
row4 = []
row5 = []
row6 = []
row7 = []
row8 = []
row9 = []

# initiating the box lists
box1 = []
box2 = []
box3 = []
box4 = []
box5 = []
box6 = []
box7 = []
box8 = []
box9 = []

# reading in the file
file = open("SudokuInput", "r")
contents = ""
list_contents = file.read().splitlines()
for line in list_contents:
    line += " "
    contents += line
file.close()

contents = contents.replace(" ", "")

# collecting column data
counter = 0
for value in contents:
    if counter == 0:
        col1.append(value)
        counter += 1
    elif counter == 1:
        col2.append(value)
        counter += 1
    elif counter == 2:
        col3.append(value)
        counter += 1
    elif counter == 3:
        col4.append(value)
        counter += 1
    elif counter == 4:
        col5.append(value)
        counter += 1
    elif counter == 5:
        col6.append(value)
        counter += 1
    elif counter == 6:
        col7.append(value)
        counter += 1
    elif counter == 7:
        col8.append(value)
        counter += 1
    elif counter == 8:
        col9.append(value)
        counter = 0

# collecting row data
row1.extend(list(contents[0:9]))
row2.extend(list(contents[9:18]))
row3.extend(list(contents[18:27]))
row4.extend(list(contents[27:36]))
row5.extend(list(contents[36:45]))
row6.extend(list(contents[45:54]))
row7.extend(list(contents[54:63]))
row8.extend(list(contents[63:72]))
row9.extend(list(contents[72:81]))

# converting lists of strings into lists of ints
row1 = list(map(int, row1))
row2 = list(map(int, row2))
row3 = list(map(int, row3))
row4 = list(map(int, row4))
row5 = list(map(int, row5))
row6 = list(map(int, row6))
row7 = list(map(int, row7))
row8 = list(map(int, row8))
row9 = list(map(int, row9))

col1 = list(map(int, col1))
col2 = list(map(int, col2))
col3 = list(map(int, col3))
col4 = list(map(int, col4))
col5 = list(map(int, col5))
col6 = list(map(int, col6))
col7 = list(map(int, col7))
col8 = list(map(int, col8))
col9 = list(map(int, col9))

# collecting box data
box1.extend(row1[:3])
box1.extend(row2[:3])
box1.extend(row3[:3])

box2.extend(row1[3:6])
box2.extend(row2[3:6])
box2.extend(row3[3:6])

box3.extend(row1[6:9])
box3.extend(row2[6:9])
box3.extend(row3[6:9])

box4.extend(row4[:3])
box4.extend(row5[:3])
box4.extend(row6[:3])

box5.extend(row4[3:6])
box5.extend(row5[3:6])
box5.extend(row6[3:6])

box6.extend(row4[6:9])
box6.extend(row5[6:9])
box6.extend(row6[6:9])

box7.extend(row7[:3])
box7.extend(row8[:3])
box7.extend(row9[:3])

box8.extend(row7[3:6])
box8.extend(row8[3:6])
box8.extend(row9[3:6])

box9.extend(row7[6:9])
box9.extend(row8[6:9])
box9.extend(row9[6:9])


class Cell:
    def __init__(self, val, index):
        self.value = val
        self.given = bool(self.value)

        # assigning this cell's row
        if index < 9:
            self.row = row1
        elif 9 <= index < 18:
            self.row = row2
        elif 18 <= index < 27:
            self.row = row3
        elif 27 <= index < 36:
            self.row = row4
        elif 36 <= index < 45:
            self.row = row5
        elif 45 <= index < 54:
            self.row = row6
        elif 54 <= index < 63:
            self.row = row7
        elif 63 <= index < 72:
            self.row = row8
        elif 72 <= index < 81:
            self.row = row9

        # assigning this cell's column
        if index % 9 == 0:
            self.col = col1
        elif (index - 1) % 9 == 0:
            self.col = col2
        elif (index - 2) % 9 == 0:
            self.col = col3
        elif (index - 3) % 9 == 0:
            self.col = col4
        elif (index - 4) % 9 == 0:
            self.col = col5
        elif (index - 5) % 9 == 0:
            self.col = col6
        elif (index - 6) % 9 == 0:
            self.col = col7
        elif (index - 7) % 9 == 0:
            self.col = col8
        elif (index - 8) % 9 == 0:
            self.col = col9

        # assigning this cell's box
        if index == 0 or 1 or 2 or 9 or 10 or 11 or 18 or 19 or 20:
            self.box = box1
        elif index == 3 or 4 or 5 or 12 or 13 or 14 or 21 or 22 or 23:
            self.box = box2
        elif index == 6 or 7 or 8 or 15 or 16 or 17 or 24 or 25 or 26:
            self.box = box3
        elif index == 27 or 28 or 29 or 36 or 37 or 38 or 45 or 46 or 47:
            self.box = box4
        elif index == 30 or 31 or 32 or 39 or 40 or 41 or 48 or 49 or 50:
            self.box = box5
        elif index == 33 or 34 or 35 or 42 or 43 or 44 or 51 or 52 or 53:
            self.box = box6
        elif index == 54 or 55 or 56 or 63 or 64 or 65 or 72 or 73 or 74:
            self.box = box7
        elif index == 57 or 58 or 59 or 66 or 67 or 68 or 75 or 76 or 77:
            self.box = box8
        elif index == 60 or 61 or 62 or 69 or 70 or 71 or 78 or 79 or 80:
            self.box = box9


cell_list = []

for cell in range(len(contents)):
    new_cell = Cell(contents[cell], cell)
    cell_list.append(new_cell)

# implementing the backtracking algorithm'
fixable = []
for cell in cell_list:
    if not cell.given:
        fixable.append(cell)


def backtrack(lst, num):
    for c in lst[num:]:
        if c.value == 0:
            c.value = 1
        while c.value in c.box or c.value in c.row or c.value in c.col:
            if c.value == 9:
                c.value = 0
                backtrack(lst, c.index() - 1)
            else:
                c.value += 1


backtrack(fixable, 0)

for cell in range(len(cell_list)):
    if cell % 8 != 0 or cell == 0:
        print(cell_list[cell].value, end=" ")
    else:
        if cell > 9 and (cell - 1) % 8 != 0:
            print(cell_list[cell].value, end=" ")
        else:
            print(cell_list[cell].value)
