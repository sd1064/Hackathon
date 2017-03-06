from Constants.constants import constants

class board:
    # mine="-M-"
    # empty="-O-"
    board=[]

    def __init__(self):
        pass

    def generate(self,rows):
        self.board=[]
        for i in range(0,rows):
            row=[]
            for i in range(0,rows):
                row.append(constants.EMPTY)
            self.board.append(row)

    def addMine(self,row,col):
        self.board[row][col]=constants.MINE
        
    def scanForMine(self,row,col):
        toReturn = []
        toReturn.append(self.checkPosition(row+1,col))
        toReturn.append(self.checkPosition(row+1,col-1))
        toReturn.append(self.checkPosition(row+1,col+1))
        toReturn.append(self.checkPosition(row,col-1))
        toReturn.append(self.checkPosition(row,col+1))
        return toReturn

    def checkPosition(self,row,col):
        if self.board[row][col]==constants.MINE:
            return [row,col,constants.MINE]
        elif self.board[row][col]==constants.EMPTY:
            return [row,col,constants.EMPTY]

        #if outofbounds return

    def printBoardNoFogOfWar(self):
        for i in range(0,len(self.board)):
            print self.board[i]
        print "\n"
