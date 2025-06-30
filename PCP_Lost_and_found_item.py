# Get drawer items input from user
drawer_input = input("Enter items in the drawer separated by commas: ")

# Initialize an empty list
drawer_items = []

# Split input by commas and loop through each item
for item in drawer_input.split(","):
    cleaned_item = item.strip().lower()
    drawer_items.append(cleaned_item)

# Print the list
print(drawer_items)

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
