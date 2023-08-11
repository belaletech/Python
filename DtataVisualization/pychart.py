import matplotlib.pyplot as plt 
# Data 
categories = ['A', 'B', 'C', 'D'] 
values = [25, 30, 15, 20] 
# Create pie chart 
plt.pie(values, labels=categories, autopct='%1.1f%%') 
# Add title 
plt.title('Pie Chart') 
# Display the plot 
plt.show()