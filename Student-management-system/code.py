# --------------
# Code starts here

# Create the lists 
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']
# Concatenate both the strings
new_class = class_1 + class_2
print(new_class)
# Append the list
new_class.append('Peter Warden')
# Print updated list
print(new_class)

# Remove the element from the list
new_class.remove('Carla Gentry')
# Print the list
print(new_class)


# Create the Dictionary
courses = {'Math' : 65,'English' : 70,'History': 80,'French': 70,'Science': 60}
print(courses)

# Slice the dict and stores  the all subjects marks in variable
math = courses.get('Math')
english = courses.get('English')
history = courses.get('History')
french = courses.get('French')
science = courses.get('Science')
# Store the all the subject in one variable `Total`
total = math + english + history + french + science
# Print the total
print(total)
# Insert percentage formula
percentage = ((total/500)*100)
# Print the percentage
print(percentage)
# Create the Dictionary
mathematics = {'Geoffrey Hinton' : 78,'Andrew Ng' : 95,'Sebastian Raschka' : 65,'Yoshua Benjio' : 50,'Hilary Mason':70,'Corinna Cortes' : 66,'Peter Warden' : 75}
topper = max(mathematics,key = mathematics.get)
print(topper)

# Given string
topper = 'Andrew Ng'
name_split = topper.split()
print(name_split)
# Create variable first_name 
first_name = name_split[0]
Last_name = name_split[1]
# Create variable Last_name and store last two element in the list

# Concatenate the string

# print the full_name
full_name = Last_name + " " + first_name
print(full_name)
# print the name in upper case
certificate_name = full_name.upper()
print(certificate_name)
# Code ends here




