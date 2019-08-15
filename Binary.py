#This code solves a given binary puzzle
#By using logic: 1s or 0s next to "00" or "11", 1s or 0s between "0?0" or "1?1"
#Or if logic fails, by filling in a random number and testing the logic again
#If the board is full and isn't solved, it resets the board and tries again
#Thus eventually computing the solution
#Predefined numbers: Numbers the user already knows

import sys
from random import randint

board = []
width_board = 0

total_predef_numb = 0
predef_numb = []

x = []
y = []

switch = False

none_in_board = False

solved_list = []
vert_list = []

solved = False

def create_board():
  #Creates the board
  global board
  global board_copy
  global width_board

  while width_board % 2 != 0 or width_board <= 0:
    width_board = input("Width of the board? ")
    if width_board != "":
      width_board = int(width_board)
      if width_board <= 0:
        print ("")
        print ("Enter a value higher than 0!")
        print ("")
      elif width_board % 2 != 0:
        print ("")
        print ("Enter a value that is dividable by 2!")
        print ("")
    else:
      print ("")
      print ("Enter a value!")
      print ("")
      width_board = 0
    
  
  for i in range(width_board):
    board.append([])
  for i in range(width_board):
    for a in range(width_board):
      board[i].append(None)

def print_board():
  #Prints the board line by line
  for i in range(width_board):
    print (board[i])
  print ("")


def ini_predef_num():
  #Initialises predefined numbers
  global board
  global predef_numb
  global total_predef_numb
  global x
  global y
  
  #Asks for the total of predef num and what they are
  total_predef_numb = (width_board * width_board) + 1
  
  while total_predef_numb > (width_board * width_board):
    total_predef_numb = input("Total of predefined numbers? ")
    if total_predef_numb != "":
      total_predef_numb = int(total_predef_numb)
      if total_predef_numb > (width_board * width_board):
        print ("")
        print ("Enter a value that is not higher than the amount of places on the board!")
        print ("")
    else:
      print ("")
      print ("Enter a value!")
      print ("")
      total_predef_numb = (width_board * width_board) + 1
      
  for i in range(total_predef_numb):
    numb = 2
    while numb != 1 and numb != 0:
      numb = input("Predefined number " + str(int(i) + 1) + " (0/1): ")
      if numb != "":
        numb = int(numb)
        if numb == 0 or numb == 1:
          predef_numb.append(numb)
        else:
          print ("")
          print ("Enter 0 or 1!")
          print ("")
          numb = 2
      else:
        print ("")
        print ("Enter 0 or 1!")
        print ("")
        numb = 2
      
  print ("")

  #Asks, in order, where the predef num are located
  for i in range(total_predef_numb):
    x_co = -1
    while x_co < 0 or x_co >= (width_board * width_board):
      x_co = input("X co-ordinate of predefined number " + str(int(i + 1)) + ": ")
      if x_co != "":
        x_co = int(x_co) - 1
        if x_co < 0 or x_co >= (width_board):
          print ("")
          print ("Enter an x-coordinate that is on the board!")
          print ("")
          x_co = -1
        else:
          x.append(x_co)
      else:
        print ("")
        print ("Enter an x-coordinate that is on the board!")
        print ("")
        x_co = -1

    y_co = -1
    while y_co < 0 or y_co >= (width_board * width_board):
      y_co = input("Y co-ordinate of predefined number " + str(int(i + 1)) + ": ")
      if y_co != "":
        y_co = int(y_co) - 1
        if y_co < 0 or y_co >= (width_board):
          print ("")
          print ("Enter an y-coordinate that is on the board!")
          print ("")
          y_co = -1
        else:
          y.append(y_co)
      else:
        print ("")
        print ("Enter an y-coordinate that is on the board!")
        print ("")
        y_co = -1
      

    board[x[i]][y[i]] = predef_numb[i]
    print ("")

def reset_board():
  #Resets the board (clears the board of any numbers the program filled in)
  global board
  global predef_numb

  board.clear()
  for i in range(width_board):
    board.append([])
  for i in range(width_board):
    for a in range(width_board):
      board[i].append(None)
      
  #Resets the predef numbers
  for i in range(total_predef_numb):
    board[x[i]][y[i]] = predef_numb[int(i)]


def test_double_hor():
  #Looks for "00" or "11" horizontally and puts the opposite number beside them
  global board
  global switch
  
  switch = False
  
  for x in range(width_board):
    for y in range(width_board - 1):
      if board[x][y] == 0 and board[x][y + 1] == 0:
          if y == 0:
            if board[x][y + 2] != 1:
              board[x][y + 2] = 1
              switch = True
          elif (y + 2) == (width_board):
            if board[x][y - 1] != 1:
              board[x][y - 1] = 1
              switch = True
          else:
            if board[x][y - 1] != 1 or board[x][y + 2] != 1:
              board[x][y - 1] = 1
              board[x][y + 2] = 1
              switch = True
          
      elif board[x][y] == 1 and board[x][y + 1] == 1:
          if y == 0:
            if board[x][y + 2] != 0:
              board[x][y + 2] = 0
              switch = True
          elif (y + 2) == (width_board):
            if board[x][y - 1] != 0:
              board[x][y - 1] = 0
              switch = True
          else:
            if board[x][y - 1] != 0 or board[x][y + 2] != 0:
              board[x][y - 1] = 0
              board[x][y + 2] = 0
              switch = True

      


def test_double_vert():
  #Looks for "00" and "11" vertically and puts the opposite number beside them
  global board
  global switch
  
  for y in range(width_board):  
    for x in range(width_board - 1):
      if board[x][y] == 0 and board[x + 1][y] == 0:
        if x == 0:
          if board[x + 2][y] != 1:
            board[x + 2][y] = 1
            switch = True
        elif (x + 2) == width_board:
          if board[x - 1][y] != 1:
            board[x - 1][y] = 1
            switch = True
        else:
          if board[x - 1][y] != 1 or board[x + 2][y] != 1:
            board[x - 1][y] = 1
            board[x + 2][y] = 1
            switch = True

      elif board[x][y] == 1 and board[x + 1][y] == 1:
        if x == 0:
          if board[x + 2][y] != 0:
            board[x + 2][y] = 0
            switch = True
        elif (x + 2) == width_board:
          if board[x - 1][y] != 0:
            board[x - 1][y] = 0
            switch = True
        else:
          if board[x - 1][y] != 0 or board[x + 2][y] != 0:
            board[x - 1][y] = 0
            board[x + 2][y] = 0
            switch = True
    

def test_triple_hor():
  #Looks for "0?0" or "1?1" horizontally and fills in the opposite number between them
  global board
  global switch
  
  for x in range(width_board):
    for y in range(width_board - 2):
      if board[x][y] == 0 and board[x][y + 2] == 0:
        if board[x][y + 1] != 1:
          board [x][y + 1] = 1
          switch = True
      elif board[x][y] == 1 and board[x][y + 2] == 1:
        if board[x][y + 1] != 0:
          board [x][y + 1] = 0
          switch = True

def test_triple_vert():
  #Looks for "0?0" or "1?1" vertically and fills in the opposite number between them
  global board
  global switch
  
  for y in range(width_board):
    for x in range(width_board - 2):
      if board[x][y] == 0 and board[x + 2][y] == 0:
        if board[x + 1][y] != 1:
          board[x + 1][y] = 1
          switch = True
      elif board[x][y] == 1 and board[x + 2][y] == 1:
        if board[x + 1][y] != 0:
          board[x + 1][y] = 0 
          switch = True


def max_num_hor():
  #Looks if the max num of 0s and 1s has been reached horizontally
  global board
  global switch
  
  for x in range(width_board):
    if board[x].count(0) == (width_board / 2):
      for y in range(width_board):
        if board[x][y] == None:
          board[x][y] = 1
          switch = True
    elif board[x].count(1) == (width_board / 2):
      for y in range(width_board):
        if board[x][y] == None:
          board[x][y] = 0
          switch = True
    elif board[x].count(0) > (width_board / 2) or board[x].count(0) > (width_board / 2):
      if None not in board[x]:
        reset_board()


def max_num_vert():
  #Looks if the max num of 0s and 1s has been reached vertically
  global board
  global switch
  
  num_list = []
        
  for y in range(width_board):
    for x in range(width_board):
      num_list.append(board[x][y])
      
    if num_list.count(0) == (width_board / 2):
      for x in range(width_board):
        if board[x][y] == None:
          board[x][y] = 1
          switch = True
    elif num_list.count(1) == (width_board / 2):
      for x in range(width_board):
        if board[x][y] == None:
          board[x][y] = 0
          switch = True
    elif num_list.count(0) > (width_board / 2) or num_list.count(0) > (width_board / 2):
      if None not in num_list:
        reset_board()
      
    num_list.clear()


def count_none():
  #Counts how many 'None's there are left in the board
  global none_in_board
  
  none_in_board = False
  for i in range(width_board):
    if None in board[i]:
      none_in_board = True


def random_num():
  #If the board isn't filled in, fill in a 0/1 in a spot that hasn't been filled in
  global board

  rand_num_same = True
  if switch == False and none_in_board == True:
    while rand_num_same == True:
      random_posX = randint(0, width_board - 1)
      random_posY = randint(0, width_board - 1)
      if board[random_posX][random_posY] == None:
        rand_bin_num = randint(0, 1)
        board[random_posX][random_posY] = rand_bin_num
        rand_num_same = False
      else:
        rand_num_same = True


def test_solved():
  #Tests if the puzzle is solved
  global board
  global solved_list
  global vert_list
  global solved

  if none_in_board == False:
    #Same amount of 0s and 1s horizontally?
    for i in range(width_board):	
      if board[i].count(0) != board[i].count(1):
        solved_list.append(False)
      
    #Same amount of 0s and 1s vertically?
    posY = 0
    for i in range(width_board):
      posX = 0
      for i in range(width_board):
        vert_list.append(board[posX][posY])
        posX += 1
      if vert_list.count(0) != vert_list.count(1):
        solved_list.append(False)
      vert_list.clear()
      posY += 1
      
    #Tests if 1s next to "00" or 0s next to "11" horizontally
    posX = 0
    while posX <= (width_board - 1):
      posY = 0
      posY2 = 1
      for i in range(width_board - 1):
        if board[posX][posY] == 1 and board[posX][posY2] == 1:
          if posY == 0:
            if board[posX][posY2 + 1] != 0:
              solved_list.append(False)
          elif posY2 == (width_board - 1):
            if board[posX][posY - 1] != 0:
              solved_list.append(False)
          else:
            if board[posX][posY - 1] != 0 or board[posX][posY2 + 1] != 0:
              solved_list.append(False)
            
          
        elif board[posX][posY] == 0 and board[posX][posY2] == 0:
          if posY == 0:
            if board[posX][posY2 + 1] != 1:
              solved_list.append(False)
          elif posY2 == (width_board - 1):
            if board[posX][posY - 1] != 1:
              solved_list.append(False)
          else:
            if board[posX][posY - 1] != 1 or board[posX][posY2 + 1] != 1:
              solved_list.append(False)
        posY += 1
        posY2 += 1
      posX += 1

    #Tests if 1s next to "00" or 0s next to "11" vertically
    posX = 0
    posX2 = 1
    while posX2 <= (width_board - 1):
      posY = 0
      for i in range(width_board):
        if board[posX][posY] == 1 and board[posX2][posY] == 1:
          if posX == 0:
            if board[posX2 + 1][posY] != 0:
              solved_list.append(False)
          elif posX2 == (width_board - 1):
            if board[posX - 1][posY] != 0:
              solved_list.append(False)
          else:
            if board[posX - 1][posY] != 0 or board[posX2 + 1][posY] !=  0:
              solved_list.append(False)
    
        elif board[posX][posY] == 0 and  board[posX2][posY] == 0:
          if posX == 0:
            if board[posX2 + 1][posY] != 1:
              solved_list.append(False)
          elif posX2 == (width_board - 1):
            if board[posX - 1][posY] != 1:
              solved_list.append(False)
          else:
            if board[posX - 1][posY] != 1 or board[posX2 + 1][posY] !=  1:
              solved_list.append(False)

        posY += 1
      posX += 1
      posX2 += 1

    #If none of the previous tests returned False, declare the puzzle solved, otherwise reset the board and try again
    if False not in solved_list: 
      print("")
      print ("Puzzle Solved!")
      print_board()
      solved = True
    else:
      reset_board()
    

def puzzle():
  create_board()
  print_board()

  ini_predef_num()
  print_board()


  while solved != True:
    test_double_hor()

    test_double_vert()

    test_triple_hor()

    test_triple_vert()

    max_num_hor()

    max_num_vert()

    count_none()
  
    random_num()

    test_solved()
    
def reset_var():
  global board, width_board, total_predef_numb, predef_numb, x, y, switch, none_in_board, solved_list, vert_list, solved
  
  board = []
  width_board = 0
  total_predef_numb = 0
  predef_numb = []
  x = []
  y = []
  switch = False
  none_in_board = False
  solved_list = []
  vert_list = []
  solved = False


puzzle()
while True:
  restart = input("Do you want to solve another puzzle?(y/n) ")
  print ("")
  if restart == "y" or restart == "Y":
    reset_var()
    puzzle()
  elif restart == "n" or restart == "N":
    sys.exit()
  else:
    print ("Enter y or n")
    print ("")

    
 

