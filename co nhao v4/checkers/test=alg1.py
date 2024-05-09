import pygame
from pygame.locals import *

# Constants
WIDTH, HEIGHT = 1000, 1000
ROWS, COLS = 5, 5
SQUARE_SIZE = WIDTH // COLS
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
GREEN = (0, 128, 0)
PURPLE = (128, 0, 128)

# Piece Class
class Piece:
    PADDING = 60
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)

# Board Class
class Board:
    def __init__(self):
        self.board = []
        self.create_board()

    def draw_squares(self, win):
        # Adjust window dimensions
        global WIDTH, HEIGHT
        WIDTH = COLS * SQUARE_SIZE + 200  # Increase the width by 200 pixels
        HEIGHT = ROWS * SQUARE_SIZE + 200  # Increase the height by 200 pixels
        win.fill(WHITE)

        # Calculate the offset to center the board
        x_offset = (WIDTH - (COLS * SQUARE_SIZE)) // 2
        y_offset = (HEIGHT - (ROWS * SQUARE_SIZE)) // 2

        for col in range(COLS-1):
            for row in range(ROWS-1):
                pygame.draw.rect(win, BLACK, (col * SQUARE_SIZE + x_offset, row * SQUARE_SIZE + y_offset, SQUARE_SIZE, SQUARE_SIZE), 2)

                if row % 2 == 0 and col % 2 != 0:
                    pygame.draw.line(win, BLACK, (col * SQUARE_SIZE + x_offset, (row * SQUARE_SIZE) + SQUARE_SIZE + y_offset), (((col + 1) * SQUARE_SIZE) + x_offset, (row * SQUARE_SIZE) + y_offset), 2)
                elif row % 2 != 0 and col % 2 == 0:
                    pygame.draw.line(win, BLACK, (col * SQUARE_SIZE + x_offset, (row * SQUARE_SIZE) + SQUARE_SIZE + y_offset), (((col + 1) * SQUARE_SIZE) + x_offset, (row * SQUARE_SIZE) + y_offset), 2)
                else:
                    pygame.draw.line(win, BLACK, (col * SQUARE_SIZE + x_offset, (row * SQUARE_SIZE) + y_offset), (((col + 1) * SQUARE_SIZE) + x_offset, ((row + 1) * SQUARE_SIZE) + y_offset), 2)

    def move(self, piece, row, col):
        if abs(piece.row - row) > 1 or abs(piece.col - col) > 1:
            jumped_row = (piece.row + row) // 2
            jumped_col = (piece.col + col) // 2
            self.board[jumped_row][jumped_col] = 0
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        self.board =   [WHITE,WHITE,WHITE,WHITE,WHITE,
                        WHITE,WHITE,WHITE,WHITE,WHITE,
                        0,0,0,0,0,
                        BLUE,BLUE,BLUE,BLUE,BLUE,
                        BLUE,BLUE,BLUE,BLUE,BLUE]
        # for row in range(ROWS):
        #     for col in range(COLS):
        #         if row < 2:
        #             self.board[row].append(Piece(row, col, WHITE))
        #         elif row > 2:
        #             self.board[row].append(Piece(row, col, BLUE))
        #         else:
        #             self.board[row].append(0)

    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)
                    
    def get_valid_moves(self, piece):
        moves = {}
        row = piece.row
        col = piece.col

        # Tất cả các hướng có thể di chuyển (8 hướng)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        for drow, dcol in directions:
            next_row, next_col = row + drow, col + dcol
            # Kiểm tra xem ô tiếp theo có nằm trong phạm vi bàn cờ không
            if 0 <= next_row < ROWS and 0 <= next_col < COLS:
                # Nếu ô đó trống, thêm vào danh sách các nước đi hợp lệ
                if self.board[next_row][next_col] == 0:
                    moves[(next_row, next_col)] = []
                # Nếu ô đó có quân cờ đối phương, kiểm tra xem có thể nhảy qua không
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

# Game Class
class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = BLUE
        self.valid_moves = {}

    def winner(self):
        return self.board.winner()

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False
        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == BLUE:
            self.turn = WHITE
        else:
            self.turn = BLUE

# Main Game Loop
def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Checkers')
    clock = pygame.time.Clock()
    game = Game(win)
    run = True

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = pos[1] // SQUARE_SIZE, pos[0] // SQUARE_SIZE
                game.select(row, col)
        game.update()

    pygame.quit()

if __name__ == "__main__":
    main()
