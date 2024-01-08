# Question IV
import time

try:
    N=int(input('Enter the number of row of the list u want: '))
    m=1
    if N < 0:
        time.sleep(0.5)
        print('Can there be minus line?')
    else:
        time.sleep(0.5)
        print('%-8s%-8s%-8s'%('m','m+1','m**(m+1)'))
        while m<N+1:
            time.sleep(0.5)
            print('%-8d%-8d%-8d'%(m,m+1,m**(m+1)))
            m+=1
except:
    time.sleep(0.5)
    print('Numbers, plz')