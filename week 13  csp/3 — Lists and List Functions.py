# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.

# Examples:

my_list = ['apple', 'banana', 'cherry']
print(my_list[0])         # apple
print(my_list[1:])        # ['banana', 'cherry']

my_list.append('grape')
print(my_list)

my_list.pop(1)
print(my_list)

numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)
my_list = [1,2,3,4,5]
print(my_list)
print(type(my_list))

print(my_list[0])
print(my_list[1:4])
print(my_list[0:])
print(my_list[-1])

my_list.append(6)
print(my_list)

my_list.append(7)
my_list.append(8)
print(my_list)

my_list.extend([10,11,12,13,14])
print(my_list)

my_list.extend(list(range(15,500)))
print(my_list)

my_list.extend(list(range(500,1000)))
print(my_list)

new_lits = ['a','b','c']
print(new_lits)
new_lits.append('d')
print(new_lits)
remove_item = new_lits.pop()
print(remove_item)
print(new_lits)
remove_second_item = new_lits.pop(1)
print(new_lits)

numbers = [4,2,5,1,3]
numbers.sort()

numbers.reverse()
print(numbers)

numbers.insert(2, 10)
print(numbers)

third_list = [7,8,9]
third_list[0] = 6
print(third_list)
third_list[-1] = 10
print(third_list)

import random
random_list = random.sample(range(1, 1000), 100)
print(random_list)
print(sorted(random_list))

sorted_list = sorted(random_list)
print(sorted_list)



#summary of lits of functions
#.appendi(item) - adds an item to the end of the list
# .pop(index) - removes aand returns the item at the specified index
# .sort() - sort the list in acending order
# .reverse() - reverses the order of the list 
# Practice Problems:

# Create a list with 5 of your favorite foods.

# Print the second and last item.

# Add a new item using .append().

# Remove the first item using .pop(0).

# Reverse your list using .reverse().

# Create a list of 3 lists (matrix), and access the middle element.