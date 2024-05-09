import pygame
import sys

class ChessBoard:
    def __init__(self, rows, cols, cell_size):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.board = [[(row, col) for col in range(cols)] for row in range(rows)]

    def get_dimensions(self):
        return self.rows, self.cols

    def get_cell_size(self):
        return self.cell_size

    def get_position(self, row, col):
        return self.board[row][col]

class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def get_color(self):
        return self.color

    def get_position(self):
        return self.position

# Hàm kiểm tra ô có thể di chuyển đến được hay không
def is_valid_move(current_position, new_position, pieces):
    row_diff = abs(current_position[0] - new_position[0])
    col_diff = abs(current_position[1] - new_position[1])
    
    # Kiểm tra di chuyển bình thường (1 ô)
    if (row_diff == 1 and col_diff == 0) or (row_diff == 0 and col_diff == 1):
        return True
    
    # Kiểm tra nhảy (2 ô)
    elif (row_diff == 2 and col_diff == 0) or (row_diff == 0 and col_diff == 2):
        # Kiểm tra xem có quân cờ ở ô giữa không
        middle_row = (current_position[0] + new_position[0]) // 2
        middle_col = (current_position[1] + new_position[1]) // 2
        middle_position = (middle_row, middle_col)
        for piece in pieces:
            if piece.get_position() == middle_position:
                return True
        return False
    
    else:
        return False

# Hàm di chuyển quân cờ
def move_piece(piece, new_position, pieces):
    current_position = piece.get_position()
    row_diff = abs(current_position[0] - new_position[0])
    col_diff = abs(current_position[1] - new_position[1])
    
    # Di chuyển bình thường (1 ô)
    if (row_diff == 1 and col_diff == 0) or (row_diff == 0 and col_diff == 1):
        piece.position = new_position
    
    # Nhảy (2 ô)
    elif (row_diff == 2 and col_diff == 0) or (row_diff == 0 and col_diff == 2):
        # Loại bỏ quân cờ ở ô giữa
        middle_row = (current_position[0] + new_position[0]) // 2
        middle_col = (current_position[1] + new_position[1]) // 2
        middle_position = (middle_row, middle_col)
        for other_piece in pieces:
            if other_piece.get_position() == middle_position:
                pieces.remove(other_piece)
                break
        piece.position = new_position

# Khởi tạo Pygame
pygame.init()

# Các màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Kích thước màn hình
WIDTH, HEIGHT = 800, 600

# Kích thước ô cờ
CELL_SIZE = 100

# Số lượng ô cờ trên bảng
NUM_ROWS = 5
NUM_COLS = 5

# Khởi tạo bàn cờ
board = ChessBoard(NUM_ROWS, NUM_COLS, CELL_SIZE)

# Khởi tạo các quân cờ
pieces = []
for row in range(NUM_ROWS):
    for col in range(NUM_COLS):
        if row < 2:
            pieces.append(Piece(BLACK, (row, col)))
        elif row >= NUM_ROWS - 2:
            pieces.append(Piece(WHITE, (row, col)))

# Khởi tạo màn hình
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cờ nhảy")

# Khởi tạo biến lượt đi
current_player = BLACK  # Lượt đi ban đầu

# Hàm vẽ bảng cờ
def draw_board():
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            pygame.draw.rect(screen, WHITE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 3)

# Hàm vẽ quân cờ
def draw_pieces():
    for piece in pieces:
        if piece.get_color() == BLACK:
            pygame.draw.circle(screen, BLACK, (piece.get_position()[1] * CELL_SIZE + CELL_SIZE // 2, piece.get_position()[0] * CELL_SIZE + CELL_SIZE // 2), 20)
        else:
            pygame.draw.circle(screen, WHITE, (piece.get_position()[1] * CELL_SIZE + CELL_SIZE // 2, piece.get_position()[0] * CELL_SIZE + CELL_SIZE // 2), 20)

# Hàm đổi lượt đi
def switch_turn():
    global current_player
    if current_player == BLACK:
        current_player = WHITE
    else:
        current_player = BLACK

# Hàm main
def main():
    # Vòng lặp chính
    while True:
        screen.fill(RED)
        draw_board()
        draw_pieces()

        # Xử lý sự kiện
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Di chuyển quân cờ khi nhấn chuột
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                clicked_row = mouse_pos[1] // CELL_SIZE
                clicked_col = mouse_pos[0] // CELL_SIZE
                
                for piece in pieces:
                    if piece.get_position() == (clicked_row, clicked_col) and piece.get_color() == current_player:
                        new_position = (clicked_row, clicked_col)
                        move_piece(piece, new_position, pieces)
                        switch_turn()  # Đổi lượt đi sau khi di chuyển
                        break  # Thoát vòng lặp sau khi di chuyển một quân cờ

        # Hiển thị màn hình
        pygame.display.flip()

# Chạy chương trình
if __name__ == "__main__":
    main()
