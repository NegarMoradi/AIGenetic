from copy import deepcopy
import pygame
from math import inf

RED = (255,0,0)
WHITE = (255,255,255)
GREEN = (0, 255, 0)
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

def maxi(position, game, depth):
    
    if position.winner() != None or depth == 0 :
        return position.evaluate(), position
    
    bestMove, maxim = None, -inf
    moves = getAllMoves(position, WHITE, game)
    for move in moves:
        newDepth = depth - 1
        evalu, bMove = mini(move, game, newDepth)
        if maxim <= evalu and (evalu != inf or maxim == -inf):
            if maxim <= evalu:
                bestMove = move
                maxim = evalu
    
    return maxim, bestMove

def mini(position, game, depth):
    
    if position.winner() != None or depth == 0 :
        return position.evaluate(), position
    
    bestMove, minim = None, inf
    moves = getAllMoves(position, RED, game)
    for move in moves:
        newDepth = depth - 1
        evalu, bMove = maxi(move, game, newDepth)
        if minim >= evalu and (evalu!= -inf or minim == inf):
            if minim >= evalu:
                bestMove = move
                minim = evalu
    
    return minim, bestMove
    

def minimax(position, depth, maxPlayer, game):
    
    if maxPlayer:
        return maxi(position, game, depth)
    
    else:
        return mini(position, game, depth)
    



def simulateMove(piece, move, board, game, skip):
    
    x, y = move
    board.move(piece, x, y)
    
    if skip:
        board.remove(skip)
        
    return board    

def getAllMoves(board, color, game):
    
    moves = []
    allpiece = board.getAllPieces(color)  #get pieces
    
    for eachPiece in allpiece:
        allValidMoves = board.getValidMoves(eachPiece)   #get valid moves
        for move, skip in allValidMoves.items():
            newBoard = UpdateBoard(game, board, eachPiece, skip, move)
            moves.append(newBoard)
    
    return moves
            
    
def UpdateBoard(game, board, piece, skip, moveVal):

    board.draw(game.win)
    pygame.display.update()
    nBoard = deepcopy(board)
    pRow, pCol = piece.row, piece.col
    nPiece = nBoard.getPiece(pRow, pCol)
    
    return simulateMove(nPiece, moveVal, nBoard, game, skip)