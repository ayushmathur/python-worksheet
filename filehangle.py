fobj_in=open("example.txt")
fobj_out=open("excopy.txt","w")
i=1
for line in fobj_in:
    print(line.rstrip())
    fobj_out.write(str(i)+":"+line)
    i=i+1
fobj_in.close()
fobj_out.close()