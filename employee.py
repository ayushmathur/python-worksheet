class Employee:
    def __init__(self,id=0,name="",sal=0,dg="",dt=""):
        self.empno=id
        self.ename=name
        self.sal=sal
        self.dept=dg
        self.desg=dt
    def __str__(self):
        return str(self.empno)+" "+self.ename+" "+str(self.sal)+" "+self.dept+" "+self.desg

emp1=Employee(10,"Dom",5000,"HR","IT")
print(emp1)

class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return str(self.x)+" "+str(self.y)
    def __radd__(self,ob):
        a=self.x+ob
        b=self.y+ob
        return Point(a,b)
    def __add__(self,ob):
        if isinstance(ob,Point):
            a=self.x+ob.x
            b=self.y+ob.y
        else:
            a=self.x+ob
            b=self.y+ob
        return Point(a,b)
    def __rmul__(self,ob):
        a=self.x*ob
        b=self.y*ob
        return Point(a,b)
    def __mul__(self,ob):
        if isinstance(ob,Point):
            a=self.x*ob.x
            b=self.y*ob.y
        else:
            a=self.x*ob
            b=self.y*ob
        return Point(a,b) 
    def __rsub__(self,ob):
        a=self.x-ob
        b=self.y-ob
        return Point(a,b)
    def __sub__(self,ob):
        if isinstance(ob,Point):
            a=self.x-ob.x
            b=self.y-ob.y
        else:
            a=self.x-ob
            b=self.y-ob
        return Point(a,b)          
p1=Point(20,40)
p2=Point(10,50)
p3=p1+p2
p4=p1+10
p5=20+p2
p6=p1*p2
p7=p1*10
p8=20*p2
p9=p1-p2
p10=p1-10
p11=20-p2
print(p3)
print(p4)
print(p5)
print(p6)
print(p7)
print(p8)
print(p9)
print(p10)
print(p11)