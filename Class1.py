class Mnn0:
   no_of_leaves=8
   def __init__(self,jname,jage):
       self.name=jname
       self.age=jage

   def jojo(self):
      return f"THe name is {self.name}. and age is {self.age}"
   @classmethod
   def ch(cls,new):
      cls.no_of_leaves=new
   @classmethod
   def mb(cls,string):
      return cls(*string.split("/"))
   @staticmethod 
   def joj(sr):
       return f"Hello {sr}"
   
 
lass=Mnn0("laer",15)
jass=Mnn0("jaer",18)
khali=Mnn0.mb("KHALI/19")
lass.ch(88)
print(khali.name)

