#########################################
## 1
## 1 2
## 1 2 3
## 1 2 3 4
## 1 2 3 4 5

# num = int(input("Enter num: "))
# for r in range(1, num+1):
#     for c in range(1, r+1):
#         print(c, end = "")
#     print()

#----------------------------------------

## 1 2 3 4 5
## 1 2 3 4 
## 1 2 3
## 1 2 
## 1

# num = int(input("Enter num: "))
# for r in range(num, 0, -1):
#     for c in range(1, r+1):
#         print(c, end = "")
#     print()

#----------------------------------------

## *
## * *
## * * *
## * * * *
## * * * * *

# num = int(input("Enter num: "))
# for r in range(1, num+1):
#     for c in range(1, r+1):
#         print("*", end = "")
#     print()

#----------------------------------------

# * * * * *
# * * * *
# * * *
# * *
# *

# num = int(input("Enter num: "))
# for r in range(num, 0, -1):
#     for c in range(1, r+1):
#         print("*", end = "")
#     print()

#----------------------------------------

## A
## A B
## A B C
## A B C D
## A B C D E

# num = int(input("Enter num: "))
# for r in range(1, num+1):
#     a = 65
#     for c in range(1, r+1):
#         print(chr(a), end = "")
#         a += 1
#     print()

#----------------------------------------

## A B C D E
## A B C D
## A B C
## A B 
## A 

# num = int(input("Enter num: "))
# for r in range(num, 0, -1):
#     a = 65
#     for c in range(1, r+1):
#         print(chr(a), end = "")
#         a+=1
#     print()

#----------------------------------------

## 5 4 3 2 1
## 5 4 3 2
## 5 4 3 
## 5 4
## 5

# num = int(input("Enter num: "))
# for r in range(num, 0, -1):
#     a = num
#     for c in range(1, r+1):
#         print(a, end = " ")
#         a-=1
#     print()

#----------------------------------------

## 1 2 3 4 5
## 1 2 3 4
## 1 2 3
## 1 2
## 1

# num = int(input("Enter num: "))
# for r in range(num, 0, -1):
#     a = 1
#     for c in range(1, r+1):
#         print(a, end = " ")
#         a+=1
#     print()

#----------------------------------------

## A
## B B
## C C C 
## D D D D 
## E E E E E

# num = int(input("Enter num: "))
# a = 65
# for r in range(1, num+1):
#     for c in range(1, r+1):
#         print(chr(a), end = " ")
#     a+=1
#     print()
#----------------------------------------

## A A A A A 
## B B B B
## C C C 
## D D 
## E

# num = int(input("Enter num: "))
# a = 65
# for r in range(num, 0, -1):
#     for c in range(1, r+1):
#         print(chr(a), end = " ")
#     a+=1
#     print()

#----------------------------------------

## A 
## B C
## D E F
## G H I J
## K L M N O

# num = int(input("Enter num: "))
# a = 65
# for r in range(1, num+1):
#     for c in range(1, r+1):
#         print(chr(a), end = " ")
#         a+=1
#     print()

#----------------------------------------

## A B C D E
## F G H I
## J K L
## M N 
## O

# num = int(input("Enter num: "))
# a = 65
# for r in range(num, 0, -1):
#     for c in range(1, r+1):
#         print(chr(a), end = " ")
#         a+=1
#     print()

#----------------------------------------
# ----------> LOOPS WITH THE GAP
#-----------------------------------------
#     *
#    **
#   ***
#  ****
# *****

# num = int(input("Enter num: "))
# for r in range(num, 0, -1):
#     for gap in range(1, r):
#         print(" ", end = ' ')
#     for c in range(num, r-1, -1):
#         print("*", end = ' ')
#     print() 

#-----------------------------------------

# *****
# ****
# ***
# **
# *

# num = int(input("Enter num: "))
# for r in range(1, num + 1):
#     for gap in range(1, r):
#         print(' ', end = ' ')
#     for c in range(num, r-1, -1):
#         print("*", end= ' ')
#     print()    

#-----------------------------------------
###############

#-----------------------------------------

#         1
#       1 2
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5

# num = int(input("Enter num: "))
# for r in range(num, 0, -1):
#     for gap in range(1, r):
#         print(" ", end = ' ')
#     n = 1
#     for c in range(num, r-1, -1):
#         print(n, end = ' ')
#         n += 1
#     print()

#-----------------------------------------

# 1 2 3 4 5 
#   1 2 3 4
#     1 2 3      
#       1 2
#         1

# num = int(input("Enter num: "))
# for r in range(1, num+1):
#     for gap in range(1, r):
#         print(' ', end = ' ')
#     n = 1
#     for c in range(r, num+1):
#         print(n, end = " ")
#         n += 1
#     print()

#-----------------------------------------

#         1
#       2 1
#     3 2 1
#   4 3 2 1
# 5 4 3 2 1

# num = int(input("Enter num: "))
# n = 1
# for r in range(num, 0, -1):
#     for gap in range(1, r):
#         print(" ", end = ' ')
#     for c in range(n, 0, -1):
#         print(c, end = ' ')
#     n += 1
#     print()

#-----------------------------------------

# 5 4 3 2 1
#   4 3 2 1
#     3 2 1      
#       2 1
#         1

# num = int(input("Enter num: "))
# n = num
# for r in range(1, num+1):
#     for gap in range(1, r):
#         print(" ", end = ' ')
#     for c in range(n, 0, -1):
#         print(c, end = ' ')
#     n -= 1
#     print()

#-----------------------------------------

#         5
#       4 5
#     3 4 5
#   2 3 4 5
# 1 2 3 4 5

# num = int(input("Enter num: "))
# n = num
# for r in range(num, 0, -1):
#     for gap in range(1, r):
#         print("  ", end = " ")
#     for c in range(n, num+1):
#         print(c, end = ' ')
#     n-=1
#     print()

#-----------------------------------------

# 1 2 3 4 5
#   2 3 4 5
#     3 4 5      
#       4 5
#         5

# num = int(input("Enter num: "))
# n = 1
# for r in range(1, num+1):
#     for gap in range(1, r):
#         print(" ", end = ' ')
#     for c in range(n, num+1):
#         print(c, end = ' ')
#     n += 1
#     print()


#-----------------------------------------
###############
#         A
#       B A 
#     C B A
#   D C B A
# E D C B A

# ch = 65
# num = int(input("Enter the num: "))
# for r in range(num, 0, -1):
#     for gap in range(1, r):
#         print("^", end = ' ')
#     # ch = 65
#     for c in range(ch, 64, -1):
#         print(chr(c), end = ' ')
#     ch += 1
#     print()

#-----------------------------------------

# E D C B A
#   D C B A
#     C B A      
#       B A
#         A

# ch = 65
# n = 1
# num = int(input("Enter the num: "))
# for r in range(1, num+1):
#     for gap in range(1, r):
#         print(" ", end = ' ')
#     for c in range(ch+(num-n), ch-1, -1):
#         print(chr(c), end = ' ')
#     n+=1
#     print()

#-----------------------------------------

#         E
#       D E
#     C D E
#   B C D E
# A B C D E

# ch = 70
# n = 1
# num = int(input("Enter the num: "))
# for r in range(num, 0, -1):
#     for gap in range(1, r):
#         print(" ", end = ' ')
#     for c in range(ch-n,ch):
#         print(chr(c), end = ' ')
#     n+=1
#     print()

#-----------------------------------------

# A B C D E
#   B C D E
#     C D E      
#       D E
#         E

# ch = 70
# n = 0
# num = int(input("Enter the num: "))
# for r in range(1, num+1):
#     for gap in range(1, r):
#         print(" ", end = ' ')
#     for c in range(65+n, ch):
#         print(chr(c), end = ' ')
#     n += 1
#     print()

#-----------------------------------------
###############
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

## MINE

# num = int(input("Enter the number: "))
# for r in range(num , 0, -1):
#     for gap in range(1, r):
#         print(' ', end = ' ')
#     for c in range(r, num+1):
#         print(" * ", end = ' ')
#     print()

## NOT MINE

# num = int(input("Enter the number: "))
# for r in range(0, num):
#     for gap in range(0, num - r - 1):
#         print(end = ' ')
#     for j in range(0, r+1):
#         print("*", end = ' ')
#     print()
# -----------------------------------
###############
#     A
#    B C
#   D E F
#  G H I J 
# K L M N O 

# ch = 65
# n = 1
# num = int(input("Enter the number: "))
# for r in range(num, 0, -1):
#     for gap in range(1, r):
#         print(" ", end = ' ')
#     for c in range(ch, ch+n):
#         print(' ' + chr(c)+ ' ', end = ' ')
#         ch += 1
#     n += 1
#     print()

# ------------------------------------

#     A
#    B B
#   C C C
#  D D D D 
# E E E E E 

# ch = 65
# n = 1
# num = int(input("Enter the number: "))
# for r in range(num, 0, -1):
#     for gap in range(1, r):
#         print(' ', end = ' ')
#     for c in range(0, n):
#         print(' ' + chr(ch) + ' ', end = ' ')
#     ch += 1
#     n += 1
#     print()

# ------------------------------------

## still make a pyramid and opposite of that too

#     1 
#    2 3
#   4 5 6
#  7 8 9 10
# 11 12 13 14 15


# num = int(input("Enter the number: "))
# n = 1
# s = 1
# for r in range(num, 0, -1):
#     for gap in range(1, r):
#         print(' ', end = ' ')    
#     for c in range(1, s+1):
#         print('', n, '', end = ' ')
#         n += 1
#     s += 1
#     print()

###############incomplete

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

# num = int(input("Enter the num: "))
# n=1
# for r in range(1, num+1):
#     for c in range(1, r+1):
#         print(n, end = ' ')
#         n += 1
#     print()

# ------------------------------------

#     1
#    2 2
#   3 3 3
#  4 4 4 4 
# 5 5 5 5 5 

# n = 1
# num = int(input("Enter the num: "))
# for r in range(num, 0, -1):
#     for gap in range(1, r):
#         print(" ", end = ' ')
#     for c in range(1, n+1):
#         print('', n , '', end = ' ')
#     n+=1
#     print()

# ------------------------------------

# A B C D E
#  F G H I
#   J K L 
#    M N
#     o 

# ch = 65
# n = 5
# # num = int(input("Enter the num: "))
# for r in range(1, 6):
#     for gap in range(1, r):
#         print(' ', end = ' ')
#     for c in range(1, n+1):
#         print('', chr(ch), '', end = ' ')
#         ch+=1
#     n-=1
#     print()

