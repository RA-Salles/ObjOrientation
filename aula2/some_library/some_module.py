class Duck():
    """ Uma tentativa de modelar um pato """
    
    
    def __init__(self,name,age,weight):
        
        self.name= name
        self.age= age
        self.weight= weight
        
    
    def speak(self):
        
        print('\nQuack.. quack..\n')
        
    
    def swim(self):
        
        print(self.name.title() + " is now swiming!")


    
        
        