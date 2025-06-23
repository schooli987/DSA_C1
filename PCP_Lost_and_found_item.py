drawer_items = ["book", "charger", "pen", "notebook", "eraser"]
lost_item = "pen"
found = False

for item in drawer_items:
    if item == lost_item:
        found = True
        break

if found:
    print(f"{lost_item.capitalize()} found in the drawer!")
else:
    print(f"{lost_item.capitalize()} not found.")
