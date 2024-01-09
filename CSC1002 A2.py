import turtle as t

'''
main idea:

use a lists-in-list(data) to represent chess board with cols and rows,
string contained initailly is '_', which would be replaced by color after a click on the turtle window
data[0][0] represents the chess on the bottom and left,
data[7][7] represents the chess on the top and right,
(others similar in the middle)
col represents vertical lines and row is horizontal

if the mouse is moving in specific area on x-axis, there would be high-light on the rectangular on the bottom
there are numercial transfer between locations and locations obtained by bind() function

use recursive function to check whether 4 or more chesses are connected, which is simple to solve
complicated situations

color and title need to be changed after each chess placed,
so in my coding, they are sychronous


mainly contains self_defined functions:

change()                which is used to change color of chess and title
check_full()            which is used to check whether a column is full or not
chess()                 which is used to draw a chess on the turtle window according to the list(data)
play()                  which is used to find certain location that where to place a chess
add_chess_to_board()    which put a color in to the list(data) to represent a chess in chessboard in logic
check_color()           which detects whether color is hoped, used in check_game()
hight_light()           which is used to highlight chesses at the locations in the given list(con_lt)
check_game()            which is used to check whether 4 or more chesses are connected  # Details are explained right above the function
check_board_full()      which is used to check whether the board is full
def retangle()          which is used to draw the lower rectangular
column_bound()          same as above but contains boarder data
emphasize_bound()       which is used to draw column tracker
column_tracker()        as what its name is

I also used Screen.cv.bind() to bind left click with function play()
and motion with function column_tracker()
'''

# Below are all important variables or steps I can hardly avoid during my coding

'''
I mistakenly consider that 2 player may choose color themselves so I add this process,
which causes more inconvenience, here I just make a simple adjustment to let it run as usual
'''
# while True:
#     color1 = input('Enter the color of Player 1: ').lower()
#     color2 = input('Enter the color of Player 2: ').lower()
#     try:     
#         t.pencolor(color1)
#         t.pencolor(color2)
#         break
#     except:
#         print("There's something wrong about colors you entered. Please try again")

# 创建空心turtle的方法：m = creatTurtle
def creatTurtle(x,y,color='red',border='black'):
    a=t.Turtle('Square')
    a.color(border,color)
    a.up()
    a.goto(x,y)
    return a

color1 = 'yellow'
color2 = 'blue'

'''
Setting up screen should be carried out in main(), but I didn't realize it at the beginning.
It's too late when I realize that and try to move this part into main(), which caused lots of error, so I just put it here
'''
scr = t.Screen()
scr.setup(430,450) 


'''use data[col][row] to index the chess board'''
'''They are set up globally to be used and changed in many functions'''
data = [['_' for j in range(8)] for i in range(8)]
col = 0 ; row = 0           # pointer to location in data

'''Basic beginning set-up'''
color = color1
color_copy = 'color'
title = 'Connect 4 - Player 1 Turn'

#below are setting pens
pen1 = t.Turtle()       # for drawing each step
pen1.pen(speed = 0)

pen2 = t.Turtle()       # for the column bound
pen2.pen(pencolor = 'black', fillcolor = 'black', speed = 0)

pen3 = t.Turtle()   # draw column tracker
pen3.pen(pensize = 5, speed = 0)

pen4 = t.Turtle()       # for high_light
pen4.pen(pensize = 4, pencolor = 'red', speed = 0)

pen1.hideturtle()
pen2.hideturtle()
pen3.hideturtle()
pen4.hideturtle()
t.hideturtle()


# below are variable for limitation
clicked = False
end = False



def change():
    global color, title, end
    if end:
        return
    
    if color == color1:   
        # Player 1 has ended his move
        title = 'Connect 4 - Player 2 Turn'
        color = color2

    elif color == color2:  
        # player 2 has ended his move
        title = 'Connect 4 - Player 1 Turn'
        color = color1
    
    t.title(title)


def check_full(col, data):
    if '_' not in data[col]:
        return True
    return False


def chess(color, goto):   # red or blue
    if goto == True:
        return

    change()
    # Go to a specific location to draw chess
    pen1.penup()
    pen1.goto(goto)
    pen1.pen(pencolor = color, fillcolor = color)
    pen1.pendown()

    pen1.pen(pencolor = color, fillcolor = color)
    pen1.seth(270)
    pen1.fd(10)
    pen1.lt(90)
    pen1.begin_fill()
    pen1.circle(20)
    pen1.end_fill()
    pen1.seth(270)
    pen1.backward(10)

    x = (goto[0] + 175)//50 ; y=(goto[1] + 175)//50
    check_game(data, color, x, y , direction = 0)

    return


def play(event):
    global col, clicked, color, end
    x = event.x

    if end:
        return
    
    col0 = 0
    left_bound = 15 ; right_bound = 55
    for i in range(8):
        if left_bound <= x <= right_bound:
            col = col0                                   # locate the newly added chess in column
            clicked = True
            chess(color, add_chess_to_board(col, color))
            break
        left_bound += 50 ; right_bound += 50        # move the location to the next
        col0 += 1

    return

def add_chess_to_board(col, color):
    '''only incurred once, changing data during exclusion and return the location in turtle window with orgin at the center'''
    global data, row
    if check_full(col, data):
        return True

    row = data[col].index('_')                           # locate the newly added chess in row
    data[col][row] = color
    
    # print(col,row)
    # check_game(data, color, col, row, 0)

    x = -175 + 50*col ; y = -165 + 50*row
    
    return x,y

'''No need to change every variable so just put them all in arguments'''
def check_color(data, col, row, color):
    if (col < 0) or (col > 7) or (row < 0) or (row > 7):    # Out of range
        return False                                        
    
    else:
        check = data[col][row]
        if check == color:                                  # Color is the same 
            return True
        elif check == '_':                                  # empty, not out, no color
            return False

        else: return False                                  # not the same color


def hight_light(connected_list):
    locations = list(map(lambda lt_loc:(lt_loc[0]*50 - 175, lt_loc[1]*50 - 153), connected_list))         # x = -175 + 50*col ; y = -165 + 50*row
    # print(locations)

    pen4.pencolor(color3)
    for i in locations:
        pen4.penup()
        pen4.goto(i)
        pen4.seth(270)
        pen4.fd(21)
        pen4.pendown()
        pen4.lt(90)
        pen4.circle(20)


'''No need to change data, col, row and color, so put them in arguments rather than global'''
'''
Use recursion to check the connected chesses in different directions so that double connected or
5-or-more connected could all be detected. Also, recursive method starts from each new chess
in the chessboard and there's no need to check every chesses on the board
'''
def check_game(data, color, col, row, direction, con_lt = []):
    global title, end

    connected = 0
    if direction == 0:
        for i in range(1,5):
            if i == 1:
                con_lt1 = []
                con1 = check_game(data, color, col, row, 1, con_lt1) + check_game(data, color, col, row, 5, con_lt1) + 1
                # print(con_lt, '1', con)
                if con1 >= 4:            # Win in 'right-up' to 'left-down' direction
                    connected = con1
                    # print(con_lt1)
                    # con_lt1.append((col, row))
                    end = True
                    for i in con_lt1:            
                        con_lt.append(i)

            elif i == 2: 
                con_lt2 = []
                con2 = check_game(data, color, col, row, 2, con_lt2) + check_game(data, color, col, row, 6, con_lt2) + 1
                # print(con_lt)       #########check######### No Problem
                if con2 >= 4:
                    connected = con2
                    # con_lt2.append((col, row))
                    end = True
                    # print(con_lt2)
                    for i in con_lt2:
                        con_lt.append(i)
            
            elif i == 3:
                con_lt3 = []
                con3 = check_game(data, color, col, row, 3, con_lt3) + check_game(data, color, col, row, 7, con_lt3) + 1
                # print(con_lt, '3', con)
                if con3 >= 4:
                    connected = con3
                    # con_lt3.append((col, row))
                    end = True
                    # print(con_lt3)
                    for i in con_lt3:
                        con_lt.append(i)
            
            elif i == 4:        # down
                con4 = 1
                con_lt4 = []
                if row <= 2:
                    pass
                elif row >= 3:
                    a = row
                    # print(col,a)
                    while (data[col][a] == color) and (a>=0):

                        
                        con4 += 1
                        con_lt4.append((col,a))
                        a -= 1
                
                    if con4 >= 4:
                        connected = con4
                        for i in con_lt4[1:]:
                            con_lt.append(i)
                        end = True
                    else:
                        # con_lt = con_lt[:1-con]
                        if end == False:
                            con_lt = []

        if connected >= 4:      
                      # The game ends
            # print(con_lt,'Hello Hello')
            con_lt.reverse()
            con_lt.append((col, row))
            con_lt.reverse()
            # print(con_lt)
            hight_light(con_lt)

            if title == 'Connect 4 - Player 1 Turn':
                t.title('Winner - Player 2')
            elif title == 'Connect 4 - Player 2 Turn':
                t.title('Winner - Player 1')
        else: 
            if check_board_full(data):
                end = True
                t.title('Game Ties')
        return 
    
    #####------Below are recursive parts------#####
    
    elif direction == 1:            # right-up
        if check_color(data, col+1, row+1, color):
            con_lt.append((col+1, row+1))
            return 1 + check_game(data, color, col+1, row+1, 1, con_lt)
        else: return 0
    
    elif direction == 2:            # right
        if check_color(data, col+1, row, color):
            con_lt.append((col+1, row))
            return 1 + check_game(data, color, col+1, row, 2, con_lt)
        else: return 0
    
    elif direction == 3:            # right-down
        if check_color(data, col+1, row-1, color):
            con_lt.append((col+1, row-1))
            # print(con_lt)
            return 1 + check_game(data, color, col+1, row-1, 3, con_lt)
        else: return 0
    
    
    
    elif direction == 5:            # left-down
        if check_color(data, col-1, row-1, color):
            con_lt.append((col-1, row-1))
            return 1 + check_game(data, color, col-1, row-1, 5, con_lt)
        else: return 0
    
    elif direction == 6:            # left
        if check_color(data, col-1, row, color):
            con_lt.append((col-1, row))
            return 1 + check_game(data, color, col-1, row, 6, con_lt)
        else: return 0
    
    elif direction == 7:            # left-up
        if check_color(data, col-1, row+1, color):
            con_lt.append((col-1, row+1))
            return 1 + check_game(data, color, col-1, row+1, 7, con_lt)
        else: return 0

def check_board_full(data):
    for i in data:
        if '_' in i:
            return False
    return True
    
def retangle():
    pen2.seth(0)
    pen2.begin_fill()
    for i in range(2):
        pen2.fd(40)
        pen2.rt(90)
        pen2.fd(10)
        pen2.rt(90)
    pen2.end_fill()
    return

def column_bound():
    x = -195
    for i in range(8):
        pen2.penup()
        pen2.goto(x,-195)   
        pen2.pendown()
        retangle()
        x += 50               # Set the destination of next move of pen2
    '''
    [(-195,-155)(15,55)], [(-145,-105)(65,105)], [(-95,-55)(115,155)], [(-45,-5)(165,205)]
    [(5,45)(215,255)],    [(55.95)(265,305)],    [(105,145)(315,355)], [(155,195)(365,405)]
    '''
    return

def emphasize_bound(x):
    # pen3.clear()
    t.tracer(0)
    pen3.penup()
    pen3.goto(x-1,-194)
    pen3.seth(0)
    pen3.pendown()
    pen3.pen(pencolor = color)

    for i in range(2):
        pen3.fd(42)
        pen3.rt(90)
        pen3.fd(12)
        pen3.rt(90)
    t.tracer(1)
    return

'''
The use of timer_id could lower the frequency of refreshing so that maximum of recursion can hardly be reached
However, the problem left is that the column highlight cannot last long if the mouse stays still. That's the problem
'''
timer_id = None
x_ranges = [(15, 55), (65, 105), (115, 155), (165, 205), (215, 255), (265, 305), (315, 355), (365, 405)]

def column_tracker(event):
    global end, timer_id
    
    if end:
        scr.cv.unbind_all('<Motion>')
        scr.cv.unbind_all('<Button-1>')
        pen3.clear()
        return

    x = event.x
    for i, (x1, x2) in enumerate(x_ranges):
        if x1 <= x <= x2:
            emphasize_bound((x1 - 210))
            if timer_id is not None:
                scr.cv.after_cancel(timer_id)
            timer_id = scr.cv.after(100, pen3.clear)
            break
    else:
        if timer_id is not None:
            scr.cv.after_cancel(timer_id)
            timer_id = None
            
    return

def main():
    global data, color, col, row, title, color1, color2, color3

    color3 = list(filter(lambda x: (x != color1) and (x != color2), ['red', 'purple', 'blue']))[0]

    scr.tracer(0)
    t.title('Connect 4')
    column_bound()
    t.title('Connect 4 - Player 1 Turn')

    
    scr.cv.bind('<Button-1>', play)
    scr.cv.bind('<Motion>', column_tracker)

    t.mainloop()
main()