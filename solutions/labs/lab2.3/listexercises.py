# Create two different lists, with values of both strings and integers

list1 = list('abc')
list2 = ['x', 'y', 2]
print(list1)
print(list2)

# Add your first name to the first list
list1.append('Brad')
print("Appended first name:", list1)

# Insert your last name in the middle of the second list
list2.insert(2, 'Lohmeyer')
print("Inserted Last name:", list2)

# Extend your middle name into the first list

list1.extend('David')
print("Extended first name:", list1)

# Remove and return the first letter of your middle name from the first list

returned = list1.pop(-5)
print(returned)
print(list1)

# Delete the last letter of your first name from the first list

list1[-5] = list1[-5][:-1]
print("removed last letter of first name", list1)

# Create a new list containing the two lists you have made

new_list = list1.append(list2)
list1.index()

# Print the new list

print(new_list)