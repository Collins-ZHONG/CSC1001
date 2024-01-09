#### Please do not use input() function!!!
class process_derivative(object):

    def __init__(self, polynominal):
        self.polynominal = polynominal

    def get_first_derivative(self):
        # You should follow the example format. Do not use input()
        def derive(aVari):
            if '*' in aVari:#Whether it is a constant
                if '^' in aVari:#Whether it is linear
                    a=aVari.split('^')
                    power=a[1]
                    if power==0:
                        return None
                    b=a[0].split('*')
                    times=b[0]
                    if times=='0':
                        return None
                    vari=b[1]
                    try:
                        vari==eval(vari)
                        return None
                    except:pass
                    newtimes=int(times)*int(power)
                    if int(power)==2:
                        return str(newtimes)+'*'+str(vari)
                    elif int(power)>=3:
                        return str(newtimes)+'*'+str(vari)+'^'+str(int(power)-1)
                    elif int(power)==1:
                        return times
                    elif int(power)==0:
                        return None
                else:#It is linear
                    a=aVari.split('*')
                    times=a[0]
                    if times==0:
                        return None
                    vari=a[1]
                    try:
                        vari==eval(vari)
                        return None
                    except: pass
                return str(times)
            else:#It is a constant or 一次式
                try:
                    aVari==eval(aVari) #constant
                    return ''
                except:
                    if '*' in aVari:
                        a=aVari.split('*')[0]
                        times=int(a[0])
                        # print(times)
                        if times==0:
                            # print('check')
                            return None
                 
                        if '^' in a[1]:
                            vari=a[1].split('^')[0]
                            power=int(a[1].split('^')[1])
                            try:
                                vari==eval(vari)
                                return None
                            except:
                                pass
                            if power==2:
                                return str(power*times)+vari
                            elif power==0:
                                return None
                            elif power==1:
                                return str(times)
                            else:
                                return str(power*times)+vari+str(power-1)
                        else:
                            return str(times)
                
                    else:
                        aVari
                        if aVari.startswith('-'):
                            a=aVari[1:]
                            if '^' in a:
                                vari=a.split('^')[0]
                                try:
                                    vari==eval(vari)
                                    return None
                                except: pass
                                power=int(a.split('^')[1])
                                if power==2:
                                    return '-'+str(power)+vari
                                elif power==1:
                                    return '-1'
                                elif power==0:
                                    return None
                                else:
                                    return '-'+str(power)+vari+str(power-1)
                            else:
                                return '-1'
                        else:
                            a=aVari
                            if '^' in a:
                                vari=a.split('^')[0]
                                try:
                                    vari==eval(vari)
                                    return None
                                except: pass
                                power=int(a.split('^')[1])
                                if power==2:
                                    return str(power)+vari
                                elif power==1:
                                    return '1'
                                elif power==0:
                                    return None
                                else:
                                    return str(power)+vari+str(power-1)
                            else:
                                return '1'


        def splitFunction(polynominal):
            count=0
            allVari=[]
            #加上第一项
            allVari.append(polynominal.split('+')[0].split('-')[0])
            # print(polynominal.split('+')[0].split('-')[0])

            #第二项开始的所有项
            for i in polynominal:
                # print(i)  #check √
                if i=='+':#正项
                    county=count+1
                    j=None
                    for j in polynominal[count+1:]:
                    # print(polynominal[count+1:]) #check √
                    # print(j)
                        if j=='+' or j=='-':#下一个正负号前结尾
                            aVari=polynominal[count+1:county]
                            # print(count,county,aVari)
                            break
                        if county>=len(polynominal)-1:#到底了结尾
                            aVari=polynominal[count+1:]
                            # print(count,county,aVari)
                            break
                        county+=1
                    allVari.append(aVari)
                elif i=='-':#负项
                    k=None
                    county=count+1
                    for k in polynominal[count+1:]:
                        if k=='+' or k=='-':
                            aVari='-'+polynominal[count+1:county]
                            break
                        if county>=len(polynominal)-1:
                            aVari='-'+polynominal[count+1:]
                            break
                        county+=1
                    allVari.append(aVari)

                count+=1
            # print(allVari)#check
            return allVari

        all2=[]
        result_two=''
        allVari=splitFunction(self.polynominal)
        
        # print(allVari)
        # count=0
        # for i in allVari:
        #     if i==None:
        #         print('check')##################3
        #         count1=count+1
        #         for j in allVari[count:]:
        #             if count1<=len(allVari)-1:
        #                 allVari[count1-1]=allVari[count1]
        #             count1+=1
        #         allVari.pop()
        #     count+=1

        allVari.reverse()
        vari2=derive(allVari.pop())
        if vari2!=None:
            all2.append(vari2)
        allVari.reverse()
        for aVari in allVari:
            if aVari.startswith('-'):
                vari3=derive(aVari)
                if vari3!=None:    
                    all2.append(vari3)
            else:
                vari3=derive(aVari)
                if vari3!=None:
                    all2.append('+'+vari3)
        # print(all2)            #################check#################
        if all2[-1]=='+':# the last one is empty if the anti-derivative ends with a constant
            all2.pop()
        for a in all2:
            result_two+=a
        if result_two=='': # in case only a constant is input
            result_two='0'    
        if result_two[0]=='+':
            result_two=result_two[1:]
        
        # result_two = 'your calculator result'
        print("The first derivative is: " + result_two )
        return "The first derivative is: " + result_two  # e.g. "The first derivative is: '6*x^2+6*x+5'"

# test one
# test_one=process_derivative('2*x^3+3*x^2+5*x+1')
# result_two=test_one.get_first_derivative()

# test two
# test_two=process_derivative('2*y^3+3*y^2+5*y+1')
# result_two=test_two.get_first_derivative()

# test three
# test_three=process_derivative('0*x^3+3*x^2+5*x+1^0')
# result_two=test_three.get_first_derivative()

# test four
# test_four=process_derivative('2*x^6-3*x^8+5*x+1')
# result_two=test_four.get_first_derivative()

# test five
# test_five=process_derivative('5')
# result_two=test_five.get_first_derivative()