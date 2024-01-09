#### Please do not use input() function!!!
from random import random
class ecosystem(object):

    def __init__(self, river_len, num_fish, num_bear, steps):
        #######initialization#######
        self.river_len = river_len
        self.num_fish = num_fish
        self.num_bear = num_bear
        self.steps = steps
    
    def myRandint(self,a,b):    
        return int(a+(b-a)*random())  #random needs no argument

    def initialize(self):
        if self.num_bear+self.num_fish>self.river_len:
            print('Too many fishes and bears. Make sure your input is correct.')
            exit()
        elif self.river_len<=2:
            print('The river is too short.')
            exit()

        self.river=['N']*self.river_len
        # print(self.river)
        bLeft=self.num_bear
        fLeft=self.num_fish
        while bLeft>0:    #放熊
            # print(bLeft)
            location=self.myRandint(0,self.river_len)
            # print(location)
            if self.river[location]=='N':
                # print('check')
                self.river[location]='B'
                bLeft-=1
        while fLeft>0:   #放鱼
            # print(fLeft)
            location=self.myRandint(0,self.river_len)
            # print(location)
            if self.river[location]=='N':
                self.river[location]='F'
                fLeft-=1
        return self.river

    def printRiver(self):
        printList=[]
        for i in self.river:
            if i=='NB':
                i='B'
            elif i=='NF':
                i='F'
            printList.append(i)
        for j in printList:
            print(j,end=' ')
        print('')

    def __move__(self):
        lo=0
        # print(lo)
        skip=False
        for i in self.river:
            if skip==True:#########这一步是防止动物连着往右走或者熊连杀
                skip=False
            elif i!='N' and i!='NB' and i!='NF':
                if lo==0: #最左侧（not complete）
                    if 3*random()<1:
                        action=1
                        if i=='B':
                            animal='B'
                            if self.river[1]=='N' or self.river[1]=='F' or self.river[1]=='NF': #走或者吃鱼
                                self.river[1]='B'
                                self.river[0]='N'
                                skip=True                         #以免它下次再走一步
                            elif self.river[1]=='B' or self.river[1]=='NB': #breed
                                # print('check breed    b moves right')
                                self.breed('NB')
                        elif i=='F':
                            animal='F'
                            if self.river[1]=='N': #走
                                self.river[1]='F'
                                self.river[0]='N'
                                skip=True                           #以免下次再走
                            elif self.river[1]=='B' or self.river[1]=='NB': #被吃
                                self.river[0]='N'
                            elif self.river[1]=='F' or self.river[1]=='NF': #breed
                                # print('check breed    f moves right')
                                self.breed('NF')
                    else: 
                        action=0
                        if self.river[lo]=='B':
                            animal='B'
                        elif self.river[lo]=='F':
                            animal='F'

                elif lo==self.river_len-1: #最右侧（not complete）
                    # print('check')
                    if 3*random()<1:
                        action=-1
                        if i=='B':
                            animal='B'
                            if self.river[self.river_len-2]=='N' or self.river[self.river_len-2]=='F' or self.river[self.river_len-2]=='NF': #走或者吃鱼
                                self.river[self.river_len-2]='B'
                                self.river[self.river_len-1]='N'
                            elif self.river[self.river_len-2]=='B' or self.river[self.river_len-2]=='NB': #breed
                                # print('check breed    b moves left')
                                self.breed('NB')
                        elif i=='F':
                            animal='F'
                            if self.river[self.river_len-2]=='N': #走
                                self.river[self.river_len-2]='F'
                                self.river[self.river_len-1]='N'
                            elif self.river[self.river_len-2]=='B' or self.river[self.river_len-2]=='NB': #被吃
                                self.river[self.river_len-1]='N'
                            elif self.river[self.river_len-2]=='F' or self.river[self.river_len-2]=='NF': #breed
                                # print('check breed    f moves left')
                                self.breed('NF')
                    else: 
                        action=0
                        if self.river[lo]=='B':
                            animal='B'
                        elif self.river[lo]=='F':
                            animal='F'

                else:      #非两侧
                    x=random()
                    if 3*x<1: #往左
                        action=-1
                        if i=='B':
                            animal='B'
                            if self.river[lo-1]!='B' and self.river[lo-1]!='NB': # 吃鱼或者走
                                self.river[lo-1]='B'
                                self.river[lo]='N'
                            elif self.river[lo-1]=='B' or self.river[lo-1]=='NB': #breed
                                # print('check breed    b moves left')
                                self.breed('NB')
                        elif i=='F':
                            animal='F'
                            if self.river[lo-1]=='N': #走
                                self.river[lo-1]='F'
                                self.river[lo]='N'
                            elif self.river[lo-1]=='B' or self.river[lo-1]=='NB': #被吃
                                self.river[lo]='N'
                            elif self.river[lo-1]=='F' or self.river[lo-1]=='NF': #breed
                                # print('check breed    f moves left')
                                self.breed('NF')
                    elif 3*x>=2: #往右
                        action=1
                        if i=='B':
                            animal='B'
                            if self.river[lo+1]!='B' and self.river[lo+1]!='NB': #吃鱼或者走
                                self.river[lo+1]='B'
                                self.river[lo]='N'
                                skip=True                                                   #以免下次再走
                            elif self.river[lo+1]=='B' or self.river[lo+1]=='NB': #breed
                                # print('check breed    b moves right')
                                self.breed('NB')
                        elif i=='F':
                            animal='F'
                            if self.river[lo+1]=='N': #走
                                self.river[lo+1]='F'
                                self.river[lo]='N'
                                skip=True                                                    #以免下次再走
                            elif self.river[lo+1]=='B' or self.river[lo+1]=='NB': #被吃
                                self.river[lo]='N'
                            elif self.river[lo+1]=='F' or self.river[lo+1]=='NF': #breed
                                # print('check breed    f moves right')
                                self.breed('NF')
                    elif 1<=3*x<2: #不动
                        action=0
                        if self.river[lo]=='B':
                            animal='B'
                        elif self.river[lo]=='F':
                            animal='F'
                print('Animal: ',animal,', Action: ',action)
                print('The current ecosystem after the action:')
                self.printRiver()
                print(' ')
            lo+=1
        count=0
        for j in self.river:
            if j=='NB':
                self.river[count]='B'
            elif j=='NF':
                self.river[count]='F'
            count+=1
        return self.river
    
    def breed(self,e):
        while True:
            location=self.myRandint(0,self.river_len)
            # print(location,self.river[location],self.river)
            if self.river[location]=='N':
                self.river[location]=e
                break
            elif 'N' not in self.river:
                break

    def __steps__(self):
        initSteps=self.steps
        for i in range(initSteps):
            print('The ecosystem at the beginning of the step ',(initSteps+1)-self.steps,' is:')
            self.printRiver()
            print(' ')
            self.__move__()
            self.steps-=1
            
        return self.river

    def simulation(self):
        # You should follow the example format. Use print() tp display the result as given in AS3 read me.pdf. Do not use input()
        self.initialize()
        # print('check')
        # print(self.__steps__())
        self.__steps__()
        # print(a)

# test one
eco=ecosystem(5,2,1,3)
result_three=eco.simulation()

# test two
# eco=ecosystem(5,3,0,3)
# result_three=eco.simulation()

# test three
# eco=ecosystem(5,2,3,3)
# result_three=eco.simulation()