import pandas as pd
x=[1,2,3,4,5]
var=pd.Series(x,dtype="float")

print(var)
print(type(var))
print(var[4])
#a=[6,7,8,9,10]
#y=pd.Series(a,dtype="float")
#a=pd.Series(y,index=['a','b','c','d','e'],dtype="flot",name="python")
x=pd.Series(var,index=['a','b','c','d','e'],dtype="flot",name="python")
print()