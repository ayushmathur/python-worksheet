emp=open("employee.dat")
data={}
for line in emp:
    line=line.rstrip()
    splitline=(line.split(","))
    if splitline[2] in data:
        data[splitline[2]]+=int(splitline[4])
    else:
        data[splitline[2]]=int(splitline[4])
print(data)
emp.close()