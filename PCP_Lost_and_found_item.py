# Step 1: Get drawer items from user
drawer_input = input("Enter items in the drawer separated by commas: ")
drawer_items = [item.strip().lower() for item in drawer_input.split(",")]

# Step 2: Get the lost item to search
lost_item = input("Enter the item you lost: ").strip().lower()

# Step 3: Perform linear search
found = False

for item in drawer_items:
    if item == lost_item:
        found = True
        break

# Step 4: Print result
if found:
    print(f"{lost_item.capitalize()} found in the drawer!")
else:
    print(f"{lost_item.capitalize()} not found.")
