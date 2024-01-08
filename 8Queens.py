from time import sleep


board = [ 9 * [0] , 9 * [0], 9 * [0], 9 * [0], 9 * [0], 9 * [0], 9 * [0], 9 * [0], 9 * [0]]  #用8个列向量当做棋盘，从第一列开始逐列摆放

def isSafe(col, row):

    global board

    # if col == 1:
    #     if row in (1,2):
    #         return False
    # else:
    for i in range(0,9):      #检查是不是在同一行
        if board[i][row] == 1:
            return False
        
    if 1 in board[col]: return False
        
    for m in range(1,col):         #检查是不是在对角线
        for n in range(1,9):
            if abs(n-row) == abs(col-m) and board[m][n] == 1:
                return False
        
    return True

# board = [9 * [0], [0,1,0,0,0,0,0,0,0], 9 * [0], 9 * [0], 9 * [0], 9 * [0], 9 * [0], 9 * [0], 9 * [0]]

# print(isSafe(1,2))  # Should be False   -->  False after debug
# print(isSafe(1,3))  # Should be False
# print(isSafe(2,1))  #应该打出False，实际上也打出了False
# print(isSafe(2,2))  #应该打出False，实际上也打出了False
# print(isSafe(2,3))  #应该打出True，实际上也打出了True

        
def printSolution(board):  #打出结果
    for col in range (1, 9):
        for row in range (1, 9):
            print(board[col][row], ' ', end='')
        print('')
    print("")

# board = [[0,0,0,0,0,0,0,0,0], [0,1,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,1,0], [0,0,0,0,0,1,0,0,0], [0,0,0,0,0,0,0,0,1], [0,0,1,0,0,0,0,0,0], [0,0,0,0,1,0,0,0,0], [0,0,0,0,0,0,1,0,0], [0,0,0,1,0,0,0,0,0]]
# printSolution(board)      #打出来没问题，但打完所有结果之后不会自动停止运行，很奇怪

def solveQueens(col, row, recur):

    global board
    if recur == 8:              # 结束条件
        board[col][row] = 1
        printSolution(board)
        exit()


    board[col][row] = 1
    # printSolution(board)
    # sleep(1)

    '''testing'''
    # print("col =", col, "row =",row)  # test
    # printSolution(board)        # test
    # sleep(0.5)
    """end of testing"""

    
    # else:                                   #主要是这个地方我实在逻辑混乱了、、主要是这里写不出来

    col_o = col; row_o = row
    # for col in range(col_num,9):
    #     for row in range(row_num,9): 

    for col in range(col_o,9):      # range(col, 9)
        for row in range(1,9):  # 这里却应该是range(1,9)

            # print("col =", col, "row =",row, recur)  # test


            if isSafe(col, row):
                # board[col][row] = 1

                # printSolution(board)        # test
                # print("check", col, row)

                solveQueens(col, row, recur+1)


    # print("retreat\n",col_o,row_o)
    board[col_o][row_o] = 0
    # printSolution(board)
    # sleep(0.5)
    return
                
                

solveQueens(1,1,1)   