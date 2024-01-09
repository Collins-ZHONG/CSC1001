"""
You are permitted to write code between Start and End.
Besides, you can write other extra functions or classes outside, 
but don't change the template.
"""
class Stack:
    def __init__(self,n):
        self.data=[]
        self.size=0
        self.n=n
    def __len__(self):
        return self.size
    def is_empty(self):
        return self.size==0
    def push(self,e):
        self.data.append(e)
        self.data.append(False)
        self.size+=2
    def initPush(self,e):
        self.data.append(e)
        self.size+=1
    def top(self):
        if self.is_empty():
            return None
        else:
            return self.data[self.__len__()-1]
    def topNumber(self):
        if self.is_empty():
            return None
        else:
            if self.top()==False:
                return self.data[self.__len__()-2]
            else:
                return self.top()
    def _pop(self):
        if self.is_empty():
            print('The Stack is empty.')
            return None
        else:
            a=self.data.pop()
            self.size-=1
            return a
    def __str__(self):
        return str(self.data)

def getBiggest(a,b,c,n):
    if a==None:
        a=n+1
    elif a==False:
        a=0
    if b==None:
        b=n+1
    elif b==False:
        b=0
    if c==None:
        c=n+1
    elif c==False:
        c=0
    if (a>b) and (a>c):
        return 'a'
    elif (b>a) and (b>c):
        return 'b'
    elif (c>a) and (c>b):
        return 'c'
def getSmallest(a,b,c,n):
    if a==None:
        a=n+1
    elif a==False:
        a=n+2
    if b==None:
        b=n+1
    elif b==False:
        b=n+2
    if c==None:
        c=n+1
    elif c==False:
        c=n+2
    if (a<b) and (a<c):
        return 'a'
    elif (b<a) and (b<c):
        return 'b'
    elif (c<a) and (c<b):
        return 'c'

def xtoy(x,y):
    y.push(x._pop())
    
def dif(a,b):
    if (a==None) or (b==None):
        return False
    elif(a==False) or (b==False):
        return False
    elif (a-b)%2==1:
        return True
    else: return False

def sp(a,b,c,aN,bN,cN):

    if a==None:
        if b==False:
            if dif(bN,c) and (bN>c):
                return 'c-→b'
        elif c==False:
            if dif(b,cN) and (cN>b):
                return 'b-→c'
    elif b==None:
        if a==False:
            if dif(aN,c) and (aN>c):
                return 'c-→a'
        elif c==False:
            if dif(a,cN) and (cN>a):
                return 'a-→c'
        
    elif c==None:
        if b==False:
            if dif(bN,a) and (bN>a):
                return 'a-→b'
        elif a==False:
            if dif(b,aN) and (aN>b):
                return 'b-→a'
    else:
        if a==False:
            if dif(aN,b) and (aN>b):
                return 'b-→a'
            elif dif(aN,c) and (aN>c):
                return 'c-→a'
            elif dif(b,c):
                if b>c:
                    return 'c-→b'
                elif c>b:
                    return 'b-→c'
        elif b==False:
            if dif(bN,a) and (bN>a):
                return 'a-→b'
            elif dif(bN,c) and (bN>c):
                return 'c-→b'
            elif dif(a,c):
                if a>c:
                    return 'c-→a'
                elif c>a:
                    return 'a-→c'
        elif c==False:
            if dif(cN,b) and (cN>b):
                return 'b-→c'
            elif dif(cN,a) and (cN>a):
                return 'a-→c'
            elif dif(a,b):
                if a>b:
                    return 'b-→a'
                elif b>a:
                    return 'a-→b'
    # print('called')
    return None

# from time import sleep

def HanoiTower(n, from_rod ='A',aux_rod ='B',to_rod ='C'):
    result_list = []
    # Start writing your code.
    from_rod=Stack(n)
    for i in range(n):
        from_rod.initPush(n-i)
    aux_rod=Stack(n)
    to_rod=Stack(n)
    if n%2==0:#偶数
        aux_rod.push(from_rod._pop())
        result_list.append('A--→B')
    elif n%2==1:#奇数
        to_rod.push(from_rod._pop())
        result_list.append('A--→C')
    # print(result_list)

    while True:   #第二此往后开始挪
        # sleep(1)

        a=from_rod.top()
        b=aux_rod.top()
        c=to_rod.top()
        aN=from_rod.topNumber()
        bN=aux_rod.topNumber()
        cN=to_rod.topNumber()
        # print(a,b,c,'        ',aN,bN,cN)
        if (cN==n) and ((from_rod.is_empty()) or (aux_rod.is_empty)):
            if n%2==0:#偶数
                if from_rod.is_empty():
                    g=to_rod._pop()
                    to_rod.push(aux_rod._pop())
                    result_list.append('B--→C')
                    cN=to_rod.topNumber()
                elif aux_rod.is_empty(): pass
            n-=1
        if (from_rod.is_empty()) and (aux_rod.is_empty()):
            break

        big=getBiggest(a,b,c,n)
        small=getSmallest(a,b,c,n)

        # print(from_rod,'   and "a": ',a)
        # print(aux_rod,'   and "b": ',b)
        # print(to_rod,'   and "c": ',c)

        # print('挪动前')
        # print(from_rod)
        # print(aux_rod)
        # print(to_rod)
        #这一步是清False
        if a==False:
            from_rod._pop()
        elif b==False:
            aux_rod._pop()
        elif c==False:
            to_rod._pop()
        
        if cN==n:
            cN==None
        x=sp(a,b,c,aN,bN,cN)
        if x=='a-→b':
            xtoy(from_rod,aux_rod)
            result_list.append('A--→B')
        elif x=='b-→a':
            xtoy(aux_rod,from_rod)
            result_list.append('B--→A')
        elif x=='a-→c':
            xtoy(from_rod,to_rod)
            result_list.append('A--→C')
        elif x=='c-→a':
            xtoy(to_rod,from_rod)
            result_list.append('C--→A')
        elif x=='b-→c':
            xtoy(aux_rod,to_rod)
            result_list.append('B--→C')
        elif x=='c-→b':
            xtoy(to_rod,aux_rod)
            result_list.append('C--→B')
        else:
            #没有奇偶不同数优先挪空的
            if small=='a':
                if b==None:
                    xtoy(from_rod,aux_rod)
                    result_list.append('A--→B')
                elif c==None:
                    xtoy(from_rod,to_rod)
                    result_list.append('A--→C')
            elif small=='b':
                if a==None:
                    xtoy(aux_rod,from_rod)
                    result_list.append('B--→A')
                elif c==None:
                    xtoy(aux_rod,to_rod)
                    result_list.append('B--→C')
            elif small=='c':
                if a==None:
                    xtoy(to_rod,from_rod)
                    result_list.append('C--→A')
                elif b==None:
                    xtoy(to_rod,aux_rod)
                    result_list.append('C--→B')
            # if (small=='a') and (big=='b'):
            #     xtoy(from_rod,aux_rod)
            #     result_list.append('A--→B')
            # elif (small=='b') and (big=='a'):
            #     xtoy(aux_rod,from_rod)
            #     result_list.append('B--→A')
            # elif (small=='a') and (big=='c'):
            #     xtoy(from_rod,to_rod)
            #     result_list.append('A--→C')
            # elif (small=='c') and (big=='a'):
            #     xtoy(to_rod,from_rod)
            #     result_list.append('C--→A')
            # elif (small=='b') and (big=='c'):
            #     xtoy(aux_rod,to_rod)
            #     result_list.append('B--→C')
            # elif (small=='c') and (big=='b'):
            #     xtoy(to_rod,aux_rod)
            #     result_list.append('C--→B')
        
        # print('这一次挪完后')
        # print(from_rod)
        # print(aux_rod)
        # print(to_rod)
        # print(' ')
        
        if (from_rod.is_empty()) and (aux_rod.is_empty()):
            break
    # print(from_rod)
    # print(aux_rod)
    # print(to_rod)
    # End writing your code.
    return result_list


"""
You should store each line your output in result_list defined above.
For example, if the outputs of print() are: 
                A --> C
                A --> B
then please store them in result_list:

strs = "A --> C"
result_list.append(strs)
strs = "A --> B"
result_list.append(strs)

Thus, once you want to print something, please store them in result_list immediately, 
rather than utilizing print() to print it. 
Don't miss the space! For example, don't output:
                A-->C
                A-->B

We will utilize the code similar to the following to check your answer.
"""

if __name__ == '__main__':
    n = 4
    result_list = HanoiTower(n)
    for item in result_list:
        print(item)