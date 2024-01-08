# Question II
import time
try:
    x=str(int(input('Enter an interger: ')))
    for i in x:
        print(i)
        time.sleep(0.5)
    
except:
    print('Interger, plz')