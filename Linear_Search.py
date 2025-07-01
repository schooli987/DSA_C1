# Get list input from user
user_input = input("Enter numbers separated by space: ")

# Convert input into list of integers
num_list = []
for x in user_input.split():
    num_list.append(int(x))

# Get the target number to search
target = int(input("Enter the target number to search: "))

# Check if target is in the list
found = False
for num in num_list:
    if num == target:
        found = True
        break

# Display result
if found:
    print(f"Target {target} found in the list.")
else:
    print(f"Target {target} not found in the list.")
