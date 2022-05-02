# Exercise One
# Create a list named students containing some student names (strings).
# Print out the second student's name.
# Print out the last student's name.

student_list = "Sarah", "Claire", "Guy", "Sue", "Jose", "Nel", "Todd"
print(student_list[1])
print(student_list[-1])


# Excercise Two
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Use a for loop to print out the string "food goes here is a good food".

tup = ("banana", "pinapple", "mango", "kiwi",
       "strawberry", "lemon", "orange")

for food in tup:
    print(food+" goes here is a good "+food)

# Excercise 3
# Using a for loop, print just the last two food strings from foods.
for food in range(5, 7):
    print(tup[food])
