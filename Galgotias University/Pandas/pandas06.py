import pandas as pd
d={'a':["Belal","Ahmad","Nehal","Ayan","Raza"],'b':[1.2,2,3,4,5],'c':[6,7,8,9,10]}
var=pd.DataFrame(d,columns=["a"],index=['b','c','d','e','f'])
print(var)
print(type(var))
print(var['a'][3])
