class Cafe:
    def __init__(self,stock):
        self.coffee=stock
    def insert(self,money):
        if money<0:
            print('Pilice caught the thief')
        elif self.coffee>0:
            if money>300:
                self.coffee-=1
                print(str(self.coffee)+' coffee left')
                return money-300
            elif money<300:
                print(str(self.coffee)+' coffee left')
                return money
            else:
                self.coffee-=1
                print(str(self.coffee)+' coffee left')
                return None
        else:
            print('Closed')
        return money
ediya=Cafe(3)
print(ediya.insert(500))
