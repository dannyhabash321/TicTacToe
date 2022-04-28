import random

# sets baord to intial state
def setBoard(board):
    for i in range(0,4):
        for j in range(0,4):
            board[i].append("___")

#stores the scores of each move for the ai model
def setBoardScores(board):
    for i in range(0,4):
        for j in range(0,4):
            board[i].append(0)  

#prints current state of the board
def printBoard():
    for i in range(0,4):
        for j in range(0,4):
            if j == 3:
                if i==3 and board[i][j] == "___":
                    print("   ", end="")
                else:
                    print (board[i][j], end="")
            else:
                if i==3 and board[i][j] == "___":
                    print("   |", end="")
                else:
                    print (board[i][j] + "|", end="")
        print()

#prints current state of the board
def printBoardScores():
    print("Current Placement Scores")
    for i in range(0,4):
        for j in range(0,4):
            print (boardScores[i][j], " ", end="")
        print()


#changes baord position to that of the player
def setPos(i, j, player):
    if board[i][j] == "___":
        if player == 1:
            board[i][j] = "_X_"
        if player == 2:
            board[i][j] = "_O_"
    else:
        return False


#checks for win level1
def checkLevel1Win(player1increase=0, player2increase=0):
    for i in range(0,4):
        #checks for all 
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][2] == board[i][3] and board[i][0] != "___":
            if board[i][0]== "_X_":
                print("Player 1 wins")
                player1increase=1
            elif board[i][0]== "_O_":
                print("Player 2 wins")
                player2increase=1
            return True, player1increase, player2increase
        elif board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[2][i] == board[3][i] and board[0][i] != "___":
            if board[0][i]== "_X_":
                print("Player 1 wins")
                player1increase=1
            elif board[0][i]== "_O_":
                print("Player 2 wins")
                player2increase=1
            return True, player1increase, player2increase
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] == board[3][3] and board[0][0] != "___":
        if board[0][0]== "_X_":
            print("Player 1 wins")
            player1increase=1
        elif board[0][0]== "_O_":
            print("Player 2 wins")
            player2increase=1
        return True, player1increase, player2increase
    elif board[0][3] == board[1][2] and board[1][2] == board[2][1] and board[2][1] == board[3][0] and board[0][3] != "___":
        if board[0][3]== "_X_":
            print("Player 1 wins")
            player1increase=1
        elif board[0][3]== "_O_":
            print("Player 2 wins")
            player2increase=1
        return True, player1increase, player2increase
    return False, player1increase, player2increase

#checks for merit wins and also scores the play
def checkLevel2Win(player1Score=0, player2Score=0):
    for i in range(0,4):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != "___":
            if board[i][0]== "_X_":
                player1Score+=3
            elif board[i][0]== "_O_":
                player2Score+=3
        if board[i][1] == board[i][2] and board[i][2] == board[i][3] and board[i][1] != "___":
            if board[i][1]== "_X_":
                player1Score+=3
            elif board[i][1]== "_O_":
                player2Score+=3
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != "___":
            if board[0][i]== "_X_":
                player1Score+=3
            elif board[0][i]== "_O_":
                player2Score+=3
        if board[1][i] == board[2][i] and board[2][i] == board[3][i] and board[1][i] != "___":
            if board[1][i]== "_X_":
                player1Score+=3
            elif board[1][i]== "_O_":
                player2Score+=3

    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != "___":
        if board[0][0]== "_X_":
            player1Score+=3
        elif board[0][0]== "_O_":
            player2Score+=3
    if board[1][1] == board[2][2] and board[2][2] == board[3][3] and board[1][1] != "___":
        if board[1][1]== "_X_":
            player1Score+=3
        elif board[1][1]== "_O_":
            player2Score+=3
    if board[0][3] == board[1][2] and board[1][2] == board[2][1] and board[0][3] != "___":
        if board[0][3]== "_X_":
            player1Score+=3
        elif board[0][3]== "_O_":
            player2Score+=3
    if board[1][2] == board[2][1] and board[2][1] == board[3][0] and board[1][2] != "___":
        if board[1][2]== "_X_":
            player1Score+=3
        elif board[1][2]== "_O_":
            player2Score+=3
    if board[0][1] == board[1][2] and board[1][2] == board[2][3] and board[0][1] != "___":
        if board[0][1]== "_X_":
            player1Score+=3
        elif board[0][1]== "_O_":
            player2Score+=3
    if board[1][0] == board[2][1] and board[2][1] == board[3][2] and board[1][0] != "___":
        if board[1][0]== "_X_":
            player1Score+=3
        elif board[1][0]== "_O_":
            player2Score+=3
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != "___":
        if board[0][2]== "_X_":
            player1Score+=3
        elif board[0][2]== "_O_":
            player2Score+=3
    if board[1][3] == board[2][2] and board[2][2] == board[3][1] and board[1][3] != "___":
        if board[1][3]== "_X_":
            player1Score+=3
        elif board[1][3]== "_O_":
            player2Score+=3
    return player1Score, player2Score

#R1
def makeWinningMove():
    for i in range(0,4):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] == "_O_"  and board[i][3]== "___":
            board[i][3]="_O_"
            return True
        if board[i][1] == board[i][2] and board[i][2] == board[i][3] and board[i][1] == "_O_" and board[i][0]== "___":
            board[i][0]="_O_"
            return True
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] == "_O_" and board[3][i]== "___":
            board[3][i]= "_O_"
            return True
        if board[1][i] == board[2][i] and board[2][i] == board[3][i] and board[1][i] == "_O_" and board[0][i]== "___":
            board[0][i]= "_O_"
            return True

    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == "_O_" and board[3][3]== "___":
        board[3][3]= "_O_"
        return True
    if board[1][1] == board[2][2] and board[2][2] == board[3][3] and board[1][1] == "_O_" and board[0][0]== "___":
        board[0][0]= "_O_"
        return True
    if board[0][3] == board[1][2] and board[1][2] == board[2][1] and board[0][3] == "_O_" and board[3][0]== "___":
        board[3][0]= "_O_"
        return True
    if board[1][2] == board[2][1] and board[2][1] == board[3][0] and board[1][2] == "_O_" and board[0][3]== "___":
        board[0][3]= "_O_"
        return True
    return False

#R2
def blockWinningMove():
    for i in range(0,4):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] == "_X_"  and board[i][3]== "___":
            board[i][3]="_O_"
            return True
        if board[i][1] == board[i][2] and board[i][2] == board[i][3] and board[i][1] == "_X_" and board[i][0]== "___":
            board[i][0]="_O_"
            return True
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] == "_X_" and board[3][i]== "___":
            board[3][i]= "_O_"
            return True
        if board[1][i] == board[2][i] and board[2][i] == board[3][i] and board[1][i] == "_X_" and board[0][i]== "___":
            board[0][i]= "_O_"
            return True

    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == "_X_" and board[3][3]== "___":
        board[3][3]= "_O_"
        return True
    if board[1][1] == board[2][2] and board[2][2] == board[3][3] and board[1][1] == "_X_" and board[0][0]== "___":
        board[0][0]= "_O_"
        return True
    if board[0][3] == board[1][2] and board[1][2] == board[2][1] and board[0][3] == "_X_" and board[3][0]== "___":
        board[3][0]= "_O_"
        return True
    if board[1][2] == board[2][1] and board[2][1] == board[3][0] and board[1][2] == "_X_" and board[0][3]== "___":
        board[0][3]= "_O_"
        return True
    
    return False

#R3
def makeMeritMove():
    for i in range(0,4):
        if board[i][0] == board[i][1] and board[i][0] == "_O_"  and board[i][2]== "___":
            board[i][2]="_O_"
            return True
        if board[i][3] == board[i][2] and board[i][3] == "_O_"  and board[i][1]== "___":
            board[i][1]="_O_"
            return True
        if board[i][1] == board[i][2] and board[i][1] == "_O_" and (board[i][0]== "___" or board[i][3]== "___" ):
            if board[i][0]== "___":
                board[i][0]="_O_"
            elif board[i][3]== "___":
                board[i][3]="_O_"
            return True
        if board[0][i] == board[1][i] and board[0][i] == "_O_"  and board[2][i]== "___":
            board[2][i]="_O_"
            return True
        if board[3][i] == board[2][i] and board[3][i] == "_O_"  and board[1][i]== "___":
            board[1][i]="_O_"
            return True
        if board[1][i] == board[2][i] and board[1][i] == "_O_" and (board[0][i]== "___" or board[3][i]== "___" ):
            if board[0][i]== "___":
                board[0][i]="_O_"
            elif board[3][i]== "___":
                board[3][i]="_O_"
            return True
   #diagonal conditions
    if board[0][0] == board[1][1] and board[0][0] == "_O_" and board[2][2]=="___":
        board[2][2]= "_O_"
        return True
    if board[2][2] == board[3][3] and board[2][2] == "_O_" and board[1][1]=="___":
        board[1][1]= "_O_"
        return True
    if board[1][1] == board[2][2] and board[1][1] == "_O_" and (board[0][0]=="___" or board[3][3]=="___"):
        if board[0][0]=="___":
            board[0][0]= "_O_"
        elif board[3][3]== "___":
            board[3][3]= "_O_"
        return True
    
    if board[0][3] == board[1][2] and board[0][3] == "_O_" and board[2][1]=="___":
        board[2][1]= "_O_"
        return True
    if board[3][0] == board[2][1] and board[3][0] == "_O_" and board[1][2]=="___":
        board[1][2]= "_O_"
        return True
    if board[1][2] == board[2][1] and board[1][2] == "_O_" and (board[0][3]=="___" or board[3][0]=="___"):
        if board[0][3]=="___":
            board[0][3]= "_O_"
        elif board[3][0]== "___":
            board[3][0]= "_O_"
        return True

    if board[0][1] == board[1][2] and board[0][1] == "_O_" and board[2][3]=="___":
        board[2][3]= "_O_"
        return True
    if board[0][2] == board[1][1] and board[0][2] == "_O_" and board[2][0]=="___":
        board[2][0]= "_O_"
        return True
    if board[3][1] == board[2][2] and board[3][1] == "_O_" and board[1][3]=="___":
        board[1][3]= "_O_"
        return True
    if board[3][2] == board[2][1] and board[3][2] == "_O_" and board[1][0]=="___":
        board[1][0]= "_O_"
        return True

    
    return False

#R4
def blockMeritMove():
    for i in range(0,4):
        if board[i][0] == board[i][1] and board[i][0] == "_X_"  and board[i][2]== "___":
            board[i][2]="_O_"
            return True
        if board[i][3] == board[i][2] and board[i][3] == "_X_"  and board[i][1]== "___":
            board[i][1]="_O_"
            return True
        if board[i][1] == board[i][2] and board[i][1] == "_X_" and (board[i][0]== "___" or board[i][3]== "___" ):
            if board[i][0]== "___":
                board[i][0]="_O_"
            elif board[i][3]== "___":
                board[i][3]="_O_"
            return True
        if board[0][i] == board[1][i] and board[0][i] == "_X_"  and board[2][i]== "___":
            board[2][i]="_O_"
            return True
        if board[3][i] == board[2][i] and board[3][i] == "_X_"  and board[1][i]== "___":
            board[1][i]="_O_"
            return True
        if board[1][i] == board[2][i] and board[1][i] == "_X_" and (board[0][i]== "___" or board[3][i]== "___" ):
            if board[0][i]== "___":
                board[0][i]="_O_"
            elif board[3][i]== "___":
                board[3][i]="_O_"
            return True
   #diagonal conditions
    if board[0][0] == board[1][1] and board[0][0] == "_X_" and board[2][2]=="___":
        board[2][2]= "_O_"
        return True
    if board[2][2] == board[3][3] and board[2][2] == "_X_" and board[1][1]=="___":
        board[1][1]= "_O_"
        return True
    if board[1][1] == board[2][2] and board[1][1] == "_X_" and (board[0][0]=="___" or board[3][3]=="___"):
        if board[0][0]=="___":
            board[0][0]= "_O_"
        elif board[3][3]== "___":
            board[3][3]= "_O_"
        return True
    
    if board[0][3] == board[1][2] and board[0][3] == "_X_" and board[2][1]=="___":
        board[2][1]= "_O_"
        return True
    if board[3][0] == board[2][1] and board[3][0] == "_X_" and board[1][2]=="___":
        board[1][2]= "_O_"
        return True
    if board[1][2] == board[2][1] and board[1][2] == "_X_" and (board[0][3]=="___" or board[3][0]=="___"):
        if board[0][3]=="___":
            board[0][3]= "_O_"
        elif board[3][0]== "___":
            board[3][0]= "_O_"
        return True

    if board[0][1] == board[1][2] and board[0][1] == "_X_" and board[2][3]=="___":
        board[2][3]= "_O_"
        return True
    if board[0][2] == board[1][1] and board[0][2] == "_X_" and board[2][0]=="___":
        board[2][0]= "_O_"
        return True
    if board[3][1] == board[2][2] and board[3][1] == "_X_" and board[1][3]=="___":
        board[1][3]= "_O_"
        return True
    if board[3][2] == board[2][1] and board[3][2] == "_X_" and board[1][0]=="___":
        board[1][0]= "_O_"
        return True
    return False


#R5
def makeRandomMove():
    i = random.randint(0,3)
    j = random.randint(0,3)

    while board[i][j] != "___":
        i = random.randint(0,3)
        j = random.randint(0,3)
    board[i][j] = "_O_"

#human model runs functions based on the project requirements
def humanModel():
    if makeWinningMove() == False:
        if blockWinningMove() == False:
            if makeMeritMove() == False:
                if blockMeritMove() == False:
                    makeRandomMove()







# #algorithm to check surrounding neighbors for an X so the AI can make a scoring system
def checkNeighbors(i,j):
    try:
        if board[i][j-1]=="_X_" and i >=0 and i < 4 and j >0 and j < 4: 
            boardScores[i][j]+=1
    except IndexError:
        pass
    try:
        if board[i-1][j-1]=="_X_" and i >0 and i < 4 and j >0 and j < 4:
            boardScores[i][j]+=1
    except IndexError:
        pass
    try:
        if board[i+1][j-1]=="_X_" and i >=0 and i < 3 and j >0 and j < 4:
            boardScores[i][j]+=1
    except IndexError:
        pass
    try:
        if board[i-1][j]=="_X_" and i >0 and i < 4 and j >=0 and j < 4:
            boardScores[i][j]+=1
    except IndexError:
        pass
    try:
        if board[i+1][j]=="_X_" and i >=0 and i < 3 and j >=0 and j < 4:
            boardScores[i][j]+=1
    except IndexError:
        pass
    try:
        if board[i][j+1]=="_X_" and i >=0 and i < 4 and j >=0 and j < 3:
            boardScores[i][j]+=1
    except IndexError:
        pass
    try:
        if board[i-1][j+1]=="_X_" and i >0 and i < 4 and j >=0 and j < 3:
            boardScores[i][j]+=1
    except IndexError:
        pass
    try:
        if board[i+1][j+1]=="_X_" and i >=0 and i < 3 and j >=0 and j < 3:
            boardScores[i][j]+=1
    except IndexError:
        pass
    



#this scores a merit move to 25 
def ScoreMeritMove():
    for i in range(0,4):
        if board[i][0] == board[i][1] and board[i][0] == "_X_"  and board[i][2]== "___":
            boardScores[i][2]+=25
            return True
        if board[i][3] == board[i][2] and board[i][3] == "_X_"  and board[i][1]== "___":
            boardScores[i][1]+=25
            return True
        if board[i][1] == board[i][2] and board[i][1] == "_X_" and (board[i][0]== "___" or board[i][3]== "___" ):
            if board[i][0]== "___":
                boardScores[i][0]+=25
            elif board[i][3]== "___":
                boardScores[i][3]+=25
            return True
        if board[0][i] == board[1][i] and board[0][i] == "_X_"  and board[2][i]== "___":
            boardScores[2][i]+=25
            return True
        if board[3][i] == board[2][i] and board[3][i] == "_X_"  and board[1][i]== "___":
            boardScores[1][i]+=25
            return True
        if board[1][i] == board[2][i] and board[1][i] == "_X_" and (board[0][i]== "___" or board[3][i]== "___" ):
            if board[0][i]== "___":
                boardScores[0][i]+=25
            elif board[3][i]== "___":
                boardScores[3][i]+=25
            return True
   #diagonal conditions
    if board[0][0] == board[1][1] and board[0][0] == "_X_" and board[2][2]=="___":
        boardScores[2][2]+=25
        return True
    if board[2][2] == board[3][3] and board[2][2] == "_X_" and board[1][1]=="___":
        boardScores[1][1]+=25
        return True
    if board[1][1] == board[2][2] and board[1][1] == "_X_" and (board[0][0]=="___" or board[3][3]=="___"):
        if board[0][0]=="___":
            boardScores[0][0]+=25
        elif board[3][3]== "___":
            boardScores[3][3]+=25
        return True
    
    if board[0][3] == board[1][2] and board[0][3] == "_O_" and board[2][1]=="___":
        boardScores[2][1]+=25
        return True
    if board[3][0] == board[2][1] and board[3][0] == "_O_" and board[1][2]=="___":
        boardScores[1][2]+=25
        return True
    if board[1][2] == board[2][1] and board[1][2] == "_O_" and (board[0][3]=="___" or board[3][0]=="___"):
        if board[0][3]=="___":
            boardScores[0][3]+=25
        elif board[3][0]== "___":
            boardScores[3][0]+=25
        return True

    if board[0][1] == board[1][2] and board[0][1] == "_O_" and board[2][3]=="___":
        boardScores[2][3]+=25
        return True
    if board[0][2] == board[1][1] and board[0][2] == "_O_" and board[2][0]=="___":
        boardScores[2][0]+=25
        return True
    if board[3][1] == board[2][2] and board[3][1] == "_O_" and board[1][3]=="___":
        boardScores[1][3]+=25
        return True
    if board[3][2] == board[2][1] and board[3][2] == "_O_" and board[1][0]=="___":
        boardScores[1][0]+=25
        return True
    return False


def scoreBlockingMeritMove():
    for i in range(0,4):
        if board[i][0] == board[i][1] and board[i][0] == "_O_"  and board[i][2]== "___":
            boardScores[i][2]+=20
            return True
        if board[i][3] == board[i][2] and board[i][3] == "_O_"  and board[i][1]== "___":
            boardScores[i][1]+=20
            return True
        if board[i][1] == board[i][2] and board[i][1] == "_O_" and (board[i][0]== "___" or board[i][3]== "___" ):
            if board[i][0]== "___":
                boardScores[i][0]+=20
            elif board[i][3]== "___":
                boardScores[i][3]+=20
            return True
        if board[0][i] == board[1][i] and board[0][i] == "_O_"  and board[2][i]== "___":
            boardScores[2][i]+=20
            return True
        if board[3][i] == board[2][i] and board[3][i] == "_O_"  and board[1][i]== "___":
            boardScores[1][i]+=20
            return True
        if board[1][i] == board[2][i] and board[1][i] == "_O_" and (board[0][i]== "___" or board[3][i]== "___" ):
            if board[0][i]== "___":
                boardScores[0][i]+=20
            elif board[3][i]== "___":
                boardScores[3][i]+=20
            return True
   #diagonal conditions
    if board[0][0] == board[1][1] and board[0][0] == "_O_" and board[2][2]=="___":
        boardScores[2][2]+=20
        return True
    if board[2][2] == board[3][3] and board[2][2] == "_O_" and board[1][1]=="___":
        boardScores[1][1]+=20
        return True
    if board[1][1] == board[2][2] and board[1][1] == "_O_" and (board[0][0]=="___" or board[3][3]=="___"):
        if board[0][0]=="___":
            boardScores[0][0]+=20
        elif board[3][3]== "___":
            boardScores[3][3]+=20
        return True
    
    if board[0][3] == board[1][2] and board[0][3] == "_O_" and board[2][1]=="___":
        boardScores[2][1]+=20
        return True
    if board[3][0] == board[2][1] and board[3][0] == "_O_" and board[1][2]=="___":
        boardScores[1][2]+=20
        return True
    if board[1][2] == board[2][1] and board[1][2] == "_O_" and (board[0][3]=="___" or board[3][0]=="___"):
        if board[0][3]=="___":
            boardScores[0][3]+=20
        elif board[3][0]== "___":
            boardScores[3][0]+=20
        return True

    if board[0][1] == board[1][2] and board[0][1] == "_O_" and board[2][3]=="___":
        boardScores[2][3]+=20
        return True
    if board[0][2] == board[1][1] and board[0][2] == "_O_" and board[2][0]=="___":
        boardScores[2][0]+=20
        return True
    if board[3][1] == board[2][2] and board[3][1] == "_O_" and board[1][3]=="___":
        boardScores[1][3]+=20
        return True
    if board[3][2] == board[2][1] and board[3][2] == "_O_" and board[1][0]=="___":
        boardScores[1][0]+=20
        return True

    
    return False

#function to set a really high score for an opposing winning move so that the game continues
def scoreWinningMove():
    for i in range(0,4):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] == "_X_"  and board[i][3]== "___":
            boardScores[i][3]+=100
            return True
        if board[i][1] == board[i][2] and board[i][2] == board[i][3] and board[i][1] == "_X_" and board[i][0]== "___":
            boardScores[i][0]+=100
            return True
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] == "_X_" and board[3][i]== "___":
            boardScores[3][i]+= 100
            return True
        if board[1][i] == board[2][i] and board[2][i] == board[3][i] and board[1][i] == "_X_" and board[0][i]== "___":
            boardScores[0][i]+= 100
            return True

    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == "_X_" and board[3][3]== "___":
        boardScores[3][3]+= 100
        return True
    if board[1][1] == board[2][2] and board[2][2] == board[3][3] and board[1][1] == "_X_" and board[0][0]== "___":
        boardScores[0][0]+= 100
        return True
    if board[0][3] == board[1][2] and board[1][2] == board[2][1] and board[0][3] == "_X_" and board[3][0]== "___":
        boardScores[3][0]+= 100
        return True
    if board[1][2] == board[2][1] and board[2][1] == board[3][0] and board[1][2] == "_X_" and board[0][3]== "___":
        boardScores[0][3]+= 100
        return True
    return False

#function to set a really high score for an opposing winning move so that the game continues
def scoreBlockingMove():
    for i in range(0,4):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] == "_O_"  and board[i][3]== "___":
            boardScores[i][3]+=50
            return True
        if board[i][1] == board[i][2] and board[i][2] == board[i][3] and board[i][1] == "_O_" and board[i][0]== "___":
            boardScores[i][0]+=50
            return True
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] == "_O_" and board[3][i]== "___":
            boardScores[3][i]+= 50
            return True
        if board[1][i] == board[2][i] and board[2][i] == board[3][i] and board[1][i] == "_O_" and board[0][i]== "___":
            boardScores[0][i]+= 50
            return True

    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == "_O_" and board[3][3]== "___":
        boardScores[3][3]+= 50
        return True
    if board[1][1] == board[2][2] and board[2][2] == board[3][3] and board[1][1] == "_O_" and board[0][0]== "___":
        boardScores[0][0]+= 50
        return True
    if board[0][3] == board[1][2] and board[1][2] == board[2][1] and board[0][3] == "_O_" and board[3][0]== "___":
        boardScores[3][0]+= 50
        return True
    if board[1][2] == board[2][1] and board[2][1] == board[3][0] and board[1][2] == "_O_" and board[0][3]== "___":
        boardScores[0][3]+= 50
        return True
    return False


#computes the scores for each move
def scoreMoves():
    for i in range(0,4):
        for j in range(0,4):
            if board[i][j] == "___":
                checkNeighbors(i,j)

#finds the heighest score within the score board and sets an X there for the ai
def makeHeighestScoreMove():
    mx=0
    indexList=[[1,1]]
    for i in range(0,4):
        for j in range(0,4):
            if boardScores[i][j]>=mx and board[i][j]=="___":
                mx= boardScores[i][j]
                indexList.append([i,j])
    for i in range(len(indexList)-1, -1, -1):
        if board[indexList[i][0]][indexList[i][1]] == "___":
            board[indexList[i][0]][indexList[i][1]] = "_X_"
            # boardScores[indexList[i][0]][indexList[i][1]]=0
            return
    
#ai model that runs other functions in order
def aiModel():
    scoreMoves()
    ScoreMeritMove()
    scoreWinningMove()
    scoreBlockingMove()
    scoreBlockingMeritMove()
    makeHeighestScoreMove()
    printBoardScores()


#to store stats for the 100 games to be played
player1Wins=0
player2Wins=0
ties=0


# main code simulation to run 100 time for the game
for l in range(100):
    print("Game: ", l+1)
    #reset all variables to normal for new game
    board = [[],[],[],[]]
    boardScores = [[],[],[],[]]
    setBoardScores(boardScores)
    setBoard(board)
    player1Inc=0
    player2Inc=0
    moveNumber=1
    #play 8 times and one move per player so 16 moves total
    for i in range(8):
        moveNumber+=1
        aiModel()
        print("Player 1 Move Number:", moveNumber)
        printBoard()
        replay, player1Inc, player2Inc = checkLevel1Win()
        if replay==True:
            break
        
        print("Player 2 Move Number:", moveNumber+1)
        moveNumber+=1
        humanModel()
        printBoard()
        replay, player1Inc, player2Inc = checkLevel1Win()
        if replay == True:
            break

    print("Final State (game",l+1,")")
    printBoard()
    checkLevel2Win()
    player1Score, player2Score = checkLevel2Win()
    print("Player 1(X):", player1Score)
    print("Player 2(O):", player2Score)
    if replay==False:
        if player1Score > player2Score:
            player1Wins+=1
        elif player2Score > player1Score:
            player2Wins+=1
        else:
            ties+=1
    else:
        player1Wins+=player1Inc
        player2Wins+=player2Inc



print("Player 1 Wins:", player1Wins)
print("Player 2 Wins:", player2Wins)
print("Ties:", ties)

