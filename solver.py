board = [
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

# Board will init like this
# s1 s2 s3
# s4 s5 s6
# s7 s8 s9

def get_section(board, section):
    a = dict([
    ('s1' , board[0][0:3] + board[1][0:3] + board[2][0:3]),
    ('s4' , board[3][0:3] + board[4][0:3] + board[5][0:3]),
    ('s7' , board[6][0:3] + board[7][0:3] + board[8][0:3]),

    ('s2' , board[0][3:6] + board[1][3:6] + board[2][3:6]),
    ('s5' , board[3][3:6] + board[4][3:6] + board[5][3:6]),
    ('s8' , board[6][3:6] + board[7][3:6] + board[8][3:6]),

    ('s3' , board[0][6:] + board[1][6:] + board[2][6:]),
    ('s6' , board[3][6:] + board[4][6:] + board[5][6:]),
    ('s9' , board[6][6:] + board[7][6:] + board[8][6:])
    ])
    return a[section]

def get_row(board, row):
    return board[row]

def get_col(board, col):
    #bad method, should be better one with for loop
    return [board[0][col], board[1][col],board[2][col],board[3][col],board[4][col],board[5][col],board[6][col],board[7][col],board[8][col]]

def printboard(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
                print board[i][j],

        print "\n"


def get_sectionums(section):
    retarr = []
    for i in range(3):
        for j in range(3):
            retarr.append(section[i][j])
    return retarr

def find_missingnos(section):
    nums = range(1,10)
    missing = []
    for num in nums:
        if num not in section:
            missing.append(num)
    return missing

def solve_section(section):
    #Solves section if only one missing
    missing = find_missingnos(get_sectionums(section))
    if len(missing) == 1:
        for i in range(len(section)):
            for j in range(len(section[0])):
                if section[i][j] == "":
                    section[i][j] = missing[0]
    return section

def solved(section):
    solved = True
    for element in section:
        if element == "":
            solved = False
    return solved

#printboard(board)
#print s1
