class Employee:
    def __init__(self,name,id):
        self.name = name 
        self.id = id 
    def showDetails(self) :
        print (f"The name of Employee is: {self.name} and his ID is : {self.id}")
class programer (Employee) :
    def showLanguage (self) :
        print ("The default language is PYTHON")      
e = Employee("tomy","408")
e.showDetails()
e1 = programer ("jon","410")
e1.showDetails ()
e1.showLanguage ()