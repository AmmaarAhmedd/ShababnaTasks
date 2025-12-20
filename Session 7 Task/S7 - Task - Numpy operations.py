import numpy as np

A = np.array([10, 20, 30, 40, 50])
B = np.array([5, 4, 3, 2, 1])

print ('1. Operations: ')
print("A + B =", A + B)
print("A - B =", A - B)
print("A * B =", A * B)
print("A / B =", A / B)

print ('2. Functions: ')
print("Mean of A =", np.mean(A))
print("Max of A =", np.max(A))
print("Min of A =", np.min(A))

print("3. Dot product of A and B = ", np.dot(A, B))

print ('4. Reshaping: ')
A_reshaped = A.reshape(5, 1)
print("Reshaped A:\n", A_reshaped)
