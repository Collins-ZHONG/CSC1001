
def emirps_100():
    '''
    Displays the first 100 emirps. Display 10 numbers per line and align the numbers properly.
    This function does not need a return value. 
    '''
    ########### Start your code ############
    ### hint: When aligh the numbers, monospaced font will be helpful.
    def reverse(x):
    
        x0=str(x)
        l=len(x0)
        b=''
        for i in x0:
        #先记录第一个数字
        #把第一个数字和无相加
        #再记录第二个数字
        #第二个数字和第一个数字相加
        #记录结果为第三个数字
            a=i
            b=a+b
        return eval(b)#最后结果是个数

    def isPrimeNumber(n):
        for i in range(2,round(n/2)+1):
            if n%i==0:
                return False
            elif n%i!=0:
                continue
        return True

    def isPalindromic(n):
        a=reverse(n)
        if a==n:
            return True
        if a!=n:
            return False

    def isEmirp(n):
    #print('检验1',n)
        if isPrimeNumber(n)==True and isPalindromic(n)==False and isPrimeNumber(reverse(n))==True:
            return True

#------------这下面是你输入几就给你几个符合要求的数字-------------#
    def main1():
        try:
            numberOfNumbers=int(input('An integer of number of emirps: '))
        except:
            print('So I just consider you input 100.')
            numberOfNumbers=100
        n=2
        count=0
        while count<numberOfNumbers:
            if isEmirp(n)==True:
                count+=1
                print('%4s'%n,end=' ')
                if count%10==0:
                    print(' ')
            n+=1
#-----------这里截止----------#

#----------这下面是你输入几就给你全部小于等于这个数字的符合要求的式子----------#
    def main2():
        from math import floor
        try:
            x=floor(float(input('An real positive number so that I will show you emirps smaller than it: ')))
            if x<=0:
                print('Positive,Positive,Positive!')
                exit()
            elif x<=12:
                print('Do u think a number smaller than this will be emirp?')
                exit()
        except:
            print('Did you enter a NUMBER?')
            exit()
        n=2
        count=0
        while n<=x:
            if isEmirp(n)==True:
                count+=1
                print('%4s'%n,end=' ')
                if count%10==0:
                    print(' ')
            n+=1
#----------这里截止----------#

#main1() # Enter x and it will return x emirps
#main2() # Enter x and it will return all emirps not bigger than x
    
    def main3():
        numberOfNumbers=100
        n=13
        count=0
        while count<numberOfNumbers:
            if isEmirp(n)==True:
                count+=1
                print('%4s'%n,end=' ')
                if count%10==0:
                    print(' ')
            n+=1
    main3()

    ############ End your code #############

if __name__ == '__main__':
    emirps_100()

    # You can just print your solution. Like this:
    #    13   17   31   37   71   73   79   97  107  113
    #   149  157  167  179  199  311  337  347  359  389
    # ...