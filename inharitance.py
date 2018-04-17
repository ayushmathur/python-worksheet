class Person:
    def __init__(self,name="",id=0,mob=0):
        self.id=id
        self.name=name
        self.mob=mob
    def __str__(self):
        return str(self.id)+" "+self.name+" "+str(self.mob)

class Employee(Person):
    def __init__(self,name="",id=0,dept="",desg="",mob=0):
        super().__init__(name,id,mob)
        self.dept=dept
        self.desg=desg
    def __str__(self):
        return super().__str__()+" "+self.dept+" "+self.desg
    
class Salaried(Employee):
    def __init__(self,name="",id=0,dept="",desg="",mob=0,sal=0):
        super().__init__(name,id,dept,desg,mob)
        self.sal=sal
    def calcsal(self):
        self.netpay=self.sal+(10/100)*self.sal+(15/100)*self.sal-(8/100)*self.sal
        return "Net Salary :"+str(self.netpay)
    def __str__(self):
        return super().__str__()+" "+str(self.sal)

class Contract(Employee):
    def __init__(self,name="",id=0,dept="",desg="",mob=0,rate=0,time=0):
        super().__init__(name,id,dept,desg,mob)
        self.rate=rate
        self.time=time
    def calcsal(self):
        return "Net payment: "+str(self.rate*self.time)
    def __str__(self):
        return super().__str__()
p1=Salaried("Dom",101,"HR","HOD",1234567899,40900)
print(p1)
c1=Contract("Lucy",102,"IT","Developer",1234567899500,500,120)
print(c1.calcsal())
print(p1.calcsal())