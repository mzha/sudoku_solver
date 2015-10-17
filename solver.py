import pdb;
a = [
[0,2,9,4,8,6,0,1,3],
[1,3,0,7,9,0,4,6,0],
[0,6,4,0,3,1,7,9,2],
[3,9,1,6,4,7,2,0,5],
[4,5,0,2,1,3,9,7,6],
[0,7,2,9,0,8,0,4,1],
[9,0,7,8,2,0,6,3,4],
[5,8,6,0,7,4,1,2,9],
[2,4,3,1,6,0,8,5,7]
]

b = [
[0,2,0,4,5,6,7,8,9],
[4,5,7,0,8,0,2,3,6],
[6,8,9,2,3,7,0,4,0],
[0,0,5,3,6,2,9,7,4],
[2,7,4,0,9,0,6,5,3],
[3,9,6,5,7,4,8,0,0],
[0,4,0,6,1,8,3,9,7],
[7,6,1,0,4,0,5,2,8],
[9,3,8,7,2,5,0,6,0]
]

c = [
[2,9,5,7,0,0,8,6,0],
[0,3,1,8,6,5,0,2,0],
[8,0,6,0,0,0,0,0,0],
[0,0,7,0,5,0,0,0,6],
[0,0,0,3,8,7,0,0,0],
[5,0,0,0,1,6,7,0,0],
[0,0,0,5,0,0,1,0,9],
[0,2,0,6,0,0,3,5,0],
[0,5,4,0,0,8,6,7,2]
]
#Currently cannot solve the hardest sudoku
d = [
[8,0,0,0,0,0,0,0,0],
[0,0,3,6,0,0,0,0,0],
[0,7,0,0,9,0,2,0,0],
[0,5,0,0,0,7,0,0,0],
[0,0,0,0,4,5,7,0,0],
[0,0,0,1,0,0,0,3,0],
[0,0,1,0,0,0,0,6,8],
[0,0,8,5,0,0,0,1,0],
[0,9,0,0,0,0,4,0,0]
]
#Difficult Puzzle
e = [
[0,7,0,0,9,0,8,0,0],
[2,0,4,0,7,0,0,0,0],
[0,8,9,0,0,0,0,0,1],
[0,0,0,0,8,5,0,9,0],
[0,9,0,1,0,3,0,8,0],
[0,1,0,6,2,0,0,0,0],
[7,0,0,0,0,0,5,1,0],
[0,0,0,0,6,0,9,0,8],
[0,0,3,0,1,0,0,4,0]
]


# Board will init like this
# Areas:
# 1 2 3
# 4 5 6
# 7 8 9

#-------------------------------------------------
##Board Functions
def get_area(board, area):
    a = dict([
    (1 , board[0][0:3] + board[1][0:3] + board[2][0:3]),
    (4 , board[3][0:3] + board[4][0:3] + board[5][0:3]),
    (7 , board[6][0:3] + board[7][0:3] + board[8][0:3]),

    (2 , board[0][3:6] + board[1][3:6] + board[2][3:6]),
    (5 , board[3][3:6] + board[4][3:6] + board[5][3:6]),
    (8 , board[6][3:6] + board[7][3:6] + board[8][3:6]),

    (3 , board[0][6:] + board[1][6:] + board[2][6:]),
    (6 , board[3][6:] + board[4][6:] + board[5][6:]),
    (9 , board[6][6:] + board[7][6:] + board[8][6:])
    ])
    return a[area]

def get_row(board, row):
    return board[row]

def get_col(board, col):
    ret = []
    for i in range(len(board)):
        ret.append(board[i][col])
    return ret

def printboard(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
                print board[i][j],
        print "\n"

#-------------------------------------------------
##Sync solved areas to board
def sync_row(board, row, rownum):
    board[rownum] = row
    return board

def sync_col(board, col, colnum):
    for i in range(len(board)):
        board[i][colnum] = col[i]
    return board

def sync_area(board, area, areanum):
    if areanum == 1:
        (board[0][0:3],board[1][0:3],board[2][0:3]) = area[0:3],area[3:6],area[6:9]
    elif areanum == 4:
        (board[3][0:3],board[4][0:3],board[5][0:3]) = area[0:3],area[3:6],area[6:9]
    elif areanum == 7:
        (board[6][0:3],board[7][0:3],board[8][0:3]) = area[0:3],area[3:6],area[6:9]

    elif areanum == 2:
        (board[0][3:6],board[1][3:6],board[2][3:6]) = area[0:3],area[3:6],area[6:9]
    elif areanum == 5:
        (board[3][3:6],board[4][3:6],board[5][3:6]) = area[0:3],area[3:6],area[6:9]
    elif areanum == 8:
        (board[6][3:6],board[7][3:6],board[8][3:6]) = area[0:3],area[3:6],area[6:9]

    elif areanum == 3:
        (board[0][6:],board[1][6:],board[2][6:]) = area[0:3],area[3:6],area[6:9]
    elif areanum == 6:
        (board[3][6:],board[4][6:],board[5][6:]) = area[0:3],area[3:6],area[6:9]
    elif areanum == 9:
        (board[6][6:],board[7][6:],board[8][6:]) = area[0:3],area[3:6],area[6:9]
    else:
        return "Don't let this happen"
    return board

#-------------------------------------------------
##Solve rows/cols/areas
def find_missing(section):
    nums = range(1,10)
    missing = []
    for num in nums:
        if num not in section:
            missing.append(num)
    return missing

def add_notes(section):
    missing = find_missing(section)
    for i in range(len(section)):
        if section[i] == 0 and len(missing) == 1:
            section[i] = missing[0]
    #    elif len(missing) == 0:
    #        print "We got the wrong guess"
        elif section[i] == 0:
            section[i] = missing
        elif type(section[i]) is list:
            sboth = set(missing).intersection(section[i])
            both = []
            for j in range(len(sboth)):
                both.append(sboth.pop())
            if len(both) == 1:
                section[i] = both[0]
            else:
                section[i] = both
    return section

#-------------------------------------------------
##Determine if the puzzle has been solved
def sectionsolved(section):
    solved = True
    for element in section:
        if element == 0 or type(element) is list:
            solved = False
    return solved

def solved(board):
    complete = True
    for row in board:
        complete = complete and sectionsolved(row)
    return complete

#-------------------------------------------------
##Solve Puzzle
def guess(board):
    guess = []
    tempboard = []
    #Find guess
    for i in range(len(board)):
        for j in range (len(board[0])):
            if type(board[i][j]) is list:
                guess = board[i][j]

    #Use guess to get new board
                for g in range(len(guess)):

                    print "Guessing", guess[g], "at position", str([i,j])+ ". I can guess", str(guess)
                    tempboard = board
                    tempboard[i][j] = guess[g]
                    solve(tempboard)

def iter(board):
    #Solve Rows
    for row in range(len(board)):
        sync_row(board, add_notes(get_row(board,row)), row)
    #Solve Cols
    for col in range(len(board[0])):
        sync_col(board, add_notes(get_col(board,col)), col)
    #Solve Areas
    for area in range(1,10):
        sync_area(board, add_notes(get_area(board,area)), area)
    return board

def solve(board):
    out = board
    for i in range(20):
        out = iter(board)
    if solved(out):
        print "Puzzle Solved"
        print "##################"
        printboard(out)
        print "##################"
        print "\n"

    else:
        #print "Not quite yet"
        guess(board)

#-------------------------------------------------
##Run Code
solve(e)
