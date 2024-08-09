class Piece:
    def __init__(self, pieceArray,piece_items,color):
        if len(pieceArray) != 5:
            raise ValueError("A piece must have 5 elements")
        
        for fila in pieceArray:
            if len(fila) != 5:
                raise ValueError("A piece must have 5 elements")
        
        self.piece = pieceArray
        self.items = piece_items
        self.color = color

    def get_first_position(self):
        for i in range(5):
            for j in range(5):
                if self.piece[i][j] != 0:
                    return (i,j)
        return None
    
    def get_remaining_items(self):
        return self.items

    def piece_get_element(self,i,j):
        return self.piece[i][j]
    
    def get_form(self):
        return self.piece


    def rotate(self):
        # Rotates the piece 90 degrees
        self.piece = [[self.piece[j][i] for j in range(5)] for i in range(5)]
        self.piece = [list(reversed(fila)) for fila in self.piece]
        return self.piece
    
    def valid_index(self,i,j):
        return i >= 0 and i < 5 and j >= 0 and j < 5
    
    def subtract_item(self):
        self.items -= 1
    def add_item(self):
        self.items += 1