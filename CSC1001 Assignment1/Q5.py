# Question V
y=0
try:
    N=int(input('Enter an positive interger and I will show u all prime numbers smaller than it: '))
    if N <= 1:
        print('Do u think there are prime numbers smaller than',N,'','?')
    else:
        for i in range(2,N):
            priNum=False
            
            for w in range(2,i):
                # if i%w != 0:
                #     priNum=False
                if i%w == 0:
                    priNum=True
                    break

            if priNum == False:
                y+=1
                #换行操作
                #用一个变量，每print一个加一，加到八换行
                if y%8==1:
                    if y!=1:
                        print('')
                print(i,end=' ')
except:
    print('Interger! I mean interger!')