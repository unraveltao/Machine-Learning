#####################################################
# Import math library
import math
# Print the value of pi
print ('pi = ', math.pi)
# Print the value of e
print ('e = ', math.e)
# Print the value of square root of 2
print ('sqrt(2) = ', math.sqrt(2))
#####################################################
from mpmath import mp
mp.dps = 1000 + 1
print('print 1000 digits of pi behind decimal point')
print(mp.pi)
print('print 1000 digits of e behind decimal point')
print(mp.e)
print('print 1000 digits of sqrt(2) behind decimal point')
print(mp.sqrt(2))
######################################################
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.
num = float(input("Enter a number: "))
if num.is_integer():
    if (num % 2) == 0:
       print("{0} is even ".format(int(num)))
    else:
       print("{0} is odd ".format(int(num)))
else:
    print("{0} is not an integer ".format(num))
########################################################
num1 = 2
num2 = 3
# add two numbers
sum = num1 + num2
# display the computation
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
#############################################################
# user input numbers
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

# add two numbers
sum = float(num1) + float(num2)

# display the computation
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
######################################################
import numpy as np

a_i = np.linspace(1,10,10)
print(a_i)

a_i_cumsum = np.cumsum(a_i)
print(a_i_cumsum)
#################################################
num1 = 5
num2 = 3

# add two numbers
diff = num1 - num2

# display the computation
print('The difference of {0} and {1} is {2}'.format(num1, num2, diff))
#################################################
import numpy as np

# row vector transposed to a column vector
a_row = np.array([[1, 2, 3]])
print(a_row)

b = a_row.T
print(b)

b_col = np.array([[1],[2],[3]])
print(b_col)

a = b_col.T
print(a)
###################################
import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6]])

A_first_col = A[:,0] # saved as one dimension row
print(A_first_col)

A_first_col_V2 = A[:,[0]] # saved as a column
print(A_first_col_V2)

A_first_second_col_V2 = A[:,[0,1]] # extract first and second columns
print(A_first_second_col_V2)

A_first_third_col_V2 = A[:,[0,2]] # extract first and third columns
print(A_first_third_col_V2)

A_first_row = A[[0],:] # extract first row
print(A_first_row)

A_second_row = A[[1],:] # extract second row
print(A_second_row)

A_second_row_first_col = A[[1],[0]] # i = 2, j = 1
print(A_second_row_first_col)
###############################################

