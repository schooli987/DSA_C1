# Step 1: Get list input from user
user_input = input("Enter numbers separated by space: ")
num_list = [int(x) for x in user_input.split()]

# Step 2: Get the target number to search
target = int(input("Enter the target number to search: "))

# Step 3: Perform linear search to find all occurrences
positions = []

for i in range(len(num_list)):
    if num_list[i] == target:
        positions.append(i)

# Step 4: Display result
if positions:
    print(f"Target {target} found at positions (indexes): {positions}")
else:
    print(f"Target {target} not found in the list.")
