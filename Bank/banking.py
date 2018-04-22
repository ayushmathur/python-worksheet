import ast
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
    def calcinterest(self):
        self.interest=float(self.balance)+(float(self.balance)*self.intrate)

class Current(Account):
    def __init__(self,id=0,name="",email="",mobile=0,balance=0,username=""):
        super().__init__(id,name,email,mobile,balance)
        self.username=username
        self.pin=9999
        self.type="Current"
    def calcinterest(self):
        self.interest=float(self.balance+100)

def addaccount():
    typ=int(input("Enter the type of account\n1. Savings Account\n2. Current Account\nOr press 9 to go back\n"))
    if typ == 1:
        name=input("Enter new Savings account holder's name: ")
        email=input("Enter Email ID: ")
        mob=input("Enter Mobile Number: ")
        bal=int(input("Enter opening balance amount: "))
        id=sorted(data.keys())[-1]+1
        chqno=id+251000
        obj=Savings(id,name,email,mob,bal,chqno)
        obj.calcinterest()
        data[obj.id]=obj.__dict__
        print("New account successfully created with ID = "+str(obj.id)+"\n")
        interface()
    elif typ == 2:
        name=input("Enter new Current account holder's name: ")
        email=input("Enter Email ID: ")
        mob=input("Enter Mobile Number: ")
        bal=int(input("Enter opening balance amount: "))
        uname=input("Enter unique username: ")
        id=sorted(data.keys())[-1]+1
        obj=Current(id,name,email,mob,bal,uname)
        obj.calcinterest()
        data[obj.id]=obj.__dict__
        print("New account successfully created with ID = "+str(obj.id)+"\n")
        interface()
    elif typ == 9:
        interface()
    else:
        print("Incorrect Choice, please try again")
        addaccount()

def deleteaccount():
    x=input("Are you sure you want to delete an account(y/n)?")
    if x in ['y','Y']:
        number=int(input("Enter the account number to be deleted: "))
        del data[number]
        print("Account Deleted successfully.\n")
        interface()
    elif x in ['n','N']:
        interface()
    else:
        print("Incorrect Choice, please try again")
        deleteaccount()

def deposit():
    x=input("Are you sure you want to record a Deposit to an account(y/n)?")
    if x in ['y','Y']:
        number=int(input("Enter the account number to be updated: "))
        amount=float(input("Enter the Amount: "))
        data[number]['interest'] += amount
        print("Record updated. New Balance= "+str(data[number]['interest'])+"\n")
        interface()
    elif x in ['n','N']:
        interface()
    else:
        print("Incorrect Choice, please try again")
        deposit()
def withdrawl():
    x=input("Are you sure you want to record a Withdrawl to an account(y/n)?")
    if x in ['y','Y']:
        number=int(input("Enter the account number to be updated: "))
        amount=float(input("Enter the Amount: "))
        data[number]['interest'] -= amount
        print("Record updated. New Balance= "+str(data[number]['interest'])+"\n")
        interface()
    elif x in ['n','N']:
        interface()
    else:
        print("Incorrect Choice, please try again")
        withdrawl()

def transfer():
    x=input("Are you sure you want to record a Transfer between two accounts(y/n)?")
    if x in ['y','Y']:
        acc1=int(input("Enter the account number to be debited: "))
        acc2=int(input("Enter the account number to be cerdited: "))
        amount=float(input("Enter the Amount to be transfered: "))
        data[acc1]['interest'] -= amount
        data[acc2]['interest'] += amount
        print("Records updated. New Balance:\n"+str(acc1)+" : "+str(data[acc1]['interest'])+"\n"+str(acc2)+" : "+str(data[acc2]['interest'])+"\n")
        interface()
    elif x in ['n','N']:
        interface()
    else:
        print("Incorrect Choice, please try again")
        withdrawl()

def balance():
    x=int(input("Enter account number: "))
    print("Balance of account "+str(x)+" = "+str(data[x]['interest'])+"\n")
    interface()

def terminate():
    with open("datarecord.txt",'w') as dfile:
        for key, value  in data.items():
            dfile.write('%s=>%s\n' % (key, value))
    print("Data written to file successfully\n")
    exit

def terminateerror():
    print("\nIncorrect Choice, Try Again\n")
    interface()

switcher = {
    1: addaccount,
    2: deleteaccount,
    3: deposit,
    4: withdrawl,
    5: transfer,
    6: balance,
    7: terminate
}

def interface():
    choice=int(input("Welcome to Banking system.\n1. Add new Account\n2. Delete an existing account\n3. Record a deposit\n4. Record a withdrawl\n5. Record a transfer\n6. Check balance of an account\n7. Exit\nEnter a choice: "))
    func = switcher.get(choice,terminateerror)
    func()

def initialize():
    #Initialize dictionary
    with open("datarecord.txt") as raw_data:
        for item in raw_data:
            if '=>' in item:
                item=item.rstrip()
                key,value = item.split('=>', 1)
                key=int(key)
                data[key]=ast.literal_eval(value)  #Used module ast here to convert String in "value" into a Dictionary which is assumed to be in dictionay format already
            else:
                pass
    interface()

data={}
initialize()