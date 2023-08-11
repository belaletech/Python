import random

array_size = 10  # Specify the desired size of the array
lower_limit = 10  # Specify the lower limit of the value range
upper_limit = 60  # Specify the upper limit of the value range

my_array = []  # Initialize an empty array

for _ in range(array_size):
    random_value = random.randint(lower_limit, upper_limit)
    my_array.append(random_value)

# Print the array
print(my_array)
