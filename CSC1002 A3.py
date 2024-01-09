import turtle
import random
from functools import partial

g_screen = None
g_snake = None
g_monster = None
g_snake_sz = 5
g_intro = None
g_keypressed = None
g_status = None

COLOR_BODY = ("blue", "black")
COLOR_HEAD = "red"
COLOR_MONSTER = "purple"
FONT = ("Arial",16,"normal")

KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT, KEY_SPACE = \
       "Up", "Down", "Left", "Right", "space"

HEADING_BY_KEY = {KEY_LEFT:180, KEY_RIGHT:0, KEY_UP:90, KEY_DOWN:270}


'''Below are self-designed variables'''
x_s, y_s = 0, 0 ; x_m, y_m = 0, 0
snake_pos = []
# keys_list = [ KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN]
g_time = 0
g_timer = None
g_contact = 0
g_ccounter = None
# This list should work as a Queue using functions such as ._pop() ._append()
PAUSE = False
BOUNDED = [None, None, False, False]
# 0: for horizontal key if snake is on left/right bound; 1: for vertical key if snake is on up/down bound;
BODY = [[None, None, None, None], False]    # Left-Right-Up-Down
# Whether 4 direction are bounded (begin with unbounded)
# Since directions can be bounded at the same time, so us a list to deal with multi-bounded cases
'''
I made a mistake in the setting of BOUNDED, PAUSE and BODY.
They could connect to the same only variable to stop the snake.
And I still hadn't realized it until I finished PAUSE and BOUNDED, which are considerably figured out and cannot be developed
So, in order to avoid changing lots of things I've written, I write BODY, and the 3 are totaly independent.
'''
END = False
# This shows game end or not

# So, here is my general statement of this program
'''
About Assignment itself:
This Assignment is finished by myself based on the file Kinley uploaded on blackboard with assistance of Chat-GPT
(But I didn't let it to write code for me, I am not available to open-ai so I can't send file to it.
And its code written with my weird requirements, since the requirements of assigment is weird, is useless in most cases.
So I pledge I am not in academic dishonesty. I only use it if I want to know whether there's some functions that can help me
realize the function of what I want.)

About the content:
Use 3 independent lists to stop the snake (reason is what I stated before)
Use a Queue based on built-in list (no class) to denote locations of head and each body nodes of the snake
The interactions like contact or eat are based on locations in xy-coordination stored in variables,
which means I didn't actually build a coordination system but just store those positions in number and check whether some positions are in a certain range
For example, 
if the location of food is the same of location of head of the snake, snake would eat it;
if the location of head of the snake is in a certain range surrounding the monster, the game will be called end
if the location of each body node of the snake is in a certain range surrounding the monster, 1 contact will be counted

About my writing process:
Mostly I spend short time on the assignment every day for a very long period since there are another ddls,
so sometimes I forget what did I do and that really lower my efficiency.
But I still cannot figure out how to avoid basic logic problems in beginning processes like setting the PAUSE, BOUNDED and BODY
variables this time. It would be much better if I could use only one boolean to stop the snake.
Perhaps I would write the whole file over again or just practise my thinking over lots of such programs
'''


def configurePlayArea():

    # motion border
    m = createTurtle(0,0,"","black")
    m.shapesize(25,25,5)
    m.goto(0,-40)  # shift down half the status

    # status border 
    s = createTurtle(0,0,"","black")
    s.shapesize(4,25,5)
    s.goto(0,250)  # shift up half the motion

    # introduction
    intro = createTurtle(-200,150)
    intro.hideturtle()
    intro.write("Click anywhere to start the game .....", font=("Arial",16,"normal"))
    
    # statuses
    status = createTurtle(0,0,"","black")
    status.hideturtle()
    status.goto(-200,s.ycor()) 

    '''Below are pens added in imitation of the above doing similar jobs'''
    # timer, used to draw time in the game
    timer = createTurtle(150,250)
    timer.hideturtle()
    timer.write('Time:0', font=('arial',15,'bold'))

    # contact-counter, used to draw contact times in the game
    counter = createTurtle(-20,250)
    counter.hideturtle()
    counter.write('Contact:0', font=('arial',15,'bold'))

    return intro, status, timer, counter

def configScreen():
    s = turtle.Screen()
    s.tracer(0)    # disable auto screen refresh, 0=disable, 1=enable
    s.title("Snake based by Colin Zhong, based on Kinley Lam's.")
    s.setup(500+120, 500+120+80)
    s.mode("standard")
    return s

# create turtle, red is head and body is black
def createTurtle(x, y, color="red", border="black"):
    t = turtle.Turtle("square")
    t.color(border, color)
    t.up()
    t.goto(x,y)
    return t

def updateStatus():
    global PAUSE

    g_status.clear()
    if PAUSE:               # Self added, to draw Paused if paused
        g_status.write('Motion:Pauesd', font=('arial',15,'bold'))
    else:
        g_status.write('Motion:'+str(g_keypressed), font=('arial',15,'bold'))
    g_screen.update()

def setSnakeHeading(key):
    if key in HEADING_BY_KEY.keys():
        g_snake.setheading( HEADING_BY_KEY[key] )

def onArrowKeyPressed(key):
    global g_keypressed, PAUSE, BOUNDED
    '''key here represent the key newly pressed, g_keypressed represent the key pressed the last time'''
    # The game ends
    if END:
        return

    if key == KEY_SPACE:
        if PAUSE:
            PAUSE = False
        elif PAUSE is not True:
            PAUSE = True
    else:
        # if press the key that is bounded, skip it
        if (BOUNDED[2] == True) and (key == BOUNDED[0]):
            pass
        elif (BOUNDED[3] == True) and (key == BOUNDED[1]):
            pass
        else:
            if (key in BODY[0]):    # Means the direction of the key is bounded, skip it
                pass
            else:
                if PAUSE:   # all direction can unpause as long as not bounded
                    PAUSE = False
                g_keypressed = key
                setSnakeHeading(key)
    updateStatus()
    
def onTimerSnake():
    global PAUSE, BOUNDED, BODY, END, x_s, y_s, snake_pos, g_snake_sz, foodList#, g_keypressed # The snake could run without press at the very beginning
    
    # Game ends - Player win
    if checkFoodEaten():
        g_snake.write('Winner!!', font=('arial',15,'bold'))
        END = True
        g_screen.update()

    # The game ends
    if END:
        return

    if g_keypressed == None:
        # The snake could run without press at the very beginning with the code behind
        # g_keypressed = KEY_RIGHT
        g_screen.ontimer(onTimerSnake, 300)
        return
    
    if PAUSE == False:

        if (g_keypressed in BOUNDED) and (True in BOUNDED):     #
            pass 
        else:
            if g_keypressed in BODY[0] and (BODY[1]):
                pass
            else:

                # Clone the head as body
                g_snake.color(*COLOR_BODY)
                g_snake.stamp()
                g_snake.color(COLOR_HEAD)
                # Denote location of the snake
                if len(snake_pos) == g_snake_sz + 1:
                    snake_pos.pop()     # Can be considered as dequeue
                # Advance snake
                g_snake.forward(20)
                
                # Locate the head of the snake, noticing there exists slight errors
                # And add the location to a list, which is a Queue built on list
                snake_pos = [(round(g_snake.xcor()), round(g_snake.ycor()))] + snake_pos

                # Shifting or extending the tail.
                # Remove the last square on Shifting.
                if len(g_snake.stampItems) > g_snake_sz:
                    g_snake.clearstamps(1)

                # Game ends - Player lose
                '''
                Codes behind is also put in onTimerMonster because if snake is faster, the moster may not sense its passing by
                While in some cases moster may be faster, so I also put it here.
                It doesn't matter if 'Game Over!' is written twice overlapped.
                '''
                if (abs(x_s-x_m) < 20) and (abs(y_s-y_m) < 20):
                    g_monster.write('Game Over!', font=('arial',15,'bold'))
                    END = True


        # Stop the Snake on boundary
        x_s, y_s = round(g_snake.xcor()), round(g_snake.ycor())

        # Bounded on edges
        '''Horizontal: (-240, 240)   Vertical:(-280, 200)'''
        if (x_s >= 240): 
            BOUNDED[0] = KEY_RIGHT
            if (g_keypressed == KEY_RIGHT):
                BOUNDED[2] = True
        elif (x_s <= -240):  
            BOUNDED[0] = KEY_LEFT
            if(g_keypressed == KEY_LEFT): 
                BOUNDED[2] = True
        else: BOUNDED[0] = None; BOUNDED[2] = False     # if not, then unbounded, that's how I think BOUNDED is too limited

        if (y_s >= 200): 
            BOUNDED[1] = KEY_UP
            if (g_keypressed == KEY_UP): 
                BOUNDED[3] = True
        elif (y_s <= -280): 
            BOUNDED[1] = KEY_DOWN
            if (g_keypressed == KEY_DOWN):
                BOUNDED[3] = True
        else: BOUNDED[1] = None; BOUNDED[3] = False     # unbounded

        # Bounded on body (turning back can be also classified as bounded by body)
        # buttoms occuring in BODY[0] refers to block in the direction of the buttom and it cannot be used
        # True occuring in BODY[1] refers to the snake has to stop 
        if (x_s + 20, y_s) in snake_pos[1:]:            # Bounded by right
            BODY[0][1] = KEY_RIGHT
        else: BODY[0][1] = None
        if (x_s - 20, y_s) in snake_pos[1:]:            # Bounded by left
            BODY[0][0] = KEY_LEFT
        else: BODY[0][0] = None
        if (x_s, y_s + 20) in snake_pos[1:]:            # Bounded by up
            BODY[0][2] = KEY_UP
        else: BODY[0][2] = None
        if (x_s, y_s - 20) in snake_pos[1:]:            # Bounded by down
            BODY[0][3] = KEY_DOWN
        else: BODY[0][3] = None
        if g_keypressed in BODY[0]:
            BODY[1] = True
        else: BODY[1] = False

        # Eat
        '''
        Key idea in this part is use a list containing 4 different information of the food
        (value,location,hidden(boolean),eaten(boolean))
        skip if it's hidden
        turn the eaten to True if it's not eaten and not hidden and the location of snake is where the food is
        '''
        for i in range(5):    
            if True in foodList[i][2:]:
                pass
            elif [x_s, y_s] in foodList[i]:
                stamp_len = foodList[i][0]
                foodList[i][3] = True
                penList[i].clear()
                g_snake_sz += stamp_len

    g_screen.update()
    
    '''
    Part behind is the operation lower the speed of the snake when its body is growing
    The key point is directly increase the variable noting the length of the stamp,
    since the source code with function of incresasing length
    and the length is increased before stamp
    '''
    if len(g_snake.stampItems) > 4:
        '''Ensure no slowing down at the beginning. But if eat right at the beginning, it will slow down after the length of snake is 5'''
        if (len(g_snake.stampItems) < g_snake_sz):
            fre = 500
        else: fre = 300
    else: fre = 300
    g_screen.ontimer(onTimerSnake, fre)

# Self added
def makeFood():
    global foodList

    '''Horizontal: (-240, 240)   Vertical:(-280, 200)'''
    foodList = []
    num = 0
    while len(foodList) < 5:
        x = 20*random.randint(0, 24) - 240
        y = 20*random.randint(0, 24) - 280

        if (x, y) != (0, 0) and (x, y) not in foodList:
            num += 1
            foodList.append([num, [x, y], False, False])    
            # (number, location, hided(False is not hided), eaten)
            '''
            Actually could use "delete" method to function as the eaten(boolean)
            But in my first version I didn't notice the specfic requirement of refreshing food,
            and my own version is not in capacity of such method
            '''
    return foodList

# Self added
def setFood():
    global penList
    # food goes to the place
    '''
    foodList is used to match the location system of snake
    copy is used to adjust the location of each food make them visually at their correct positions
    '''
    # I wondered that is there a way to simplify the following steps but fail to figure out since pens are need to be assigned before put into penList
    copy = []
    for i in foodList:
        copy.append((i[1][0], i[1][1]-7))
    pen1 = turtle.Turtle() ; pen1.hideturtle() ; pen1.penup()
    pen2 = turtle.Turtle() ; pen2.hideturtle() ; pen2.penup()
    pen3 = turtle.Turtle() ; pen3.hideturtle() ; pen3.penup()
    pen4 = turtle.Turtle() ; pen4.hideturtle() ; pen4.penup()
    pen5 = turtle.Turtle() ; pen5.hideturtle() ; pen5.penup()
    pen1.goto(copy[0]) ; pen1.pendown() ; pen1.write(1, font=('arial',10,'bold'))
    pen2.goto(copy[1]) ; pen2.pendown() ; pen2.write(2, font=('arial',10,'bold'))
    pen3.goto(copy[2]) ; pen3.pendown() ; pen3.write(3, font=('arial',10,'bold'))
    pen4.goto(copy[3]) ; pen4.pendown() ; pen4.write(4, font=('arial',10,'bold'))
    pen5.goto(copy[4]) ; pen5.pendown() ; pen5.write(5, font=('arial',10,'bold'))
    penList = [pen1, pen2, pen3, pen4, pen5]
    

'''
Randomly pick a food 
1.hide it if it's unhidden
2.unhide it if it's hidden
'''
# Self added
def onTimerFood():
    global foodList, g_snake_sz

    # The game ends
    if END:
        return

    remainFood = list(filter(lambda food: food[3] == False, foodList))      # Randomly pick up food not eaten
    random.shuffle(remainFood)
    pick = remainFood[0][0] - 1
    if foodList[pick][3] == True:
        pass
    else:
        if foodList[pick][2] == False:
            foodList[pick][2] = True
            penList[pick].clear()
        else: 
            foodList[pick][2] = False
            penList[pick].write(pick + 1, font=('arial',10,'bold'))
        
        g_screen.update()

    g_screen.ontimer(onTimerFood, 1000*random.randint(3,7))     # Refresh the codition of the food in a random frequence from every 3-7 seconds

# Self added
def checkFoodEaten():   # Very intuitive and I don't think there's ideas I have to explain
    foodEaten = list(filter(lambda food: food[3] == True, foodList))
    if len(foodEaten) == 5:
        return True
    return False

# Self added
def setMonster():
    # Set the moster in a fair distance with the snake
    # Whatever, it's far enough and random
    # Ensured not cross the boundary
    if (2 * random.random() - 1) >= 0: p = 1
    else: p = -1

    x = 10
    while (x == 10) or (x == -10):
        x = 20 * random.randint(-10, 10) + 10 * p

    y = (220 - abs(x)) * p
    g_monster.goto(x, y)
    return(x, y)

# Self added
def dirMonster():
    # direct moster in the direction towards the snake
    global x_s, y_s, x_m, y_m
    x, y = g_monster.pos()
    x_m, y_m = round(x), round(y)
    if (x_s or y_s) == None:
        return 0
    
    hor = x_s - x_m ; ver = y_s - y_m

    # Adjust to locations after each move
    if abs(hor) > abs(ver):
        if hor > 0:
            x_m += 20
            return 0
        else: 
            x_m -= 20
            return 180
    else:
        if ver < 0: 
            y_m -= 20
            return 270
        else:           
            y_m += 20
            return 90

# Self added
'''check the surrounding of the monster'''
def checkContact():
    global g_contact
    for i in [(x_m+10, y_m+10), (x_m+10, y_m-10), (x_m-10, y_m+10), (x_m-10, y_m-10)]:
        if i in snake_pos[1:]:  # Locations of the snake excluding the head
            g_contact += 1
            return True
    return False


def onTimerMonster():
    global END
    
    # The game ends
    if END:
        return

    g_monster.setheading(dirMonster())
    g_monster.forward(20)

    if checkContact():
        g_ccounter.clear()
        g_ccounter.write('Contact:' + str(g_contact), font=('arial',15,'bold'))

    '''
    Codes behind is also put in onTimerSnake because if snake is so fast, the moster may not sense its passing by
    While in some cases moster may be faster, so I also put it here
    '''
    if (abs(x_s-x_m) < 20) and (abs(y_s-y_m) < 20):
        g_monster.write('Game Over!', font=('arial',15,'bold'))
        END = True
    
    g_screen.update()
        
    # The game ends
    if END:
        return
    
    # Below is regarding the speed(refreshing rate) of moster
    '''
    I have something to say about this:
    It's really hard to figure out what is "slight" actually.
    Since Monster goes directly to the head, in the actual process, if the speed of monster is similar to the snake(sometimes even higher),
    then the game would be extemly hard, since snake often goes around the outer lap while monster is in the inner lap,
    meaning the distance the monster goes is much smaller than that of the snake.
    Plus the refreshing of food, it would be really time-costing and tedious for player.
    In addition, the difference of less than 100ms is really hard to be observed, so I expand the time limit on the right side,
    making there's obervable difference.
    While the slightly faster would make game harder, unless I write another function to change the possibility of such situation,
    but it is very dreary and I don't think it's essential according to the requirements in the file.
    So I make it really "slight", you could see from the numbers below in comparison with the speed of the snake.
    
    However, it's fact that you could see changes of the speed of the monster.
    You may not be able to observe the speed of snake and monster, but you could see all requirements are met in the codes.
    '''
    g_screen.ontimer(onTimerMonster, 5 * random.randint(55,120))

# Self added
'''Just denote and write time of game.'''
def onTimerTimer():
    global g_time

    # The game ends
    if END:
        return

    g_timer.clear()
    g_timer.write('Time:'+ str(g_time), font=('arial',15,'bold'))
    g_time += 1
    g_screen.ontimer(onTimerTimer, 1000)

def startGame(x,y):
    g_screen.onscreenclick(None)
    g_intro.clear()

    # The food should be seen as game started, but I didn't write function to hide all food before the game
    # So I simply put them in startGame not in main function
    makeFood()
    setFood()
    
    g_screen.onkey(partial(onArrowKeyPressed,KEY_UP), KEY_UP)
    g_screen.onkey(partial(onArrowKeyPressed,KEY_DOWN), KEY_DOWN)
    g_screen.onkey(partial(onArrowKeyPressed,KEY_LEFT), KEY_LEFT)
    g_screen.onkey(partial(onArrowKeyPressed,KEY_RIGHT), KEY_RIGHT)
    g_screen.onkey(partial(onArrowKeyPressed,KEY_SPACE), KEY_SPACE)

    
    g_screen.ontimer(onTimerSnake, 300)
    g_screen.ontimer(onTimerMonster, 500)
    # below are self added
    g_screen.ontimer(onTimerFood, 3000)
    g_screen.ontimer(onTimerTimer, 1000)

if __name__ == "__main__":
    g_screen = configScreen()
    g_intro, g_status, g_timer, g_ccounter = configurePlayArea()
    
    updateStatus()

    g_monster = createTurtle(-110,-110,"purple", "black")
    g_snake = createTurtle(0,0,"red", "black")
    x_m, y_m = setMonster()

    g_screen.onscreenclick(startGame)

    g_screen.update()
    g_screen.listen()
    g_screen.mainloop()