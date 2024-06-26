# structure for coverage info
coverage_info = {
    'branch_1': False,
    'branch_2': False,
    'branch_3': False,
    'branch_4': False,
}

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for i in range(3):
        # Check rows and columns
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

   # Output coverage information to a file
    with open('output.txt', 'w') as file:
        file.write("Conditional Branch Coverage Information:\n")
        for branch, taken in coverage_info.items():
            file.write(f"{branch}: {'Taken' if taken else 'Not Taken'}\n")

    while True:
        print_board(board)
        row = int(input(f"Player {player}, enter the row (0, 1, 2): "))
        col = int(input(f"Player {player}, enter the column (0, 1, 2): "))

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            coverage_info['branch_1'] = True
            board[row][col] = player
            if check_winner(board, player):
                coverage_info['branch_2'] = True
                print_board(board)
                print(f"Player {player} wins!")
                break

            if is_full(board):
                coverage_info['branch_3'] = True
                print_board(board)
                print("It's a draw!")
                break

            player = "O" if player == "X" else "X"
        else:
            coverage_info['branch_4'] = True
            print("Invalid move. Try again.")

    # Second output needed for when the game ends
    with open('output.txt', 'w') as file:
        file.write("Conditional Branch Coverage Information:\n")
        for branch, taken in coverage_info.items():
            file.write(f"{branch}: {'Taken' if taken else 'Not Taken'}\n")

if __name__ == "__main__":
    main()