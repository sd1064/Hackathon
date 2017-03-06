# current position
# known locations
# print current board
# move
import time
from Constants.constants import constants

class player:
    currentPosition = [0,0]
    knownLocations  = [] #[[ROW,COL,TYPE]]
    board=[]
    DECIDE_TIME = 3

    def __init__(self,board,DECIDE_TIME):
        self.board=board
        self.currentPosition[1]=int(len(board.board)/2)
        self.DECIDE_TIME = DECIDE_TIME

    def printCurrentBoard(self):
        fogOfWarBoard=[]
        for i in range(0,len(self.board.board)):
            row=[]
            for i in range(0,len(self.board.board)):
                row.append(constants.UNKNOWN)
            fogOfWarBoard.append(row)

        for i in range(0,len(self.knownLocations)):
            fogOfWarBoard[self.knownLocations[i][0]][self.knownLocations[i][1]]=self.knownLocations[i][2]
        fogOfWarBoard[self.currentPosition[0]][self.currentPosition[1]]=constants.PLAYER
        print "\n"
        for i in range(0,len(fogOfWarBoard)):
            print fogOfWarBoard[i]
        print "\n"

    def scanForMine(self):
        self.knownLocations = self.knownLocations + self.board.scanForMine(self.currentPosition[0],self.currentPosition[1])


    def decideMove(self):
		#Logic for deciding move based on situation

    def check_valid_move(self,move):
        #check move not out of bounds
		#check move doesnt activate mines

    def move(self,moveType):
	#IMPLEMENT MOVE FORWARD,LEFT,RIGHT
