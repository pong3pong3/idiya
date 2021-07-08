class Cafe:
    def __init__(self,stock):
        self.coffee=stock
    def insert(self,money):
        while self.coffee>0:
            if money>300:
                self.coffee-=1
                print('Existence of '+str(self.coffee)+' coffee')
                return money-300
            elif money<300:
                print('Existence of '+str(self.coffee)+' coffee')
                return money
            else:
                self.coffee-=1
                print('Existence of '+str(self.coffee)+' coffee')
                return None
        print('Closed')
        return money
ediya=Cafe(3)
print(ediya.insert(500))
