class Dog:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def bark(self):
        return f"{self.name} says Woof!"  
          
    def run(self):
        self.running = True