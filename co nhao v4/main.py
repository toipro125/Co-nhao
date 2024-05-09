
import pygame
import pygame, sys
# from checkers.button import Button
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED,BLUE
from checkers.game import Game
#from minimax.algorithm import minimax

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

pygame.init()

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
    
    pygame.quit()

main()

# SCREEN = pygame.display.set_mode((1280, 720))
# pygame.display.set_caption("Cờ nhào")

# BG = pygame.image.load("assets/Background.png")

# def get_font(size): # Returns Press-Start-2P in the desired size
#     return pygame.font.Font("assets/font.ttf", size)

# def display_winner_message(winner):
#     font = pygame.font.Font(None, 36)
#     text = font.render(f"Winner: {winner}", True, (255, 255, 255))
#     text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
#     SCREEN.blit(text, text_rect)
#     pygame.display.update()

# def play():
#     while True:
#         FPS = 60
        
#         PLAY_MOUSE_POS = pygame.mouse.get_pos()

#         SCREEN.fill("black")

#         # PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
#         # PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
#         # SCREEN.blit(PLAY_TEXT, PLAY_RECT)

#         PLAY_BACK = Button(image=None, pos=(640, 460), 
#                             text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

#         PLAY_BACK.changeColor(PLAY_MOUSE_POS)
#         PLAY_BACK.update(SCREEN)

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
#                     main_menu()
        
#             WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#             pygame.display.set_caption('Cờ nhào')           
#             run = True
#             clock = pygame.time.Clock()
#             game = Game(WIN)

#             while run:
#                 clock.tick(FPS)

#                 if game.winner() != None:
#                         print(game.winner())
#                         run = False

#                 for event in pygame.event.get():
#                     if event.type == pygame.QUIT:
#                         run = False
                    
#                     if event.type == pygame.MOUSEBUTTONDOWN:
#                         pos = pygame.mouse.get_pos()
#                         row, col = get_row_col_from_mouse(pos)
#                         game.select(row, col)
                

#                 game.update()
        
#             pygame.quit()

#         pygame.display.update()
    
# def options():
#     while True:
#         OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

#         SCREEN.fill("white")

#         OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
#         OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
#         SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

#         OPTIONS_BACK = Button(image=None, pos=(640, 460), 
#                             text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

#         OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
#         OPTIONS_BACK.update(SCREEN)

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
#                     main_menu()

#         pygame.display.update()

# def main_menu():
#     while True:
#         SCREEN.blit(BG, (0, 0))

#         MENU_MOUSE_POS = pygame.mouse.get_pos()

#         MENU_TEXT = get_font(100).render("MENU", True, "#b68f40")
#         MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

#         PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
#                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
#         OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
#                             text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
#         QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
#                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

#         SCREEN.blit(MENU_TEXT, MENU_RECT)

#         for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
#             button.changeColor(MENU_MOUSE_POS)
#             button.update(SCREEN)
        
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
#                     play()
#                 if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
#                     options()
#                 if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
#                     pygame.quit()
#                     sys.exit()

#         pygame.display.update()

# main_menu()

# def main():
#     run = True
#     clock = pygame.time.Clock()
#     game = Game(WIN)

#     while run:
#         clock.tick(FPS)

#         if game.winner() != None:
#             print(game.winner())
#             run = False

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
            
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 pos = pygame.mouse.get_pos()
#                 row, col = get_row_col_from_mouse(pos)
#                 game.select(row, col)

#         game.update()
    
#     pygame.quit()

# main()