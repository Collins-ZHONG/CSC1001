def eight_queens():

    """
    The classic Eight Queens puzzle is to place eight queens on a 
    chessboard such that no two queens can attack each other (i.e., no two queens are in the 
    same row, same column, or same diagonal). There are many possible solutions. Write a 
    program that displays one such solution.

    Note: you cannot just pre-define a solution and display it. 
    Please use algorithm to display a possible solution.
    """

    ############## Start your codes ##############
    def checkLine(Line,x):
        if x==0:
            return True
        else:
            for i in range(x):  #i小于recursion
                if (Line[i]-Line[x])**2==(i-x)**2 or Line[i]==Line[x]:
                    return False
            else:
                return True
    
    def queensLine(Line=[' ']*8,recursion=0):
        setLine=Line.copy()
        if recursion==8:
            global aList
            aList.append(setLine)
            return None

        for i in range(8):
            setLine[recursion]=i
            if checkLine(setLine,recursion)==False:
                continue
            elif checkLine(setLine,recursion)==True:
                queensLine(setLine,recursion+1)

    def printAlist(a):
        for i in range(8):
            print('|',end='')
            chessLine=[' ']*8
            position=a[i]
            chessLine[position]='Q'
            for j in chessLine:
                print(j,end='|')
            print(' ')



    queensLine()
    from random import randint
    a=aList[randint(0,len(aList))]
    printAlist(a)
    ##############  End your codes  ##############

aList=[]
if __name__ == '__main__':
    eight_queens()

    # This function does not need a return value. 
    # You can just print your solution. For example:
    # |Q| | | | | | | |
    # | | | | |Q| | | |
    # | | | | | | | |Q|
    # | | | | | |Q| | |
    # | | |Q| | | | | |
    # | | | | | | |Q| |
    # | |Q| | | | | | |
    # | | | |Q| | | | |