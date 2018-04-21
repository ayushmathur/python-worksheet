import re
p=re.compile(r'\d+')
#s=p.findall('12 drummers drumming,100 pipers piping,10 lords a-leaping')
#print(s)
print(p.search('no class at all'))



iterator=p.finditer('12 drummers drumming,100 pipers piping,10 lords a-leaping,200,688')
print(iterator)
for match in iterator:
    print(match.span())
    print(match.group())