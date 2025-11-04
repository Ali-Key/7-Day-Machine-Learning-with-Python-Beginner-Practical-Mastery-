# ============================================================
# 🧾 DAY 3 — pandas for Data Handling
# ============================================================

# 🎯 Goal:
# Learn how to load, clean, and explore real datasets using pandas.

# ------------------------------------------------------------
# 🧠 What is pandas?
# pandas is a powerful Python library used for data manipulation and analysis.
# It provides data structures like Series and DataFrame that make it easy
# to work with structured (tabular) data efficiently.
# ------------------------------------------------------------

# Install pandas if needed:
# pip install pandas

# Step 1 — Import pandas
import pandas as pd
print("\n✅ pandas imported successfully!")

# ------------------------------------------------------------
# Step 2 — Creating pandas Series
# ------------------------------------------------------------

# 2.1 Creating a Series from a list
data_list = [10, 20, 30, 40, 50]
series_from_list = pd.Series(data_list)
print("\n--- Creating pandas Series from a list ---")
print(series_from_list)

# 2.2 Creating a Series from a dictionary
data_dict = {'a': 10, 'b': 20, 'c': 30}
series_from_dict = pd.Series(data_dict)
print("\n--- Creating pandas Series from a dictionary ---")
print(series_from_dict)

# ------------------------------------------------------------
# Step 3 — Creating pandas DataFrame
# ------------------------------------------------------------

# 3.1 From a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df_from_dict = pd.DataFrame(data)
print("\n--- DataFrame created from dictionary ---")
print(df_from_dict)

# 3.2 From a list of lists
data_list_of_lists = [
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]
df_from_list = pd.DataFrame(data_list_of_lists, columns=['Name', 'Age', 'City'])
print("\n--- DataFrame created from list of lists ---")
print(df_from_list)

# ------------------------------------------------------------
# Step 4 — Basic Operations with pandas DataFrame
# ------------------------------------------------------------

print("\n--- Basic Operations with DataFrame ---")

# 4.1 Adding a new column
df_from_dict['Salary'] = [70000, 80000, 90000]
print("\nAfter adding 'Salary' column:\n", df_from_dict)

# 4.2 Filtering rows based on a condition
filtered_df = df_from_dict[df_from_dict['Age'] > 28]
print("\nFiltered rows where Age > 28:\n", filtered_df)

# 4.3 Basic statistics
print("\n--- Summary Statistics ---")
print(df_from_dict.describe())

# ------------------------------------------------------------
# Step 5 — Indexing & Slicing DataFrame
# ------------------------------------------------------------

print("\n--- Indexing & Slicing DataFrame ---")

# Access a specific column
print("\n'Name' column:\n", df_from_dict['Name'])

# Access a specific row by index
print("\nFirst row:\n", df_from_dict.iloc[0])

# Slice first two rows
print("\nFirst two rows:\n", df_from_dict.iloc[0:2])

# Slice specific columns
print("\nOnly 'Name' and 'City' columns:\n", df_from_dict[['Name', 'City']])

# Access a specific element (row 2, column 'City')
print("\nElement at row 2, 'City' column:\n", df_from_dict.at[1, 'City'])


# ------------------------------------------------------------
# SUMMARY OF DAY 3 — pandas for Data Handling - Part 1
# ------------------------------------------------------------
print("\n✅ End of Day 3 Part 1: pandas for Data Handling Complete!")
print("You learned how to create Series and DataFrames, perform basic operations, and index & slice DataFrames.")
print("Stay tuned for Day 3 Part 2 where we will explore more advanced pandas functionalities!")

