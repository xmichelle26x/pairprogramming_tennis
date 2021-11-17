
points = 0
playerOne = 0
playerTwo = 0

point = [0,15,30,40]

# playerOne = {
#     "zero": 0,
#     "fifteen":15,
#     "thirty":30,
#     "forty":40,
#     "name": "playerOne"
# }

# playerTwo= {
#     "zero": 0,
#     "fifteen":15,
#     "thirty":30,
#     "forty":40,
#     "name": "playerTwo"
# } 

def sumpoints():
    if playerOne == 0 and playerTwo == 0:
        print("PlayerOne {0} PlayerTwo {1}".format(playerOne, playerTwo)) 
    if playerOne == 30 and playerTwo == 15:
        print("PlayerOne {0} PlayerTwo {1}".format(playerOne, playerTwo)) 
    if playerOne == 40 and playerTwo == 40:
        print("Deuce") 
    if playerOne == 41 and playerTwo == 40:
        print("Advantage PlayerOne")
    if playerOne == 40 and playerTwo == 41:
        print("Advantage PlayerTwo")
    if playerOne == 40 and playerTwo == 42:
        print("PlayerTwo wins")
    
(sumpoints())