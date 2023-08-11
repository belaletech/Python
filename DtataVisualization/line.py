import matplotlib.pyplot as plt 
import numpy as np 
# Generate data 
x = np.linspace(0, 10, 100) 
y = np.sin(x) 
# Create line plot 
plt.plot(x, y) 
# Add labels and title 
plt.xlabel('X-axis') 
plt.ylabel('Y-axis') 

plt.title('Line Plot') 
# Display the plot 
plt.show() 
