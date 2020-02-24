class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def Name(self):
        return self.name
        
    def Age(self):
        return self.age
    
class Customer(Person):
    def __init__(self, name, age, adr, tel):
        super().__init__(name, age)
        self.adr = adr
        self.tel = tel
        
    def Name(self):
        self.name = "氏名：　" + self.name
        return self.name
    
    def Adr(self):
        return self.adr
    
    def Tel(self):
        return self.tel
    
 