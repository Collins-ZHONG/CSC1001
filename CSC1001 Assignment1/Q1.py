# Question I
try:
    x=eval(input('Enter the final account value: '))
    y=eval(input('Enter the annual interest rate: '))*0.01
    z=eval(input('Enter the number of years: '))

    n=x/(1+y)**z
    print('The initial account value is',n,'.')
except:
    print('Please enter number')