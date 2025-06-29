# Step 1: Get list input from user
user_input = input("Enter numbers separated by space: ")
num_list = [int(x) for x in user_input.split()]

# Step 2: Get the target number to search
target = int(input("Enter the target number to search: "))

# Step 3: Perform linear search to return index position
found = False

for index in range(len(num_list)):
    if num_list[index] == target:
        print(f"Target {target} found at index position {index}.")
        found = True
        break

if not found:
    print(f"Target {target} not found in the list.")
