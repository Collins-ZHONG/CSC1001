
def isValid(number):
    ''' Return True if the card number is valid.
    param number: The card number.
    return: True of False
    '''
    ########### Start your code ############
    if 13<=len(str(number))<=16:
        if str(number).startswith('4') or str(number).startswith('5') or str(number).startswith('37') or str(number).startswith('6'):
            x=sumOfOddPlace(number)+sumOfDoubleEvenPlace(number)
            if x%10==0:
                return str(number)+' is Valid'
            else:
               return str(number)+' is InValid'
        else:
            return 'The password is incorrect. There is no such bank.'
    else:
        return 'The password is incorrect.'
    ############ End your code #############

def sumOfDoubleEvenPlace(number):
    ''' Get the result from step 2.
    param number: The card number.
    return: Sum of double even place.
    '''
    ########### Start your code ############
    def reverse(x):### This is not an function required to be defined but it makes later steps easier. #########
        x0=str(x)
        l=len(x0)
        b=''
        for i in x0:
            a=i
            b=a+b
        return b#最后结果是str
    from math import floor
    l=[]
    for i1 in reverse(number):
        l.append(i1)
    sumOfDoubleEvenPlace=0
    for i2 in range(1,floor(len(l)/2+1)):
        #print(2*i2,len(l),round((len(l)+1)/2)) ##检验
        if 2*i2>len(l):
          a=0
        elif 2*i2<=len(l):
            a=2*int(l[2*i2-1])
        a=getDigit(a)
        sumOfDoubleEvenPlace+=int(a)
    #print(sumOfDoubleEvenPlace)######################cheeeeeeeeeeeck
    return sumOfDoubleEvenPlace
    ############ End your code #############

def getDigit(number):
    ''' Get digit of the number. For instance: getDigit(5) = 5, getDigit(15) = 6.
    param number: A number who only has one or two digits.
    return: Return this number if it is a single digit, otherwise return the sum of the two digits.
    '''
    ########### Start your code ############
    if number>=10:
        b=0
        for i in str(number):
            b+=int(i)
        number=b
    return number
    ############ End your code #############

def sumOfOddPlace(number):
    ''' Return the sum of odd place digits in number.
    param number: The card number.
    return: The sum of odd place digits.
    '''
    ########### Start your code ############
    def reverse(x):
        x0=str(x)
        l=len(x0)
        b=''
        for i in x0:
            a=i
            b=a+b
        return b#最后结果是str


    l=[]
    for i1 in reverse(number):
        l.append(i1)
    sumOfOddPlace=0
    for i2 in range(0,round((len(l)+1)/2)):
        if 2*i2>len(l):
            a=0
        elif 2*i2<=len(l):
            a=int(l[2*i2])
        sumOfOddPlace+=int(a)
    #print(sumOfOddPlace)##check##################
    return sumOfOddPlace
    ############ End your code #############


if __name__ == '__main__':
    # Example test cases
    # Note: there will be more test cases in scoring
    ans1 = isValid(4388576018402626)
    ans2 = isValid(4388576018410707)
    print(ans1,ans2)
    ######## We will judge the correctness by examing the result of isValid() function. #########