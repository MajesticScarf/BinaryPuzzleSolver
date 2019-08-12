board = []
width_board = int(input("Width of the board? "))

predef_numb = []

x = []
y = []

def create_board():
  global board
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

def reset_predef_num():
  #Resets the predef numbers
  global board
  global predef_numb
  
  for i in predef_numb:
    board[x[i]][y[i]] = predef_numb[int(i)]

def test_double_hor():
  #Looks for "00" or "11" horizontally and puts the opposite number beside them
  global board
  
  posX = 0
  posY = 0
  posY2 = 1
  while posX <= (width_board - 1):
    posY = 0
    posY2 = 1
    for i in range(width_board - 1):
      if board[posX][posY] == 1 and board[posX][posY2] == 1:
        if posY != 0:
          board[posX][posY - 1] = 0
          switch = True
        if posY2 != (width_board - 1):
          board[posX][posY2 + 1] = 0
          switch = True
          
      elif board[posX][posY] == 0 and board[posX][posY2] == 0:
        if posY != 0:
          board[posX][posY - 1] = 1
          switch = True
        if posY2 != (width_board - 1):
          board[posX][posY2 + 1] = 1
          switch = True
      posY += 1
      posY2 += 1
    posX += 1

def test_double_vert():
  global board
  
  posX = 0
  posX2 = 1
  while posX2 <= (width_board - 1):
    posY = 0
    for i in range(width_board):
      if board[posX][posY] == 1 and board[posX2][posY] == 1:
        if posX != 0:
          board[posX - 1][posY] = 0
        if posX2 != (width_board - 1):
          board[posX2 + 1][posY] = 0
      elif board[posX][posY] == 0 and  board[posX2][posY] == 0:
        if posX != 0:
          board[posX - 1][posY] = 1
        if posX2 != (width_board - 1):
          board[posX2 + 1][posY] = 1
      posY += 1
    posX += 1
    posX2 += 1
    
    
create_board()
print_board()

ini_predef_num()
print_board()

test_double_hor()
print_board()

test_double_vert()
print_board()
#reset_predef_num()
#print_board()
