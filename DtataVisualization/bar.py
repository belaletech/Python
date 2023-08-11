import matplotlib.pyplot as plt 
# Data 
categories = ['A', 'B', 'C', 'D'] 
values = [10, 15, 7, 12] 
# Create bar plot 
plt.bar(categories, values) 
# Add labels and title 
plt.xlabel('Categories') 
plt.ylabel('Values') 
plt.title('Bar Plot') 
# Display the plot 
plt.show() 
