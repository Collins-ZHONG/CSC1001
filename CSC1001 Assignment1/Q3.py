# Question III
import time
try:
    m=int(input('Enter an positive interger and I will show you a least "n" so that n**2 >= the number: '))
    if m>=0:
        n=0
        while n*n < m:
            n+=1
        time.sleep(0.5)
        print('Here is the "n" u have: ',n)
    else:
        print('Positive, plz')
except:
    print('Interger, plz')