import re
multistring="""something somewhere
someotherthing"""
if(re.match("some",multistring)):
    print("found some")
else:
    print("not found some")
print(re.match('someother',multistring))
print(re.match("^someother",multistring,re.M))
print(re.search('someother',multistring,re.M))

#match finds pattern only at the beginning
print(re.match("somew",multistring,re.M))
#search finds pattern anywhere in the string
print(re.search("somew",multistring,re.M))
print(re.search("^someother",multistring,re.M))

m=re.compile('thing',re.M)

print("no match", m.match(multistring))#no match
print("match found",m.match(multistring,pos=4))#match

text="How are you? use sub u"
print(text)
#count indiciates how many occurances to replace
#if count=0 replaces all occurances of word u
print(re.sub(r'\b[uU]\b','you',text,count=0))
print(m.search(multistring,re.M))