from Board.board         import board
from Generator.generator import generator
from Player.player       import player
from Constants.constants import constants

#BOARD TESTING

ROW_NUM  = 10
MINE_NUM = 10
LAY_TIME = 10
DECIDE_TIME = 5
'''
playing = True

while playing==True:
    escape=False
    counter = 0
    myBoard = board()
    myBoard.generate(ROW_NUM)

    myMineGenerator = generator(MINE_NUM,myBoard,LAY_TIME)
    if myMineGenerator.LayMines() == False:
        print "FAILED TO LAY MINES"
        break
    myPlayer = player(myBoard,DECIDE_TIME)
    while (counter<ROW_NUM and escape==False):
        if counter==(ROW_NUM-1):
            print "YOU WIN"
            playing=False
            escape=True
            counter=ROW_NUM+10
        elif (counter<ROW_NUM):
            myPlayer.scanForMine()
            x = myPlayer.decideMove()
            if x == False:
                print "YOU BLEW UP"
                playing=False
                escape=True
            counter=counter+1
            myPlayer.printCurrentBoard()
'''