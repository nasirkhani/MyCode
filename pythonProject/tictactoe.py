from termcolor import colored

board = list(range(1, 10))

winners = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6), (1, 4, 7), (2, 3, 8), (0, 3, 6))


def print_board():
    j = 1
    for i in board:
        end = " "
        if j % 3 == 0:
            end = "\n"
        if i == 'x':
            print(colored(f"[{i}]", "red"), end=end)
        elif i == 'O':
            print(colored(f"[{i}]", "blue"), end=end)
        else:
            print(f"[{i}]", end=end)
        j += 1


def make_move(brd, plyr, mv, undo=False):
    if can_move(brd, mv):
        board[mv - 1] = plyr
        win = is_winner(brd, plyr)
        if undo:
            brd[mv - 1] = mv
        return True, win
    return False, False


def can_move(brd, mv):
    if mv in range(1, 10) and isinstance(brd[mv - 1], int):
        return True
    return False


def is_winner(brd, plyr):
    win = True
    for tup in winners:
        win = True
        for j in tup:
            if brd[j] != plyr:
                win = False
                break
        if win:
            break
    return win


def has_empty_space():
    return board.count("x") + board.count("O") != 9


player, computer = 'x', 'O'
print('player: x\ncomputer: O\n')
while has_empty_space:
    print_board()
    move = int(input("Choose your move(1-9): "))
    moved, won = make_move(board, player, move)
    if not moved:
        print("Invalid number! Try again!")
        continue
    if won:
        print(colored("You won!", "green"))
        break
