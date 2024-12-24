
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
def solve(bo):
    find = find_blank_box(bo)
    if not find :
        return True#this means we have found the final value
    else:
        row,col=find
    for i in range(1,10):
        c=check(bo,(row,col),i)#inserts a value according to sudoku rules
        if c:
            bo[row][col]=i
            if solve(bo):
                return True
            bo[row][col]=0#if solve gives false then it backtracks to the original position and then as per loop inserts the next value
    return False
def print_sudoku(bo):
    for i in range(len(bo)):
        if i%3==0 and i!=0:
            print("- - - - - - - - - -");
        
        for j in range(len(bo[0])):
            if j%3==0 and j!=0:
                    print("|",end="");

            if j==8:
                print(bo[i][j]);
            else:
                print(str(bo[i][j]) + " ",end="");
def find_blank_box(bo):#selects a blank box and this function is called in the solve function 
    for i in range(len(bo)):
        for j in range(len(bo[i])):
            if bo[i][j]==0:
                return(i,j)
    return None
def check(bo,pos,num):#checks if the value we insert does not break the sudoku rules
    for i in range(len(bo[0])):
        if bo[pos[0]][i]==num and pos[1]!=i:
            return False
    
    for i in range(len(bo[0])):
        if bo[i][pos[1]]==num and pos[0]!=i:
            return False
    box_x= pos[1]//3
    box_y= pos[0]//3
    for i in range(box_y*3,box_y*3+3):
        for j in range(box_x*3,box_x*3+3):
            if bo[i][j]==num and pos!=(i,j):
                return False
    return True

print_sudoku(board)
solve(board)
print_sudoku(board)
