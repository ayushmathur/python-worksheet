class Account:
    def __init__(self,id=0,name="",email="",mobile=0,balance=0):
        self.id=id
        self.name=name
        self.email=email
        self.mobile=mobile
        self.balance=balance

class Savings(Account):
    def __init__(self,id=0,name="",email="",mobile=0,balance=0,checque=0):
        super().__init__(id,name,email,mobile,balance)
        self.cheque=checque
        self.intrate=0.04
        self.type="Savings"
    def calcsal(self):
        self.interest=self.balance*self.intrate

class Current(Account):
    def __init__(self,id=0,name="",email="",mobile=0,balance=0,username=""):
        super().__init__(id,name,email,mobile,balance)
        self.username=username
        self.pin=9999
        self.type="Current"
    def calcsal(self):
        self.interest=self.balance+100

def addaccount():
    typ=int(input("Enter the type of account\n1. Savings Account\n2. Current Account\nOr press 9 to go back\n"))
    if typ == 1:
        #Do something about ID and chq no
        name=input("Enter new Savings account holder's name: ")
        email=input("Enter Email ID: ")
        mob=input("Enter Mobile Number: ")
        bal=input("Enter opening balance amount: ")
        obj=Savings(101,name,email,mob,bal,1001)
        data={obj.id:obj.__dict__}
        print("New account successfully created with ID = "+str(obj.id)+"\n")
        interface()
    elif typ == 2:
        #Do something about ID and chq no
        name=input("Enter new Current account holder's name: ")
        email=input("Enter Email ID: ")
        mob=input("Enter Mobile Number: ")
        bal=input("Enter opening balance amount: ")
        uname=input("Enter unique username: ")
        obj=Current(102,name,email,mob,bal,uname)
        data={obj.id:obj.__dict__}
        print("New account successfully created with ID = "+str(obj.id)+"\n")
        interface()
    elif typ == 9:
        interface()
    else:
        print("Incorrect Choice, please try again")
        addaccount()

def deleteaccount():
    pass

def deposit():
    pass

def withdrawl():
    pass

def transfer():
    pass

def balance():
    pass    

def terminate():
    exit

def terminateerror():
    print("\nIncorrect Choice, Try Again")
    interface()

switcher = {
    1: addaccount,
    2: deleteaccount,
    3: deposit,
    4: withdrawl,
    5: transfer,
    6: balance,
    7: terminate,
}

def interface():
    choice=int(input("Welcome to Banking system. Enter a choice: \n1. Add new Account\n2. Delete an existing account\n3. Record a deposit\n4. Record a withdrawl\n5. Record a transfer\n6. Check balance of an account\n7. Exit\n"))
    func = switcher.get(choice,terminateerror)
    func()

def initialize():
    #Initialize dictionary
    interface()
data={}
initialize()