# Linear Search Example
# Get list input from user
user_input = input("Enter numbers separated by space: ")
num_list = [int(x) for x in user_input.split()]

# Get the target number to search
target = int(input("Enter the target number to search: "))

# Perform linear search
found = False

for i in range(len(num_list)):
    if num_list[i] == target:
        print(f"Target {target} found at index {i}.")
        found = True
        break

if not found:
    print(f"Target {target} not found in the list.")
