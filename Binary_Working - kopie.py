from random import randint

board = []
width_board = int(input("Width of the board? "))

predef_numb = []

x = []
y = []

switch = False

none_in_board = False

solved_list = []
vert_list = []

solved = False

def create_board():
  global board
  global board_copy
  global width_board
  
  for i in range(width_board):
    board.append([])
  for i in range(width_board):
    for a in range(width_board):
      board[i].append(None)

def print_board():
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
  
  total_predef_numb = int(input("Total of predefined numbers? "))
  for i in range(total_predef_numb):
    numb = int(input("Predefined number " + str(int(i) + 1) + " (0/1): "))
    predef_numb.append(numb)
  print ("")

  
  for i in range(total_predef_numb):
    x.append(int(input("X co-ordinate of predefined number " + str(int(i + 1)) + ": "), base = 36))
    y.append(int(input("Y co-ordinate of predefined number " + str(int(i + 1)) + ": "), base = 36)) 
    board[x[i]][y[i]] = predef_numb[int(i)]
    print ("")

def reset_board():
  #Resets the board
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
  
  posX = 0
  while posX <= (width_board - 1):
    posY = 0
    posY2 = 1
    for i in range(width_board - 1):
      if board[posX][posY] == 1 and board[posX][posY2] == 1:
        if posY != 0:
          if board[posX][posY - 1] != 0:
            board[posX][posY - 1] = 0
            switch = True
        if posY2 != (width_board - 1):
          if board[posX][posY2 + 1] != 0:
            board[posX][posY2 + 1] = 0
            switch = True
          
      elif board[posX][posY] == 0 and board[posX][posY2] == 0:
        if posY != 0:
          if board[posX][posY - 1] != 1:
            board[posX][posY - 1] = 1
            switch = True
        if posY2 != (width_board - 1):
          if board[posX][posY2 + 1] != 1:
            board[posX][posY2 + 1] = 1
            switch = True
      posY += 1
      posY2 += 1
    posX += 1


def test_double_vert():
  #Looks for "00" and "11" vertically and puts the opposite number beside them
  global board
  global switch
  
  posX = 0
  posX2 = 1
  while posX2 <= (width_board - 1):
    posY = 0
    for i in range(width_board):
      if board[posX][posY] == 1 and board[posX2][posY] == 1:
        if posX != 0:
          if board[posX - 1][posY] != 0:
            board[posX - 1][posY] = 0
            switch = True
        if posX2 != (width_board - 1):
          if board[posX2 + 1][posY] != 0:
            board[posX2 + 1][posY] = 0
            switch = True
            
      elif board[posX][posY] == 0 and  board[posX2][posY] == 0:
        if posX != 0:
          if board[posX - 1][posY] != 1:
            board[posX - 1][posY] = 1
            switch = True
        if posX2 != (width_board - 1):
          if board[posX2 + 1][posY] != 1:
            board[posX2 + 1][posY] = 1
            switch = True
      posY += 1
    posX += 1
    posX2 += 1
    

def test_triple_hor():
  global board
  global switch
  
  posX = 0
  while posX <= (width_board - 1):
    posY = 0
    posY2 = 2
    for i in range(width_board - 2):
      if board[posX][posY] == 1 and board[posX][posY2] == 1:
        if board[posX][posY + 1] != 0:
          board[posX][posY + 1] = 0
          switch = True          
      elif board[posX][posY] == 0 and board[posX][posY2] == 0:
        if board[posX][posY + 1] != 1:
          board[posX][posY + 1] = 1
          switch = True
      posY += 1
      posY2 += 1
    posX += 1

def test_triple_vert():
  global board
  global switch
  
  posX = 0
  posX2 = 2
  while posX2 <= (width_board - 1):
    posY = 0
    for i in range(width_board):
      if board[posX][posY] == 1 and board[posX2][posY] == 1:
        if board[posX + 1][posY] != 0:
          board[posX + 1][posY] = 0
          switch = True
      elif board[posX][posY] == 0 and  board[posX2][posY] == 0:
        if board[posX + 1][posY] != 1:
          board[posX + 1][posY] = 1
          switch = True
      posY += 1
    posX += 1
    posX2 += 1



def count_none():
  global none_in_board
  
  none_in_board = False
  for i in range(width_board):
    if None in board[i]:
      none_in_board = True


def random_num():
  #If the board isn't filled in, fill in a 0/1 in a random spot (not a predef number) 
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

    if False not in solved_list: 
      print("")
      print ("Puzzle Solved!")
      print_board()
      solved = True
    else:
      reset_board()
    
  

create_board()
print_board()

ini_predef_num()
print_board()


while solved != True:
  test_double_hor()

  test_double_vert()

  test_triple_hor()

  test_triple_vert()

  count_none()
  
  random_num()

  test_solved()
 

