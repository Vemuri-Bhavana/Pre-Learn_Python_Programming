#solving linear equations using scipy
#Equations : x+y=30 & 4x+9y=150

from scipy import linalg
import numpy as np

a = np.array([[1,1], [4,9]])
b = np.array([30,150])
x = linalg.solve(a, b)
print("x = ",x[0],"y = ",x[1])
