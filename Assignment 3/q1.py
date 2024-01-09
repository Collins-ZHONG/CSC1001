#### Please do not use input() function!!!
class Flower(object):
    def __init__(self, Name, petals, price):
        # Name:flower name
        # petals: number of petals
        # price
        self.Name = self.checkName(Name)
        self.petals = self.checkPetals(petals)
        self.price = self.checkPrice(price)

    def Information(self):
        if self.Name==None or self.petals==None or self.price==None:
            return 'Please make sure your inputs are correct.'
        # use return to display the result instead of using print function. You should follow the example format. Do not use input()
        info = 'Here is the information of your flower. Name: '+str(self.Name)+', Number of petals: '+str(self.petals)+', price: '+str(self.price)+'.'
        print(info)
        return info  # e.g. "Here is the information of your flower. Name: juice, Number of petals: 5, price: 7.82"
    
    def checkName(self,Name):
        if type(Name)==str:
            return Name
        else:
            print('The input of the flower name is incorrect. A string is required.')
            return
    def getName(self,Name):
        return self.Name
    def setName(self,name):
        if bool(type(name)==str):
            self.Name=name
            return self.Name
        else:
            print('The input Name is not Valid.')
            return None
    
    def checkPetals(self,Petals):
        if type(Petals)==int:
            return Petals
        elif type(Petals)==float:
            if Petals==int(Petals):
                return int(Petals)
            else:
                print('The input of the number of petals is incorrect. An integer is required.')
        else:
            print('The input of the number of petals is incorrect. An integer is required.')
            return None
    def getPetals(self):
        return self.petals
    def setPetals(self,petals):
        if bool(type(petals)==int):
            self.petals=petals
            return self.petals
        else:
            print('The input Petals is not valid.')

    def checkPrice(self,Price):
        if type(Price)==float or type(Price)==int:
            return round(Price,2)
        else:
            print('The input price is incorrect. An float number or integer is required.')
    def getPrice(self):
        return self.price
    def setPrice(self,price):
        if bool(type(price) == ('float' or 'int')):
            self.price=round(price,2)
            return self.price
        else:
            print('The input Price is not valid.')
            return None

# def initiallize():
#     f=Flower('Catus',46.0,3.67)
#     f.Information()
# #     f.setName('a')
# #     f.setPetals(16)
# #     f.setPrice(500)
# #     print(f.Information())
# #     f.setName(3)
# #     f.setPetals(2.3)
# #     f.setPrice(102.45)
# #     print(f.Information())
# initiallize()

# test one
# flower=Flower('juice',5,7.82)
# result_one=flower.Information()

# test two
# flower=Flower(666,5,7.82)
# result_one=flower.Information()

# test three
# flower=Flower('juice',5.21,7.82)
# result_one=flower.Information()