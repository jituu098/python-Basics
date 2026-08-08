board = {"Top-l:": " ", "Top-M": " ", "Top-R": " ",
         "Mid-l:": " ", "Mid-M": " ", "Mid-R": " ",
         "Low-l:": " ", "Low-M": " ", "Low-R": " " }
def print_board(board):
    print(board["Top-l:"] + "|" + board["Top-M"] + "|" + board["Top-R"])  
    print("-+-+-")
    print(board["Mid-l:"] + "|" + board["Mid-M"] + "|" + board["Mid-R"])
    print("-+-+-")
    print(board["Low-l:"] + "|" + board["Low-M"] + "|" + board["Low-R"])
print_board(board)
turn = "X"
for i in range(9):
    print("Turn for " + turn + ". Move on which space?")
    move = input()
    board[move] = turn
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
    print_board(board)
