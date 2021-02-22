import numpy as np
import time


def test_run():
    # list to 1D Array
    print(np.array([2, 3, 4]))
    # list of tuples to 2D Array
    print(np.array([(2, 3, 4), (5, 6, 7)]))

    # empty array
    print(np.empty(5))
    # 2d array
    print(np.empty((5, 4)))

    print("\n\n\n3D Array: \n\n")
    # 3d Array
    print(np.empty((5, 4, 3)))

    # Arrays on ones
    print(np.ones((5, 4)))

    # type of float
    print(np.ones((5, 4), dtype=float))

    # generate an array full of random numbers, uniformly sampled from [0.0, 1.0)
    print(np.random.random((5, 4)))  # pass in a size tuple

    print("\n\nNormal Distribution :\n")
    # sample numbers from a Gaussian(normal) distribution
    print(np.random.normal(size=(2, 3)))  # " standard normal " (mean=0 , s.d=1)

    print(np.random.normal(50, 10, size=(2, 3)))  # change mean to 50 and s.d to 10

    # Random integers
    print(np.random.randint(10))  # a single integer [0, 10)
    print(np.random.randint(0, 10))  # same as above, specifying [low,high) explicit
    print(np.random.randint(0, 10, size=5))  # 5 random integers as a 1D  array
    print(np.random.randint(0, 10, size=(2, 3)))  # 2*3 array of random integers
    a = np.random.random((5, 4))  # 5*4 array of random numbers
    print(a)
    print(a.shape)
    print(a.shape[0])  # number of rows
    print(a.shape[1])  # number of columns

    print(len(a.shape))  # return dimention of the array as tuple

    print(a.size)  # present the number of elements present in the array A
    print(a.dtype)  # data type of each element in the array

    print("\n-------------------\n")
    b = np.random.seed(693)  # seed the number random generator
    print("b=", b)
    s = np.random.randint(0, 10, size=(5, 4))  # 5*4 random integers in [0,10)
    print("Array:\n", s)
    print("sum: ", s.sum())  # sum over all elements

    # Iterate over rows,to compute sum of each column
    print("Sum of Each Column:\n", s.sum(axis=0))

    # iterate over columns to compute sum of each row
    print("Sum of each row:\n", s.sum(axis=1))

    # statistics: min, max, maen (across rows, cols, and overall)

    print("Minimum of each column:\n", s.min(axis=0))
    print("Maximum of each row:\n", s.max(axis=1))
    print("Mean of all elements: ", s.mean())

    # accessing element at position(3,2)

    element = a[3, 2]
    print(element)

    # element in defined range
    print(a[0, 1:3])

    # top-left corner
    print(a[0:2, 0:2])

    # Slicing
    # Note:Slice n:m:t specifies a range that starts at n,and stops before m,
    print("Slicing: ")
    print(a[:, 0:3:2])  # will start columns 0,2 for every row

    # modifying array

    a[0, 0] = 1

    print("\n Modified(replace one element):\n", a)

    a[0, :] = 2

    print("\n Modified(replace one element):\n", a)

    # Assigning  a list to a Column in an array
    a[:, 3] = [1, 2, 3, 4, 5]
    print("\n Modified(replace one element):\n", a)

    print("\n\n\n\n")
    k = np.random.rand(5)
    # accessing using list of indices
    indices = np.array([1, 1, 2, 3])
    print(k[indices])

    # BOOLEAN Or mask index arrays
    r = np.array([(20, 25, 10, 23, 26, 32, 10, 5, 0), (0, 2, 50, 20, 0, 1, 28, 5, 0)])
    print("r=\n", r)
    # Calculating mean
    mean = r.mean()
    print(mean)

    # masking
    print(r[r < mean])

    r[r < mean] = mean
    print("new r:\n", r)

    # Arithmetic operations
    print("\n Multiply r  by 2:\n", 2 * r)

    print("\n Devide r  by 2:\n", r / 2.5)

    s = r / 3

    # should have matching dimentions
    print("sum of two array: ", r + s)

    # Matrix Multiplication (each elements)

    print("\nMutliplication\n ", r * s)

    # Matrix Devision
    print("\nDivide: ", r/s)


def test_run2():
    a = np.array([9, 6, 2, 3, 12, 14, 7, 10], dtype=np.int32)  # 32 bit integer array
    print("Array: ", a)
    # find the maximum and it's index in array
    print("Maximum Value: ", a.max())
    print("Index of max.: ", get_max_index(a))


def get_max_index(a):
    """Return the index of the maximum value in given 1D array"""
    return a.argmax()


if __name__ == "__main__":
    test_run()
# test_run2()
