# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import random







def quizrobotics():
  print("okay, i got 3 multiple choice questions about the laws of robotics.")
  aa = "A robot may not injure a human being or, through inaction, allow a human being to come to harm."
  ba = "A robot must obey the orders given it by human beings except where such orders would conflict with the First Law."
  ca = "A robot must protect its own existence as long as such protection does not conflict with the First or Second Laws."
  ab =  "A robot may not injure a human being, allow a human being to come to harm unless it's nanomachines which alters the DNA structure."
  ac = "A robot may injure a human being, but cannot allow a human being to come to harm unless it comes out from this dilemma"
  bb =  "A robot must obey the orders given it by human beings and always calls them 'my master' except where such orders would conflict with the laws of natual gravity."
  bc =  "A robot must obey the orders given it by animals except where such orders given in any known human language."
  cb =  "A robot must always protect Rotal as long as such protection does not conflict with the First or Second Laws of Feminism."
  cc = "A robot must protect its own existence by multiplying continuously until such protection does not conflict with the First or Second Laws."


  print("a", aa)
  print("b", ab)
  print("c", ac)

  choice = input("")
  while choice :
    if choice in ["a", "A"]:
      print("Thats correct")
      break
    else:# choice in ["b", "B","c","C"]:
     print("thats wrong.")
     break


  print("Okay, next question")
  print("a", ba)
  print("b", bb)
  print("c", bc)
  choice2 = input("")
  while choice2:
       if choice2 in ["a","A"]:
          print("Thats correct")
          break
       elif choice2 in ["b", "B","c","C"]:
          print("Thats wrong.")
          break


  print("last one.")
  print("a", ca)
  print("b", cb)
  print("c", cc)
  choice3 = input("")
  while choice3:
       if choice3 in ["a","A"]:
          print("Thats correct")
          break
       elif choice3 in ["b", "B","c","C"]:
          print("Thats wrong.")
          break

  return

def RPS():
    print ("Goodluck beating me with this one... Im a Rock...")
    comp_possible  = 1,2,3
    score = [0,0]
    flag = 0
    while True:
        print("Enter your choice:")
        while True:
            choice = input('->')
            if choice == 'r' or choice == 'R' or choice == 'Rock' or choice == 'rock' or choice == '1':
                choice_identifier  = 1
                break
            elif choice == 'S' or choice == 's' or choice == 'Scissors' or choice == 'sciccors' or choice == '2':
                choice_identifier =  2
                break
            elif choice == 'P' or choice == 'p' or choice == 'Paper' or choice == 'paper' or choice == '3':
                choice_identifier =  3
                break
            else:
                print('That\'s not an option in this game :)')
                print('Try again:')
                continue

        comp_choice = random.choice(comp_possible)
        if choice_identifier == comp_choice:
            print('It\'s a draw!')
            score[0] = score[0] + 1
            score[1] = score[1] + 1
        elif (choice_identifier == 1 and comp_choice == 2) or (choice_identifier == 2 and comp_choice == 3) or (choice_identifier == 3 and comp_choice == 1):
            print('You win!')
            score[0] = score[0] + 1
        else:
            print('You lose...')
            score[1] = score[1] + 1


        while True:
            answer = input('Play another round?')
            if answer == 'y' or answer == 'Y' or answer == 'yes' or answer == 'Yes' or answer == 'ye' or answer == 'Ye' or answer == 'sure' or answer == 'Sure':
                print(' Current score: You - ',score[0],' Computer - ',  score[1])
                flag = 0
                break
            elif answer == 'n' or answer == 'N' or answer == 'no' or answer == 'No' or answer == 'nah' or answer == 'Nah':
                print('Thanks for playing! Final score: You - ',score[0],' Computer - ',  score[1])
                flag = 1
                break
            else:
                print('Yay or nay...')
                continue
        if flag == 0:
            continue
        else:
            break
    return

def drawBoard(board):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def ttc():
 def inputPlayerLetter():
    # Lets the player type which letter they want to be.
    # Returns a list with the player's letter as the first item, and the computer's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # the first element in the tuple is the player's letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

 def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

 def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

 def makeMove(board, letter, move):
    board[move] = letter

 def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

 def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

 def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '

 def getPlayerMove(board):
    # Let the player type in his move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

 def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

 def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # Check if the player could win on his next move, and block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

 def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


 print('Welcome to Tic Tac Toe!')

 while True:
    # Reset the board
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # Player's turn.
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            # Computer's turn.
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break

 return
