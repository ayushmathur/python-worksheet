class MarksException(Exception):
    def __init__(self, msg="Marks Exception"):
        super().__init__()
        self.msg=msg
    def __str__(self):
        print("str called")
        return self.msg
try:
    n=int(input("enter the marks"))
    if n<0 or n>100:
        print("raise exception")
        raise MarksException("Marks cannot be < 0 or > 100")
except MarksException as e:
        print("in marks exception")
        print(e)