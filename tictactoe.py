 """TIC-TAC-TOE"""


import time #importing time module
from random import randint #importing random module
l= [[1,2,3],[4,'X',6],[7,8,9]] #making initial list for computer's turn
x=[1,2,3,4,6,7,8,9] #valid values
userwin=0 #user win
cwin=0 #computer win
print("TIC-TAC-TOE")
time.sleep(2) #wait for 2 seconds
print("Start game")
time.sleep(1)
for i in l:
    print(*i, sep='   ') # COMPUTER PLAYS FIRST
while (len(x)!=0 and userwin==0 and cwin==0):
               """USERS TURN"""
               if(cwin!=1):
                   """"ASKING FOR USER TO ENTER"""
                   while (1):

                      z=int(input("Your turn:"))
                      if (z in x): #checking if its valid integer and not repeated before..
                          break

                   """REPLACING THE VALUE AND PRINTING THE BOARD"""
                   for i in range(3):
                       for j in range(3):
                           if (l[i][j]==z):
                                l[i][j]="O"
                                x.remove(z) #same z value cannot be used for next turn
                   for i in l:
                       print(*i, sep='   ')
                   print()
                   time.sleep(2)

                   """"CHECKING FOR USER WIN """
                   for i in range(3): #checking if rows are equal
                       rows = all(element == l[i][0] == "O" for element in l[i])
                       if (rows == True):
                           userwin = 1
                           print("YOU WON!!")
                           break
                   for i in range(3):  # checking if columns are equal
                       z = [x[i] for x in l]
                       col = all(element == l[0][i] == "O" for element in z)
                       if (col == True):
                           userwin = 1
                           print("YOU WON!!")
                           break
                   # checking if diagonal element equal
                   if ((l[0][0] == l[1][1] == l[2][2] == "O") or (l[0][2] == l[1][1] == l[2][0] == "O")):
                       userwin = 1
                       print("YOU WON!!")
                       break

               """COMPUTERS TURN """
               if (userwin!=1):
                   def uniquenumforcomputer():
                       return randint(1,10)

                   while True:
                       u = uniquenumforcomputer()
                       if u in x:
                           break

                   for i in range(3):
                       for j in range(3):
                          if (l[i][j] == u):
                            l[i][j]="X"
                            x.remove(u)
                   for i in l:
                       print(*i, sep='   ')
                   print()
                   """"CHECKING FOR COMPUTER WIN """
                   for i in range(3): # checking if rows are equal
                       rows = all(element == l[i][0] == "X" for element in l[i])
                       if (rows == True):
                           cwin = 1
                           print("OOPS!YOU LOST!")
                           break
                   for i in range(3):  # checking if columns are equal
                       z = [x[i] for x in l]
                       col = all(element == l[0][i] == "X" for element in z)
                       if (col == True):
                           cwin = 1
                           print("OOPS!YOU LOST!")
                           break
                   # checking if diagonal element equal
                   if ((l[0][0] == l[1][1] == l[2][2] == "X") or (l[0][2] == l[1][1] == l[2][0] == "X")):
                       cwin = 1
                       print("OOPS!YOU LOST!")
                       break
"""CHECKING FOR TIE"""
if (userwin==0 and cwin==0):
   print("ITS A TIE!")





