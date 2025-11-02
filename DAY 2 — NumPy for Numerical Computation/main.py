# -------------------------------
# 🧠 DAY 2 — NumPy for Numerical Computation
# -------------------------------


# -------------------------------
# ✅ START OF DAY 2: NUMPY FOR NUMERICAL COMPUTATION
# -------------------------------

print("Welcome to Day 2: NumPy for Numerical Computation")

# NumPy is a Python library used for working with arrays. It also has functions for working in the domain of linear algebra, fourier transform, and matrices.
# In this tutorial, we will cover the basics of NumPy and how to use it for numerical computations.

# Install NumPy if needed
# pip install numpy

# Import libraries
import numpy as np

print("\n✅ NumPy and Matplotlib imported successfully!")



# Step 1 — Creating NumPy Arrays
# NumPy arrays are similar to Python lists, but they are more efficient for numerical computations.

# 1.1 Creating NumPy Arrays - to create arrays with specific values.

arr1 = np.array(([10, 20, 30, 40])) # Create a iD array 
print("\n--- Creating NumPy Arrays ---")
print("\nNumPy Array:", arr1)

# 2.2 Using np.arange() - to create an array with a range of values.
array_range = np.arange(0, 10)  # Create an array from 0 to 10 with a step of 2
print("\n--- NumPy Array with arange() ---")
print("\nNumPy Array with arange()", array_range)

# 2.3 Using np.zeros() and np.ones() - to create arrays filled with zeros or ones.
zeros_array = np.zeros((3, 4))  # Create a 3x4 array filled with zeros
ones_array = np.ones((2, 5))    # Create a 2x5 array filled with ones

print("\n--- Arrays Filled with Zeros and Ones ---")
print("\nZeros Array:\n", zeros_array)
print("\nOnes Array:\n", ones_array)

# 2.4 Two-dimensional (2D) arrays - to create matrices.
matrix_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # Create a 3x3 matrix from a 2D array
print("\n2D Array (Matrix):\n", matrix_2d)


# Step 3 — Basic Operations with NumPy Arrays
# Basic statistics - sum, mean, max, min, standard deviation, variance
data = np.array([10, 20, 30, 40]) 
print("\nThe original array data is:", data)

print("--- Basic Descriptive Statistics (NumPy) ---")
print("Sum:", np.sum(data)) # Sum of all elements in the array
print("Mean:", np.mean(data)) # Mean of all elements in the array
print("Max:", np.max(data))  # Maximum value in the array
print("Min:", np.min(data)) # Minimum value in the array
print("Standard Deviation:", np.std(data)) # Standard deviation of the array elements
print("Variance:", np.var(data)) # Variance of the array elements

# Arithmetic operations (vectorized) - addition, subtraction, multiplication, division
print("\n--- Arithmetic Operations (NumPy) ---")

data1 = np.array([1, 2, 3])
data2 = np.array([4, 5, 6])

print("\nThe original arrays are:", data1, "and", data2) 
print("The addition of the arrays:", data1 + data2)
print("The subtraction of the arrays:", data1 - data2)
print("The multiplication of the arrays:", data1 * data2)
print("The division of the arrays:", data2 / data1)

# Step 4 — Indexing & Slicing Arrays - to access individual elements, rows, columns, or sub-arrays.
print("\n--- Indexing and Slicing Arrays (NumPy) ---")

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nOriginal Array:\n", data)

print("\nFirst row:", data[0]) # Accessing the first row of the 2D array
print("Second row:", data[1]) # Accessing the second row of the 2D array

print("Element at row 2, column 3:", data[1, 2]) # Accessing the element at row 2, column 3
print("First two rows and first two columns:\n", data[0:2, 0:2]) # Slicing the first two rows and first two columns


# Step 5 — Reshaping Arrays - to change the shape of an array without changing its data.
print("\n--- Reshaping Arrays (NumPy) ---")

data = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("\nOriginal Array:\n", data)

print("\nReshaped Array:\n", data.reshape(4, 2)) # Reshaping the array to 4 rows and 2 columns
print("\nFlattened Array:\n", data.flatten()) # Flattening the array to 1D array

# Step 6 — Generating Random Data - to create arrays with random values.
print("\n--- Generating Random Data (NumPy) ---")

random_array = np.random.rand(1, 4)  # Create a 3x4 array with random values between 0 and 1
print("\nRandom Array:\n", random_array)

# Step 7 — Shape of an Array - to get the dimensions of an array.
print("\n--- Shape of an Array (NumPy) ---")

data = np.array([1, 2, 3]) # Create a 1D array
print("\nThe Original Array:\n", data)
print("\nShape of the Array:", data.shape)  # Get the shape of the array

# Step 8 — Reshape an Array - to change the shape of an array.
print("\n--- Reshape an Array (NumPy) ---")

data = np.array([[1, 2, 3, 4], [5, 6, 7, 8]]) # Create a 2D array
print("\nThe Original Array:\n", data)

reshaped_data = data.reshape(4, 2)  # Reshape the array to 4 rows and 2 columns
print("\nReshaped Array:\n", reshaped_data)

# Step 9 — Splitting an Array - to divide an array into multiple sub-arrays.
print("\n--- Splitting an Array (NumPy) ---")

data = np.array([[1, 2, 3, 4], [5, 6, 7, 8]]) # Create a 2D array
print("\nThe Original Array:\n", data)

split_data = np.array_split(data, 2)  # Split the array into 2 sub-arrays
print("\nSplit Arrays:")

# Step 10 — Searching Arrays - to find elements in an array that meet certain conditions.
print("\n--- Searching Arrays (NumPy) ---")

data = np.array([10, 20, 30, 40, 50]) # Create a 1D array
print("\nThe Original Array:\n", data)

search_result = np.where(data > 25)  # Find indices of elements greater than 25
print("\nIndices of elements greater than 25:", search_result[0])

# step 11 — Sorting Arrays - to sort the elements of an array.
print("\n--- Sorting Arrays (NumPy) ---")

data = np.array([40, 10, 30, 20, 50]) # Create a 1D array
print("\nThe Original Array:\n", data)

sorted_data = np.sort(data)  # Sort the array
print("\nSorted Array:\n", sorted_data)

# Step 12 — Filtering Arrays - to filter elements based on conditions.
print("\n--- Filtering Arrays (NumPy) ---")

data = np.array([10, 25, 30, 45, 50]) # Create a 1D array
print("\nThe Original Array:\n", data)

filtered_data = data[data > 30]  # Filter elements greater than 30
print("\nFiltered Array (elements greater than 30):\n", filtered_data)


# -------------------------------
# ✅ END OF DAY 2: NUMPY FOR NUMERICAL COMPUTATION
# -------------------------------
print("\n✅ End of Day 2: NumPy for Numerical Computation Complete!")
print("You learned how to create NumPy arrays, perform basic operations, indexing & slicing, reshaping, generating random data, and more.")
print("Now it's time to move on to the next day! Keep up the great work!")
