class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        
    def getName(self):
        return self.__name
    
    def getAge(self):
        return self.__age
    
    Name = property(getName)
    Age = property(getAge)
    
