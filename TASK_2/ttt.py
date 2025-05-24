import sys
import pygame
import numpy as np
import random
import copy

from constants import *

#PYGAME SETUP
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('TIC TAC TOE AI')
screen.fill( BG_COLOR)

class Board:

    def __init__(self):
        self.squares = np.zeros((ROWS,COLS))
        self.empty_sqrs = self.squares #empty squares
        self.marked_sqrs = 0

    def final_state(self,show =False):
        '''
            returns 0 if there is no win yet
            returns 1 if player 1 wins
            returns 2 if player 2 wins
        '''

        #ver wins
        for col in range(COLS):
            if self.squares[0][col]== self.squares[1][col] ==self.squares[2][col] !=0:
                if show:
                    color=C_COLOR if self.squares[0][col] == 2 else CROSS_COLOR
                    initPos = (col*SQ_SIZE+SQ_SIZE//2,20)
                    finPos = (col*SQ_SIZE+SQ_SIZE//2,HEIGHT - 20)
                    pygame.draw.line(screen,color,initPos,finPos,LINE_WIDTH)
                return self.squares[0][col]
            
        #hor wins
        for row in range(ROWS):
            if self.squares[row][0]== self.squares[row][1] ==self.squares[row][2] !=0:
                if show:
                    color=C_COLOR if self.squares[row][0] == 2 else CROSS_COLOR
                    initPos = (20,row*SQ_SIZE+SQ_SIZE//2)
                    finPos = (WIDTH- 20,row*SQ_SIZE+SQ_SIZE//2)
                    pygame.draw.line(screen,color,initPos,finPos,LINE_WIDTH)
                return self.squares[row][0]
            
        #desc diagonal win
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] !=0:
            if show:
                    color=C_COLOR if self.squares[1][1] == 2 else CROSS_COLOR
                    initPos = (20,20)
                    finPos = (WIDTH- 20,HEIGHT-20)
                    pygame.draw.line(screen,color,initPos,finPos,CROSS_WIDTH)
            return self.squares[1][1]
        
        #asc diagonal win
        if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] !=0:
            if show:
                    color=C_COLOR if self.squares[1][1] == 2 else CROSS_COLOR
                    initPos = (20,HEIGHT - 20)
                    finPos = (WIDTH- 20,20)
                    pygame.draw.line(screen,color,initPos,finPos,CROSS_WIDTH)
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
                    empty_sqrs.append((row,col))

        return empty_sqrs

    def isfull(self):
        return self.marked_sqrs == 9
    
    def isempty(self):
        return self.marked_sqrs == 0

class AI:

    def __init__(self,level = 1, player=2):
        self.level = level
        self.player = player

    def rnd(self,board):
        empty_sqrs = board.get_empty_sqrs()
        index = random.randrange(0,len(empty_sqrs))

        return empty_sqrs[index] 

    def minmax(self,board,maximizing):
        #check terminal cases
        case = board.final_state()

        #case 1 p1 wwins
        if case ==1 :
            return 1,None 
        #case 2 p2 wins
        if case==2:
            return -1,None
        #case 3 tie
        elif board.isfull():
            return 0,None
        
        if maximizing:
            max_eval = -100
            best_move = None
            empty_sqrs = board.get_empty_sqrs()

            for(row,col) in empty_sqrs:
                temp_board= copy.deepcopy(board)
                temp_board.mark_sqr(row,col,1)
                eval = self.minmax(temp_board,False)[0]
                if eval > max_eval:
                    max_eval=eval
                    best_move = (row,col)

        
            return max_eval,best_move

        elif not maximizing:
            min_eval = 100
            best_move = None
            empty_sqrs = board.get_empty_sqrs()

            for(row,col) in empty_sqrs:
                temp_board= copy.deepcopy(board)
                temp_board.mark_sqr(row,col,self.player)
                eval = self.minmax(temp_board,True)[0]
                if eval < min_eval:
                    min_eval=eval
                    best_move = (row,col)

        
            return min_eval,best_move

    def eval(self,main_board):
        if self.level==0:
            eval = 'random'
            move = self.rnd(main_board)

        else:
            #minmax alg
            eval , move=self.minmax(main_board,False)

        print(f'AI has chosen to mark the square in position {move} with the eval of {eval}')

        return move     


class Game:

    def __init__(self):
        self.board = Board()
        self.ai = AI()
        self.player = 1 #1=x 2-o
        self.gamemode = 'ai'
        self.running =True
        self.show_lines()

    def make_move(self,row, col):
        self.board.mark_sqr(row,col,self.player)
        self.draw_fig(row,col)
        self.next_turn()

    def show_lines(self):
        screen.fill(BG_COLOR) 
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

    def change_gamemode(self):
        if self.gamemode == 'pvp':
            self.gamemode = 'ai'
        else:
            self.gamemode='pvp'

    def is_over(self):
        return self.board.final_state(show=True) != 0 or self.board.isfull()

    def reset(self):
        self.__init__()


def main():

    #game Obj
    game = Game()
    board = game.board
    ai = game.ai

    #Main Loop
    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                #key g to toggle gamemode
                if event.key == pygame.K_g:
                    game.change_gamemode()

                #r key to reset
                if event.key == pygame.K_r:
                    game.reset()
                    board = game.board
                    ai = game.ai

                #game level changing
                if event.key == pygame.K_0:
                    ai.level = 0

                if event.key == pygame.K_1:
                    ai.level = 1

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQ_SIZE
                col = pos[0] // SQ_SIZE

                if board.empty_sqr(row,col) and game.running:
                    game.make_move(row,col)

                    if game.is_over():
                        game.running = False

        if game.gamemode == 'ai' and game.player == ai.player and game.running:
            pygame.display.update()
            #updates the screeen

            row, col = ai.eval(board)
            game.make_move(row,col)

            if game.is_over():
                game.running = False

        pygame.display.update()

main()