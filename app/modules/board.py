from piece import Piece  # Assuming you have a Piece class implemented in piece.py

class Board():
    def __init__(self):
        self.positions = {}

        # Initialize white pieces
        self.initialize_rank(1, "White")
        
        # Initialize white pawns
        self.initialize_pawns(2, "White")

        # Initialize black pieces
        self.initialize_rank(8, "Black")

        # Initialize black pawns
        self.initialize_pawns(7, "Black")

    def initialize_rank(self, rank, color):
        columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        for column in columns:
            position = f"{column}{rank}"
            if rank == 1 or rank == 8:
                # Back rank pieces
                piece_type = ""
                if column == 'a' or column == 'h':
                    piece_type = "Rook"
                elif column == 'b' or column == 'g':
                    piece_type = "Knight"
                elif column == 'c' or column == 'f':
                    piece_type = "Bishop"
                elif column == 'd':
                    piece_type = "Queen"
                elif column == 'e':
                    piece_type = "King"

                self.positions[position] = Piece(piece_type, color, position)
            else:
                # Empty squares for ranks 2-7
                self.positions[position] = None

    def initialize_pawns(self, rank, color):
        columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        for column in columns:
            position = f"{column}{rank}"
            self.positions[position] = Piece("Pawn", color, position)
