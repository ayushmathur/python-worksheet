import pandas as pd
#mydata = pd.read_table("http://bit.ly/chiporders")
#mymoviedata = pd.read_table("http://bit.ly/movieusers",sep="|",header=None)
mydata1=pd.read_csv("http://bit.ly/uforeports")
#print(type(mydata))
#print(mydata.head())
#print(mydata.tail())

#print(mydata1.City)
#print(mydata1["City"])
mydata1["location"]=mydata1.City + ","+ mydata1.State
print(mydata1["location"])