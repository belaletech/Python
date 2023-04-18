

import matplotlib.pyplot as plt
x=["python",'c','c++','java',"c#","html",'css']
y=[85,70,65,82,10,20,30]
plt.bar(x,y,width=0.6,color="b")

plt.title("Bar Graph",fontsize=36,color='g')
plt.xlabel("Programming language",fontsize=15,color='g')
plt.ylabel("NO")
plt.show()