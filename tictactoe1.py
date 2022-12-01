# Крестики - нолики

import random

def drawBoard(board):
    # Эта функция выводит на экран игровое поле, клетки которого будут заполняться.
    
    # "board" - это список из 10 строк, для прорисовки игрового поля(индекс 0 игнорируется).
    print(board[7] + '|' + board[8] + '|' + board [9])
    print ('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print ('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def inputPlayerLetter():
    # Разрешение игроку ввести букву, которую он выбирает.
    # Возвращает список, в котором буква игрока - первый элемент, а буква компьютера - второй.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Вы выбираете X или O')
        letter = input().upper()
       
    # Первым элементом списка является буква игрока, вторым - буква компьютера.
    if letter == 'X':
        return['X', 'O']
    else:
        return ['O', 'X']
        
def whoGoesFirst():
    # Случайный выбор игрока, который ходит первым.
    if random.randint(0, 1) == 0:
        return 'Компьютер'
    else:
        return 'Человек'
    
def makeMove(board, letter, move):
    board[move] = letter
    
def isWinner(bo, Le):
    # Учитывая заполнение игрового поля и буквы игрока, эта функция возвращает Ttrue, если игрок выиграл.
    # Мы используем "bo" вместо "board" и "le" вместо "letter", поэтому нам нужно много печатать
    return ((bo[7] == Le and bo[8] == Le and bo[9] == Le) or # across the top
    (bo[4] == Le and bo[5] == Le and bo[6] == Le) or # через центр
    (bo[1] == Le and bo[2] == Le and bo[3] == Le) or # через низ
    (bo[7] == Le and bo[4] == Le and bo[1] == Le) or # вниз по левой стороне
    (bo[8] == Le and bo[5] == Le and bo[2] == Le) or # вниз по центру
    (bo[9] == Le and bo[6] == Le and bo[3] == Le) or # вниз по правой стороне
    (bo[7] == Le and bo[5] == Le and bo[3] == Le) or # по диагонали
    (bo[9] == Le and bo[5] == Le and bo[1] == Le)) # по диагонали

def getBoardCopy(board):
    #Создает копию игрового поля и возвращает его.
    boardCopy =[]
    for i in board:
        boardCopy.append(i)
    return boardCopy
    
def isSpaceFree(board, move):
    # Возвращает True, если сделан ход в свободную клетку.
    return board [move] == ' '

def getPlayerMove (board):
    #Разрешение игроку сделать ход.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('Ваш следующий ход? (1-9)')
        move = input ()
    return int (move)
    
def chooseRandomMoveFromList(board, moveList):
    #Возвращает допустимый ход, учитывая список сделанных ходов и список заполненных клеток.
    #Возвращает значение None, если больше нет допустимых ходов.
    possibleMoves = []
    for i in moveList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
            
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    # Учитывая заполнение игрового поля и букву компьютера, определяет допустимый ход и возвращает его.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
        
    # Это алгоритм для ИИ "Крестиков - Ноликов":
    # Сначала проверяем - победим ли мы, сделав следующий ход.
    for i in range(1,10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                  return i
                
      # Проверяем - победит ли игрок, сделав следующий ход, и блокируем его.
        for i in range(1, 10):
            boardCopy = getBoardCopy(board)
            if isSpaceFree(boardCopy, i):
                makeMove(boardCopy, playerLetter, i)
                if isWinner(boardCopy, playerLetter):
                    return i
                
    # Пробуем занять один из углов, если есть свободные.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
     
    # Пробуем занять центр, если он свободен.
    if isSpaceFree(board, 5):
        return 5
     
    # Делаем ход по одной стороне.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])
 
def isBoardFull(board):
    # Возвращает True, если клетка на игровом поле занята. В противном случае, возвращает False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print('Игра "Крестики - нолики"')

while True:
    # Перезагрузка игрового поля
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('' + turn + 'ходит первым.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'Человек':
            # Ход игрока.
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Ура! Вы выиграли!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Ничья!')
                    break
                else:
                    turn = 'Компьютер'
                
        else:
            # Ход компьютера.
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
         
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('Компьютер победил! Вы проиграли.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Ничья!')
                    break
                else:
                    turn = 'Человек'
            
    print('Сыграем еще раз? (да или нет)')
    if not input().lower().startswith('д'):
        break
                
            
           
           
   
