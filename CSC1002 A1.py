import random

'''

There are 11 functions in total (except main() function)
fION(data)
checkSol(dim,data)
get_dimension()
setBoard(dim,data)
printBoard(dim,data)
same(four_keys)
validBottoms(four_letters)
four_key()
movable(dim,data,four_letters)
validMoves(e)
move(e,dim,data,four_letters)
checkGame(dim,data)


important variables:

data: 
a simple list which contains numbers and their order

dim:
number of rows and column (in this question they are the same and noted as dimension)

four_letters:
a simple list contains the four bottoms in a certain order


##----- Key Thoughts -----##
Indentation of numbers in puzzle:
Use 2 integer x and y to show index: x*dim+y so that x represent the line and y represent the row
x = index // dim ;  y = index % dim
So that a verticle move could be simplified as a change of x and a horizontal move could be simplified as a change of y

'''



letter_list_lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letter_list_upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


def fION(data):              # Find Inverse Order Number. FON would be used in checking whether the random puzzle is solvable
    count = 0
    for i in data:
        if i == ' ':
            pass
        else:
            for j in data[data.index(i)+1:]:
                if j == ' ':
                    pass
                elif i>j:
                    count += 1

    # print(count)          #check
    
    if count % 2 == 0:      
        return True         # Number of pairs of ION is even
    else: return False      # odd


'''
The following method of checking whether the puzzle has solution are translated from internet and adjusted during tests
I)  if number of rows is odd, must be even pair of ION
II) if number of rows is even,
    i)  if odd pairs of ION, (lineNow-numberOfRows) is even
    ii) if even pairs of ION, (lineNow-numberOfRows) is odd
'''
def checkSol(dim,data):
    if dim % 2 == 1:                        # odd number of rows
        if fION(data):                          # even pairs of ION
            # print(True,'1')         #check   
            return True                                 # have solution according to I)
        else: return False                      # odd pairs of ION
    elif dim % 2 == 0:                      # even number of rows
        x = data.index(' ') // dim
        if fION(data):                          # even pairs of ION
            if (dim-x) % 2 == 1:                    # numberOfRows-lineNow is odd
                # print(True,'2')     #check
                return True                             # have solution according to II)-ii)
            else: return False
        else:                                   # odd pairs of ION
            if (dim-x) % 2 == 0:                    # numberOfRows-lineNow is even
                # print(True,'3')     #check
                return True                             # have solution according to II)-i)
            else: return False


def get_dimension():
    global letter_list_lower
    global letter_list_upper
    while True:
        n = input('Enter the level of the game ("1" for 8-puzzle, "2" for 15-puzzle or "q" to end the game) >')
        if n == 'q':
            return 0
        try:
            if type(n) == float:
                print('The float number you entered has been changed into the biggest integer smaller than it.')
            dim = eval(n) + 2
            break
        except:
            if len(n) == 0:
                print('You entered nothing.')
            elif n in (letter_list_upper or letter_list_lower):
                print('You entered letter.')
            else:
                print('The dimension you entered is not an integer.')
            print('Try again.')
    return dim


def setBoard(dim,data):                     # set up initial puzzle
    random.shuffle(data)
    data[data.index(dim**2)] = ' '    
    while checkSol(dim,data) == False:
        random.shuffle(data)                # disorganizes the list into an unsolved puzzle


def printBoard(dim,data):                   # print out the list as a puzzle
    for row in range(0,dim):
        for col in range(0,dim): 
            print(data[dim*row+col],end='\t')
        print(' ')                          # change line after a row is printed


'''This Function is used in the function "four_key()" in order to check whether the input bottoms are valid'''
def same(four_keys):
    for i in four_keys:
        for j in four_keys[four_keys.index(i)+1:]:
            if i == j:
                print('You entered same number for different bottoms.')
                return True
    return False


def validBottoms(four_letters):
    global letter_list_upper
    global letter_list_lower
    for i in four_letters:
        if i in letter_list_lower:
            pass
        elif i in letter_list_upper:
            print('The bottoms you entered is Uppercase. Please enter lowercase letters.')
            return False
        
        if len(i) == 0:
            print('The bottoms you entered is short.')
            return False
        elif len(i) >= 2:
            print('The bottoms you entered is too long.')
            return False
    return True


def four_key():
    while True:
        moves = input('Enter letters used for moves in order of (up,down,left,right) > ')
        if ',' in moves:     
            four_letters = moves.split(',')
        elif ' ' in moves:
            four_letters = moves.split()
        else: 
            print('Please split four letters by "," or "(space)".')
            four_letters = []

        if same(four_letters):
            four_letters = []

        if len(four_letters) == 4:
            if validBottoms(four_letters):
                break

        elif len(four_letters) < 4:
            print('The bottoms you entered are less than 4.')
        elif len(four_letters) > 4:
            print('The bottoms you entered are more than 4.')

        print('Please enter the four bottoms in correct form.')
        print(' ')
    return four_letters


'''This function is used to print out hints of the bottoms the user entered before'''
def movable(dim,data,four_letters):
    key = data.index(' '); x = key // dim; y = key % dim
    
    ans = ''
    if y != dim - 1:
        ans += 'left-' + four_letters[2] + ', '
    if y != 0:
        ans += 'right-' + four_letters[3] + ', '
    if x != dim - 1:
        ans += 'up-' + four_letters[0] + ', '
    if x != 0:                       
        ans += 'down-' + four_letters[1] + ', '
    ans = ans.rstrip(', ')
    return '(' + ans + ')'


'''Only used to tell different mistakes.'''
def validMoves(e):
    global letter_list_lower
    global letter_list_upper
    if e in letter_list_lower:
            pass
    elif e in letter_list_upper:
        print('The moves you entered is Uppercase. Please enter lowercase letters.')
    else:
        if len(e) == 0:
            print('You entered nothing.')
        else:
            print('The move you entered was a non-letter.')
    
    if len(e) >= 2:
        print('You have mistakenly entered more than one letter.')


'''This function is used to conduct moves in the solving puzzle process.'''
def move(e,dim,data,four_letters):
    key = data.index(' ')
    x = key // dim ; y = key % dim

    if e == four_letters[0]:
        if x == dim - 1:
            print("There's nothing to be moved up.")
            return 'Invalid Move'
        else:
            (data[x*dim + y],data[(x+1)*dim + y])=(data[(x+1)*dim + y],data[x*dim + y]) #switch between ' ' and the number behind
    
    elif e == four_letters[1]:
        if x == 0:
            print("There's nothing to be moved down.")
            return 'Invalid Move'
        else:
            (data[x*dim + y],data[(x-1)*dim + y])=(data[(x-1)*dim + y],data[x*dim + y])

    elif e == four_letters[3]:
        if y == 0:
            print("There's nothing to be moved right.")
            return 'Invalid Move'
        else:
            (data[x*dim + y],data[x*dim + (y-1)])=(data[x*dim + (y-1)],data[x*dim + y])
    
    elif e == four_letters[2]:
        if y == dim-1:
            print("There's nothing to be moved left.")
            return 'Invalid Move'
        else:
            (data[x*dim + y],data[x*dim + (y+1)])=(data[x*dim + (y+1)],data[x*dim + y])
    else:
        validMoves(e)
        return 'Invalid Move'
    

'''This function is to check whether the puzzle is solved after each move and end the round if solved.'''
def checkGame(dim,data):
    copy = [i for i in data]
    copy[copy.index(' ')] = dim**2
    if copy == sorted(copy):
        return True
    return False


def main():
    print("Welcome to Colin's puzzle game!")

    four_letters = four_key()
    
    count_win = 0

    while True:
        dim = get_dimension()

        if dim == 0:
            print('Now the Game ends.\nYou have won ' + str(count_win) + ' games.')
            exit()

        print(' ')
        
        data = [x for x in range(1,dim**2+1)]         # The list contains the puzzle
        setBoard(dim,data)
        printBoard(dim,data)

        count_move = 0
        while not checkGame(dim,data):
        
            m = input("Enter your move " + movable(dim,data,four_letters) + ": ")

            if move(m,dim,data,four_letters) == 'Invalid Move':
                count_move -= 1
            
            count_move += 1
            printBoard(dim,data)
            print(' ')

        count_win += 1
        print('Congrats, u win the Game with ' + str(count_move) + ' moves!')
        print(' ')
        
if __name__ == '__main__':
    main()