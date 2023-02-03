


def solve(brd):
    emptyPosition = find_empty_num(brd)
    if not emptyPosition:
        return True
    else:
        row, column = emptyPosition

    for i in range(1,10):
        if isValid(brd, i, (row, column)):
            brd[row][column] = i

            if solve(brd):
                return True

            brd[row][column] = 0

    return False


def isValid(brd, num, pos):
    # Checking row if it has the same number as num
    for i in range(len(brd[0])):
        if brd[pos[0]][i] == num and pos[1] != i:
            return False

    # Checking columnumn if it has the same number as num
    for i in range(len(brd)):
        if brd[i][pos[1]] == num and pos[0] != i:
            return False

    # Checking brdx if it has the same number as num
    brdx_x = pos[1] // 3
    brdx_y = pos[0] // 3

    for i in range(brdx_y*3, brdx_y*3 + 3):
        for j in range(brdx_x * 3, brdx_x*3 + 3):
            if brd[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(brd):
    for i in range(len(brd)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(brd[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(brd[i][j])
            else:
                print(str(brd[i][j]) + " ", end="")


def find_empty_num(brd):
    for i in range(len(brd)):
        for j in range(len(brd[0])):
            if brd[i][j] == 0:
                return (i, j)  # row, column

    return None

