
class User:
    name:str
    surname:str
    age:int
    gender:str
    status =[]
    point:int

    def __init__(self,name,surname,age,gender,point,personelNumber):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
        self.point=point
        self.personelNumbers=personelNumber
     

    def get_name(self):
        return self.name
    def get_surname(self):
        return self.surname
    def get_age(self):
       return self.age         
    def get_status(self):
        return self.status 
    def get_gender(self):
        return self.gender
    def get_point(self):
        return self.point
    def get_personelNumbers(self):
        return self.personelNumbers



    def set_personelNumbers(self,personelNumbers):
        self.personelNumbers =personelNumbers

        
    def set_point(self,point):
        self.point = point
   

    def set_gender(self, gender):
        self.gender = gender

    def set_name(self, name):
        self.name = name
 
    def set_surname(self,surname):
        self.surname = surname
  
    def set_age(self,age):
        self.age = age

    def set_status(self, status):
        self.status.append(status)
