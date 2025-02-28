def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]  # Retorna el ganador ("X" o "O")

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None  # No hay ganador todavía

def is_full(board):
    """Verifica si el tablero está lleno (empate)."""
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        
        # Captura de errores para evitar entradas inválidas
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input. Enter a number between 0 and 2.")
                continue  # Pedir entrada otra vez

        except ValueError:
            print("Invalid input. Please enter a number.")
            continue  # Pedir entrada otra vez

        # Verificar si la casilla está ocupada
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue  # Pedir entrada otra vez

        # Realizar el movimiento
        board[row][col] = player

        # Verificar si hay un ganador
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        # Verificar si hay un empate
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Cambiar turno
        player = "O" if player == "X" else "X"

tic_tac_toe()
