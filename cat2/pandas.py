import pandas as pd 
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # two-dimensional list 
df = pd.DataFrame(data, columns=['col1', 'col2', 'col3']) 
print(df)