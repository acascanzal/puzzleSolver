from colorama import Fore, Back, Style, init

# Inicializa colorama
init()

# Mapa de colores para las piezas
color_map = {
    0: Fore.BLACK,
    1: Fore.RED,
    2: Fore.GREEN,
    3: Fore.YELLOW,
    4: Fore.BLUE,
    5: Fore.MAGENTA,
    6: Fore.CYAN,
    7: Fore.WHITE,
    8: Fore.RED + Style.BRIGHT,
    9: Fore.GREEN + Style.BRIGHT,
    10: Fore.YELLOW + Style.BRIGHT,
    11: Fore.BLUE + Style.BRIGHT,
    12: Fore.MAGENTA + Style.BRIGHT
}

def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            # Selecciona el color basado en la pieza
            color = color_map.get(board[i][j], Fore.RESET)
            # Imprime la pieza con el color correspondiente
            print(f"{color}{board[i][j]:>2}{Style.RESET_ALL}", end=" ")
        print()
    print()

def print_piece(piece):
    for i in range(5):
        for j in range(5):
            # Selecciona el color basado en la pieza
            color = color_map.get(piece.piece_get_element(i,j), Fore.RESET)
            # Imprime la pieza con el color correspondiente
            print(f"{color}{piece.piece_get_element(i,j):>2}{Style.RESET_ALL}", end=" ")
        print()
    print()
