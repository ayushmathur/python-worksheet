import pandas as pd
import numpy as np
#mydata = pd.read_table("http://bit.ly/chiporders")
#mymoviedata = pd.read_table("http://bit.ly/movieusers",sep="|",header=None)
#mydata1=pd.read_csv("http://bit.ly/uforeports")
#print(type(mydata))
#print(mydata.head())
#print(mydata.tail())

#print(mydata1.City)
#print(mydata1["City"])
#mydata1["location"]=mydata1.City + ","+ mydata1.State
#print(mydata1["location"])
#print(mydata1.columns)

#ufo_cols=['col1','col2','col3','col4','col5','col6']
#mydata1.columns=ufo_cols
#print(mydata1.columns)
#print(mydata1.loc[mydata1['City']=="Chicago"])

#mydata2=pd.read_csv("data.csv")
#print(mydata2.head())
#print(mydata2.describe())

df = pd.DataFrame({'A':'foo bar foo bar foo bar foo bar foo'.split(),'B':'one one two two three two two one three'.split(),'C':np.arange(9),'D':np.arange(9)*2})
print(df)
print(df.loc[df['A']=='foo'])
print(df.mean())
print(df.loc[df['B'].isin(['one','three'])])
