import sys
import pygame
import numpy as np

from constants import *

#PYGAME SETUP
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('TIC TAC TOE AI')
screen.fill( BG_COLOR)

class Board:

    def __init__(self):
        self.squares = np.zeros((ROWS,COLS))
        self.empty_sqr = self.squares #empty squares
        self.marked_sqrs = 0

    def final_state(self):
        '''
            returns 0 if there is no win yet
            returns 1 if player 1 wins
            returns 2 if player 2 wins
        '''

        #ver wins
        for col in range(COLS):
            if self.squares[0][col]== self.squares[1][col] ==self.squares[2][col] !=0:
                return self.squares[0][col]
            
        #hor wins
        for row in range(ROWS):
            if self.squares[0][row]== self.squares[1][row] ==self.squares[2][row] !=0:
                return self.squares[row][0]
            
        #desc diagonal win
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] !=0:
            return self.squares[1][1]
        
        #asc diagonal win
        if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] !=0:
            return self.squares[1][1]

        #no win yet
        return 0

    def mark_sqr(self,row,col,player):
        self.squares[row][col]=player
        self.marked_sqrs += 1

    def empty_sqr(self,row,col):
        return self.squares[row][col] == 0

    def get_empty_sqrs(self):
        empty_sqrs = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.empty_sqr(row,col):
                    empty_sqrs.appenf((row,col))

        return empty_sqrs

    def isfull(self):
        return self.marked_sqrs == 9
    
    def isempty(self):
        return self.marked_sqrs == 0

class Game:

    def __init__(self):
        self.board = Board()
        #self.ai = AI()
        self.player = 1 #1=x 2-o
        self.gamemode = 'pvp'
        self.running =True
        self.show_lines()
    
    def show_lines(self):
        #vertical lines
        pygame.draw.line(screen, LINE_COLOR,(SQ_SIZE,0),(SQ_SIZE,HEIGHT),LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR,(WIDTH - SQ_SIZE,0),(WIDTH - SQ_SIZE,HEIGHT),LINE_WIDTH)

        #horizontal lines
        pygame.draw.line(screen, LINE_COLOR,(0,SQ_SIZE),(HEIGHT,SQ_SIZE),LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR,(0,HEIGHT - SQ_SIZE),(WIDTH,HEIGHT - SQ_SIZE),LINE_WIDTH)

    def draw_fig(self,row,col):
        if self.player ==1:
            #draw x
            #desc line
            start_desc=(col *SQ_SIZE +OFFSET,row*SQ_SIZE+OFFSET)
            end_desc=(col*SQ_SIZE+SQ_SIZE-OFFSET,row*SQ_SIZE+SQ_SIZE-OFFSET)
            pygame.draw.line(screen,CROSS_COLOR,start_desc,end_desc,CROSS_WIDTH)
            #asc line
            start_asc=(col *SQ_SIZE +OFFSET,row*SQ_SIZE+ SQ_SIZE -OFFSET)
            end_asc=(col*SQ_SIZE+SQ_SIZE-OFFSET,row*SQ_SIZE+OFFSET)
            pygame.draw.line(screen,CROSS_COLOR,start_asc,end_asc,CROSS_WIDTH)
            
        elif self.player == 2:
            #draw o
            center = (col * SQ_SIZE+SQ_SIZE//2 ,row * SQ_SIZE +SQ_SIZE//2)
            pygame.draw.circle(screen,C_COLOR,center,RADIUS,C_WIDTH)


    def next_turn(self):
        self.player=self.player % 2 + 1

def main():

    #game Obj
    game = Game()
    board = game.board

    #Main Loop
    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQ_SIZE
                col = pos[0] // SQ_SIZE

                if board.empty_sqr(row,col):
                    board.mark_sqr(row,col,game.player)
                    game.draw_fig(row,col)
                    game.next_turn()
                    print(board.squares)
                
        pygame.display.update()

main()