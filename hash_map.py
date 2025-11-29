# ------------------------------------------
# Sorting Elements Using a Hash Table (Dict)
# ------------------------------------------

# Example input list (can be changed)
numbers = [4, 2, 2, 9, 1, 4, 5, 9]

# Step 1: Create an empty hash table (dictionary in Python)
hash_table = {}

# Step 2: Store each element in the hash table
# If seen before, increase count; otherwise, set count to 1
for num in numbers:
    if num in hash_table:
        hash_table[num] += 1  # update existing count
    else:
        hash_table[num] = 1   # add new key with value 1

# Step 3: Sort the keys from the hash table
sorted_keys = sorted(hash_table.keys())

# Step 4: Create the final sorted list based on frequency
sorted_list = []
for key in sorted_keys:
    # repeat each number based on how many times it appeared
    sorted_list.extend([key] * hash_table[key])

# Print results
print("Original List:", numbers)
print("Hash Table (Value = Frequency):", hash_table)
print("Sorted List:", sorted_list)