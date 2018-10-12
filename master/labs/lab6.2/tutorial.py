# For this lab you will need to have Numpy downloaded and installed.
#
# The best option is to download one of the scientific packages for your operating system.
# These packages provide several modules beyond the standard library.
#
# We recommend the Anaconda distribution, which includes Pandas and NumPy.
# Anaconda is a distribution of Python that includes hundreds of modules beyond the standard library. 
# Check to see which version is appropriate for you – If you have Python 3.4 64bit installed, for instance,
# you should downloaded the latest 64-bit version of Anaconda. 
#
# https://www.continuum.io/downloads
# This is a large file, so downloading may take a little time and installation may take several minutes as well.
#
#
# Lab:
#
# source: http://www.engr.ucsb.edu/~shell/che210d/numpy.pdf
#
# it is common to import under the briefer name np
# This statement will allow us to access NumPy objects using np.X instead of numpy.X.
import numpy as np

# The central feature of NumPy is the array object class. Arrays are similar to lists in Python,
# except that every element of an array must be of the same type, typically a numeric type like
# float or int. Arrays make operations with large amounts of numeric data very fast and are
# generally much more efficient than lists.
#
# An array can be created from a list:

a = np.array([1, 4, 5, 8], float)
print(a)
# array([ 1., 4., 5., 8.])
type(a)
# <type 'numpy.ndarray'>

# Here, the function array takes two arguments: the list to be converted into the array and the
# type of each member of the list. Array elements are accessed, sliced, and manipulated just like
# lists:

print(a[:2])
# array([ 1., 4.])
print(a[3])
# 8.0
a[0] = 5.
print(a)
# array([ 5., 4., 5., 8.])

# Arrays can be multidimensional. Unlike lists, different axes are accessed using commas inside
# bracket notation. Here is an example with a two-dimensional array (e.g., a matrix):

a = np.array([[1, 2, 3], [4, 5, 6]], float)
print(a)
# array([[ 1., 2., 3.],
# [ 4., 5., 6.]])
print(a[0,0])
# 1.0
print(a[0,1])
# 2.0
#
# Array slicing works with multiple dimensions in the same way as usual, applying each slice
# specification as a filter to a specified dimension. Use of a single ":" in a dimension indicates the
# use of everything along that dimension:
a = np.array([[1, 2, 3], [4, 5, 6]], float)
print(a[1,:])
# array([ 4., 5., 6.])
print(a[:,2])
# array([ 3., 6.])
print(a[-1:,-2:])
# array([[ 5., 6.]])
#
#  The shape property of an array returns a tuple with the size of each array dimension:
print(a.shape)
# (2, 3)
#
#  The dtype property tells you what type of values are stored by the array:
print(a.dtype)
#  dtype('float64')
#
#  Here, float64 is a numeric type that NumPy uses to store double-precision (8-byte) real
# numbers, similar to the float type in Python.
#
#  When used with an array, the len function returns the length of the first axis:
a = np.array([[1, 2, 3], [4, 5, 6]], float)
print(len(a))
# 2
#
#  The in statement can be used to test if values are present in an array:
a = np.array([[1, 2, 3], [4, 5, 6]], float)
print(2 in a)
# True
print(0 in a)
# False
#
#  Arrays can be reshaped using tuples that specify new dimensions. In the following example, we
# turn a ten-element one-dimensional array into a two-dimensional one whose first axis has five
# elements and whose second axis has two elements:
a = np.array(range(10), float)
print(a)
# array([ 0., 1., 2., 3., 4., 5., 6., 7., 8., 9.])
a = a.reshape((5, 2))
print(a)
# array([[ 0., 1.],
# [ 2., 3.],
#  [ 4., 5.],
#  [ 6., 7.],
#  [ 8., 9.]])
print(a.shape)
# (5, 2)
#
# Notice that the reshape function creates a new array and does not itself modify the original
# array.
#
#
#
# Continue the rest of the tutorial at: http://www.engr.ucsb.edu/~shell/che210d/numpy.pdf
#
# Hint: The tutorial is written using the Python command line interpreter, which doesn't
# require explicitly typing print() to output a variable. In a Python file, however, you
# will need to use print() as shown in the examples above.