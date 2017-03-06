import time
from Constants.constants import constants

class generator:

    MINE_NUM = 0
    LAY_TIME=15

    def __init__(self,MINE_NUM,board,LAY_TIME):
        self.MINE_NUM = MINE_NUM
        self.board=board
        self.LAY_TIME = LAY_TIME

    def LayMines(self):
	#LAY THE MINES ON THE BOARD
	'''
        t_end = time.time() + self.LAY_TIME
        finished=False
        while time.time() < t_end and finished==False:
            for x in range(0,(self.MINE_NUM)):
                trys=3
                if trys==0:
                    return False
                else:
                    ############### MODIFY ##################
                    row=x
                    col=x
                    ############## MODIFY ##################
                    if self.check_valid_mine(row,col):
                        self.board.addMine(1,1)
                    else:
                        trys=trys-1
            self.board.printBoardNoFogOfWar()
            finished = True
            return True
'''
    def check_valid_mine(self,row,col):
        #check above,left,rigt,below for mines
        #check not out of bounds
        #return True
