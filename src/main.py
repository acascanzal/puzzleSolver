#you need to install colorama to run this code

from elements.pieces.piece import Piece
from elements.board.board import Board
from utils.print_functions import *

def solve(board, rest_pieces, putted_pieces):
    print_board(board.get_board())
    if len(rest_pieces) == 0:
        print("Solution found")
        return True
    
    for piece in rest_pieces:
        if board.put_piece(piece):
            putted_pieces.append(piece)
            rest_pieces.remove(piece)
            
            if solve(board, rest_pieces, putted_pieces):
                return True

            board.remove_piece(piece)
            putted_pieces.pop()
            rest_pieces.append(piece) 
    return False




board = Board(5,11)

piece1 = Piece([
    [1,1,0,0,0],
    [0,1,1,1,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
    ],5,1)
piece2 = Piece([
    [2,0,0,0,0],
    [2,2,2,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
    ],4,2)
piece3 = Piece([
    [3,3,0,0,0],
    [3,3,3,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
    ],5,3)
piece4 = Piece([
    [0,4,0,0,0],
    [4,4,4,0,0],
    [0,4,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
    ],5,4)
piece5 = Piece([
    [5,5,5,0,0],
    [0,0,5,0,0],
    [0,0,5,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
    ],5,5)
piece6 = Piece([
    [0,6,0,0,0],
    [0,6,0,0,0],
    [0,6,0,0,0],
    [6,6,0,0,0],
    [0,0,0,0,0]
    ],5,6)
piece7 = Piece([
    [7,7,7,7,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
    ],4,7)
piece8 = Piece([
    [8,8,8,8,0],
    [0,0,8,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
    ],5,8)
piece9 = Piece([
    [9,9,0,0,0],
    [0,9,9,0,0],
    [0,0,9,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
    ],5,9)
piece10 = Piece([
    [10,0,0,0,0],
    [10,10,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
    ],3,10)
piece11 = Piece([
    [11,11,0,0,0],
    [0,11,0,0,0],
    [11,11,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
    ],5,11)
piece12 = Piece([
    [12,12,0,0,0],
    [12,12,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
    ],4,12)
rest_pieces = [piece1,piece2,piece3,piece4,piece5,piece6,piece7,piece8,piece9,piece10,piece11,piece12]
putted_pieces = []
solve(board, rest_pieces, putted_pieces)
print("End of the program")

