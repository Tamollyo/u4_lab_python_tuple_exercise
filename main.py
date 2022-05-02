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
for food in range(-2, 0):
    print(tup[food])
    # print(tup[-2])
    # print(tup[-1])


# Excercise 4
# Create a dictionary named home_town containing the keys of city, state and population.
# Print a string with this format:
#"I was born in city, state - population of population"
home_town = {
    "city": "Denver",
    "state": "Colorado",
    "population": 200
}

print("I was born in " + home_town["city"]+", " +
      home_town["state"]+", with a population of " + str(home_town["population"]))

# Excercise 5
# Iterate over the key: value pairs in home_town and print a string for each item, for example:
#"city = Arcadia"
#"state = California"
#"population = 58000"

for key, value in home_town.items():
    print(key, "=", value)

# for key in home_town:
#     print('{} = {}'.format(key, home_town[key]))

# Exercise 6
# Create an empty list named cohort.
# Using a for loop, add one dictionary to the cohort list for each student name. Each dictionary should have this shape:
# {
#   'student': 'Tina',
#   'fav_food' 'Cheeseburger'
# }
# Iterate over cohort printing out each element.

cohort = []
for i in range(len(student_list)):
    cohort.append({
        'student': student_list[i],
        'fav_food': tup[i]
    })

for student in cohort:
    print(student)

# Exercise 7
# Using the list of students and list comprehension, assign to a variable named awesome_students a new list containing strings similar to this:
#["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
# Iterate over awesome_students printing out each string.

awesome_students = ['{} is awesome!'.format(
    student) for student in student_list]
for string in awesome_students:
    print(string)

# Exercise 8
# Using the tuple foods and list comprehension within a for loop, print each food string that contains the letter a.
letter_a = [food for food in tup if "a" in food]
print(letter_a)
