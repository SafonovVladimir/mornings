import numpy as np

my_array = np.arange(5)
my_array = my_array[[False, True, True, False, True]]

print(my_array[my_array <= True])
