import pandas as pd
dic={"name":['python','c','c++','java'],"par":[12,13,14,15],"Rank":[1,4,3,2]}
var1=pd.Series(dic)
v2=pd.Series(12,index=[1,2,3,4,5,6])
v3=pd.Series(3,index=[1,2,3,4])
print(var1) 
print(v2)
print(v3)
print(v2+v3)