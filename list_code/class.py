class person :
    
    def __init__(self,n,occ):
        
        self.name = n
        self.occupation = occ
        
    def info (self) :
        print (f"{self.name} is a {self.occupation}") 
        
        
a = person("Jawad","HR")
b = person("Ali","Dveloper")
a.info ()
b.info ()