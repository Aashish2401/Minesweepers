import numpy as np
import random

L = 8
W  = 8

total  = L * W

count = 9

grid = []
flag = []
pos = []

#Function to generate the mine field
def matrix():
    for i in range(L):
        gridr = []
        flagr = []
        
        for j in range(W):
            gridr.append('0')
            flagr.append('C')
            
        grid.append(gridr)
        flag.append(flagr)
        del gridr
        del flagr

#Function to count and save the number of mines around a particular block 
def number():
    global grid,L,W
    
    for i in range(L):
        for j in range(W):
            counter = 0
            sx = i-1
            sy = j-1
            ey = j+2
            ex = i+2
            if(i == 0):
                sx = i
                
            if(j == 0):
                sy = j
                
            if(i == W - 1):
                ex = i+1
                
            if(j == L - 1):
                ey = j+1
                
            for x in range(sx, ex):
                for y in range(sy, ey):
                    if(grid[x][y] == '*'):
                        counter += 1
                        
            if(grid[i][j] != '*'):
                grid[i][j] = str(counter)

#Function to print the mine field in a neet format
def printm():
    global grid,flag
    print("    1   2   3   4   5   6   7   8")
    
    for i in range(L):
        print("  --------------------------------")
        print(i + 1,end = ' ')
        for j in range(W):
            if flag[i][j] == 'C' or flag[i][j] == 'F':
                print('| ' + flag[i][j] + ' ',end = '')
            elif grid[i][j] != '0':
                print('| ' + grid[i][j] + ' ',end = '')
            else:
                print('|   ',end = '')
                
        print ()
    print("  --------------------------------")

#Generating the random positions to place the mines
def pos_init():
    global pos,count
    
    for i in range(count):
        f = 1
        
        while(f):
            new = random.randint(0,total-1)
            
            for j in pos:
                if(pos != j):
                    f = 0
                    continue               
                else:
                    f = 1
                    break
                
            if(len(pos) == 0):
                f = 0
                
        pos.append(new)

#Use the pos data to place the mines
def place():
    global pos,grid
    
    for i in pos:
        x = i // W
        y = i - (x*L)
        grid[x][y] = '*'

#Function to open the block that the user enters
def openm(i,j):
    global grid,flag,L,W
    
    if grid[i][j] == '*':
        return
    
    if grid[i][j] != '*':
        flag[i][j] = 'O'
        
    if grid[i][j] == '0':
        if i != 0:
            if flag[i-1][j] == 'C':
                openm(i-1,j)
                
            if j != 0:
                if flag[i-1][j-1] == 'C':
                    openm(i-1,j-1)
                    
            if j != W - 1:
                if flag[i-1][j+1] == 'C':
                    openm(i-1,j+1)
                    
        if j != W - 1:
            if flag[i][j+1] == 'C':
                openm(i,j+1)
                
        if i != L - 1:
            if flag[i+1][j] == 'C':
                openm(i+1,j)
                
            if j != 0:
                if flag[i+1][j-1] == 'C':
                    openm(i+1,j-1)
                    
            if j != W - 1:
                if flag[i+1][j+1] == 'C':
                    openm(i+1,j+1)
                    
        if j != 0:
            if flag[i][j-1] == 'C':
                openm(i,j-1)
                
    return

#Main function that calls and performs all the functions of the game
def play_game():
    matrix()
    pos_init()
    place()
    number()

    cont = True

    printm()
    while(cont):
        cnt = 0
        
        for i in range(L):
            for j in range(W):
                if flag[i][j] == 'C' or flag[i][j] == 'F':
                    cnt = cnt + 1
        if cnt <= count:
            print("You Won!!")
            cont = False
            break
        i = int(input("Row: "))
        j = int(input("Column: "))
        
        if grid[i-1][j-1] == '*':
            flag[i-1][j-1] = 'O'
            printm()
            print()
            print("Game Over!")
            cont = False
        else:
            openm(i-1,j-1)
            print()
            printm()

play_game()
input()
