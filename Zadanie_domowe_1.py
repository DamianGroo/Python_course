
from numpy import *
import numpy as np;

list = arange(0, 19)

print("Array before transformation:")
print(list)
print("")
print("Array after transformation:")
print(list[list % 4 == 0])



