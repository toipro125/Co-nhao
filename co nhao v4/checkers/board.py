import pygame
from .constants import BLACK, ROWS, RED, BLUE, SQUARE_SIZE, COLS, WHITE,GREEN, PURPLE,HEIGHT, WIDTH
from .piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.blue_left = self.white_left = 10
        self.create_board()
    
    def draw_squares(self, win):
        # Adjust window dimensions
        WIDTH = COLS * SQUARE_SIZE + 200  # Increase the width by 200 pixels
        HEIGHT = ROWS * SQUARE_SIZE + 200  # Increase the height by 200 pixels
        win.fill(WHITE)

        # Calculate the offset to center the board
        x_offset = (WIDTH - (COLS * SQUARE_SIZE)) // 2
        y_offset = (HEIGHT - (ROWS * SQUARE_SIZE)) // 2
        
        # Draw squares 
        for col in range(COLS-1):
            for row in range(ROWS-1):
                pygame.draw.rect(win, BLACK, ((col * SQUARE_SIZE) + x_offset, (row * SQUARE_SIZE) + y_offset, SQUARE_SIZE, SQUARE_SIZE), width=2)
      
                # Draw inner lines
                if row % 2 == 0 and col % 2 != 0 :
                    pygame.draw.line(win, BLACK, ((col * SQUARE_SIZE) + x_offset, (row * SQUARE_SIZE) + SQUARE_SIZE + y_offset), (((col + 1) * SQUARE_SIZE) + x_offset, (row * SQUARE_SIZE) + y_offset), width=2)
                elif row % 2 != 0 and col % 2 == 0:
                    pygame.draw.line(win, BLACK, ((col * SQUARE_SIZE) + x_offset, (row * SQUARE_SIZE) + SQUARE_SIZE + y_offset), (((col + 1) * SQUARE_SIZE) + x_offset, (row * SQUARE_SIZE) + y_offset), width=2)
                else:
                    pygame.draw.line(win, BLACK, ((col * SQUARE_SIZE) + x_offset, (row * SQUARE_SIZE) + y_offset), (((col + 1) * SQUARE_SIZE) + x_offset, ((row + 1) * SQUARE_SIZE) + y_offset), width=2)
        
    def move(self, piece, row, col):
        # Check if it's a jump move
        if abs(piece.row - row) > 1 or abs(piece.col - col) > 1:
            # Find the position of the jumped-over piece
            jumped_row = (piece.row + row) // 2
            jumped_col = (piece.col + col) // 2
            # Remove the jumped-over piece from the board
            self.board[jumped_row][jumped_col] = 0
        
        # Move the current piece to the new position
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                    if row <2:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 2:
                        self.board[row].append(Piece(row, col, BLUE))
                    else:
                        self.board[row].append(0)

        
    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == BLUE:
                    self.blue_left -= 1
                else:
                    self.white_left -= 1
    
    def winner(self):
        if self.blue_left <= 0:
            return WHITE
        elif self.white_left <= 0:
            return BLUE
        return None 
    
    def get_valid_moves(self, piece):
        moves = {}
        row = piece.row
        col = piece.col

        # if piece.color == BLUE and piece.color == WHITE:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for drow, dcol in directions:
            # Check one step ahead
            next_row, next_col = row + drow, col + dcol

            # Check if next position is within the board boundaries
            if 0 <= next_row < ROWS and 0 <= next_col < COLS:
                # If next position is empty, it's a valid move
                if self.board[next_row][next_col] == 0:
                    moves[(next_row, next_col)] = []

                # If next position has an opponent's piece and the next next position is empty, it's a jump move
                elif self.board[next_row][next_col].color != piece.color:
                    jump_row, jump_col = next_row + drow, next_col + dcol
                    if 0 <= jump_row < ROWS and 0 <= jump_col < COLS:
                        if self.board[jump_row][jump_col] == 0:
                            moves[(jump_row, jump_col)] = []
        
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]  # Diagonal directions

        for drow, dcol in directions:
            next_row, next_col = row + drow, col + dcol
            if (row  % 2 == 0 and piece.col % 2 == 0 or row  % 2 == 1 and piece.col % 2 == 1):
                if 0 <= next_row < ROWS and 0 <= next_col < COLS:
                    if self.board[next_row][next_col] == 0:
                        moves[(next_row, next_col)] = []

                    elif self.board[next_row][next_col].color != piece.color:
                        jump_row, jump_col = next_row + drow, next_col + dcol
                        if 0 <= jump_row < ROWS and 0 <= jump_col < COLS:
                            if self.board[jump_row][jump_col] == 0:
                                moves[(jump_row, jump_col)] = []

        return moves
    
    def _check_position(self, row, col, color):
        moves = {}
        if self.board[row][col] == 0:
            moves[(row, col)] = []
        return moves

    
   