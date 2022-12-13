winner = False
draw = False
turn = "O"
moves = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]




enters = False
row = 0
column = 0
def matrix(moves):
    line = [
    [moves[0], moves[1], moves[2]],  # 0
    [moves[3], moves[4], moves[5]],  # 1
    [moves[6], moves[7], moves[8]],  # 2
    [moves[0], moves[4], moves[8]],  # 3
    [moves[2], moves[4], moves[6]],  # 4
    [moves[0], moves[3], moves[6]],  # 5
    [moves[1], moves[4], moves[7]],  # 6
    [moves[2], moves[5], moves[8]],  # 7
    ] 
    return line
line = matrix(moves)


def print_grid(line):
    print("---------")
    print("|", " ".join(line[0]), "|")
    print("|", " ".join(line[1]), "|")
    print("|", " ".join(line[2]), "|")
    print("---------")
print_grid(line)



def win(player):
    global line
    global winner
    line = matrix(moves)
    a = False
    for i in range(0, 8):
        if set(player) == set(line[i]):
            a = True
            winner = True
            print(f"{player} wins")
    return a



def check_result():
    global draw
    x = win("X")
    o = win("O")
    if "_" not in moves and x == False and o == False:
        print("Draw")
        draw = True
    elif x == True and o == True:
        print("Impossible")
    elif abs(moves.count("X") - moves.count("O")) >= 2:
        print("Impossible")
    elif x == True:
        print("X wins")
    elif o == True:
        print("O wins")
        
def chek_input():
    global turn
    global moves
    global line
    if row == 1:
        moves[column - 1] = turn
    elif row == 2:
        moves[row + column] = turn
    elif row == 3:
        moves[column + 5] = turn
    line[row - 1][column - 1] = turn
    print_grid(line)
    check_result()
    if draw == False and winner == False:
        ask_input()

def check_row():
    global turn
    global row
    global column
    global draw
    global winner
    if row not in range(1, 4) or column not in range(1, 4):
        row = 0
        column = 0
        print("Coordinates should be from 1 to 3!")
        ask_input()
    elif line[row - 1][column - 1] != "_":
        print("This cell is occupied! Choose another one!")
        ask_input()
    else:
        if turn == "X":
            turn = "O"
            chek_input()
        else:
            turn = "X"
            chek_input()

def ask_input():
    global row
    global column
    try:
        a, b = input().split()
        row = int(a)
        column = int(b)
        check_row()
    except ValueError:
        print("You should enter numbers!")
ask_input()
