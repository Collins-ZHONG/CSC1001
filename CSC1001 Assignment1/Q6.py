
# Question VI

#选函数
functionUwant=str(input('Enter the function among "sin","cos" or "tan": '))

if functionUwant == 'sin':
    from math import sin
    def f(x):
        return sin(x)
elif functionUwant == 'cos':
    from math import cos
    def f(x):
        return cos(x)
elif functionUwant == 'tan':
    from math import tan
    def f(x):
        return tan(x)

else:
    print("Can't you type the 3 function what I gave you? I write the program, not you!") 
    exit()

from math import pi
#写定义域
try:
    a,b=eval(input('Enter 2 ends of the interval u want (If you want pi, just type "pi" or "n*pi"): '))
except:
    print('Plz type by following what I say. I write the code!')
    exit()
if a<b:
    #写那个点
    try:
        n=int(input('Enter the number of sub-intervals(must be integer): '))
    except:
        print('Integer! Integer!!!')
        exit()
    j=0
    for i in range(0,n+1):
        #检测f(x)可否套用
        #print(f(a+(b-a)/n*((i-1)-1/2)))
        #保留一个旧值用于和新值相加
        k=(b-a)/n*f(a+(b-a)/n*(i-1/2))
        j=j+k
    print(j,'is what u wanna get no matter what it is actually...')
elif a>=b:
    print('What result do you think you will reach with a interval which is only a point or does not exist?')