board = [
[1, 2, 3],
["", 5, 6],
[7, "", 9]

]

#def readboard(board):

def printboard(board):
    for arr in board:
        print arr

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

print find_missingnos(get_sectionums(board))
