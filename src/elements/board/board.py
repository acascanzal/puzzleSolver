from ..pieces.piece import Piece

class Board:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.board = [[0 for i in range(columns)] for j in range(rows)]
    
    def get_board(self):
        return self.board
    
    def get_first_empty_position(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.board[i][j] == 0:
                    return (i,j)
        return None
    
    def valid_index(self,i,j):
        return i >= 0 and i < self.rows and j >= 0 and j < self.columns
    
    def copy_piece_in_board(self, board_position, piece: Piece, piece_position):
        rows, cols = len(piece.get_form()), len(piece.get_form()[0])
        affected_positions = []  # Guardamos las posiciones afectadas en el tablero

        # Intentamos colocar toda la pieza en el tablero
        for i in range(rows):
            for j in range(cols):
                # Calculamos la posición en el tablero para la pieza
                board_i = board_position[0] + i - piece_position[0]
                board_j = board_position[1] + j - piece_position[1]

                # Verificamos que la posición sea válida y que la posición en el tablero esté vacía
                if piece.valid_index(i, j) and self.valid_index(board_i, board_j):
                    if self.board[board_i][board_j] != 0 and piece.piece_get_element(i, j) != 0:
                        return False
                elif piece.piece_get_element(i, j) != 0:
                    return False
        
        # Si todas las posiciones son válidas, colocamos la pieza
        for i in range(rows):
            for j in range(cols):
                board_i = board_position[0] + i - piece_position[0]
                board_j = board_position[1] + j - piece_position[1]
                if piece.piece_get_element(i, j) != 0:
                    self.board[board_i][board_j] = piece.piece_get_element(i, j)
                    affected_positions.append((board_i, board_j))  # Guardamos la posición afectada
                    piece.subtract_item()

        # Si la pieza fue colocada exitosamente
        return True

    def revert_piece_in_board(self, affected_positions, piece: Piece):
        # Revertimos la colocación de la pieza en las posiciones afectadas
        for pos in affected_positions:
            self.board[pos[0]][pos[1]] = 0
            piece.add_item()

        
            
    

    def put_piece(self,piece: Piece):
        first_empty_position = self.get_first_empty_position()
        
        if first_empty_position:
            for i in range(4):
                first_position_piece = piece.get_first_position()
                if self.copy_piece_in_board(first_empty_position, piece, first_position_piece):
                    return True
                else:
                    piece.rotate()
            return False
        else:
            return False
        
    def remove_piece(self,piece: Piece):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.board[i][j] == piece.color:
                    self.board[i][j] = 0
                    piece.add_item()
        return True

            
        
                    
        