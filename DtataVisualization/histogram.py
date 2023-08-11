import matplotlib.pyplot as plt 
import numpy as np 
# Generate data 
data = np.random.randn(100) 
# Create histogram 
plt.hist(data, bins=5) 
# Add labels and title 
plt.xlabel('Values') 
plt.ylabel('Frequency') 
plt.title('Histogram') 
# Display the plot 
plt.show()