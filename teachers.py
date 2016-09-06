# Create a function named most_classes that takes a dictionary of teachers
# Each key is a teacher's name and their value is a list of classes they've
# taught. most_classes should return the teacher with the most classes.
#
# The dictionary will be something like:
# {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms',
#                   'Technology Foundations'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Often, it's a good idea to hold onto a max_count variable.
# Update it when you find a teacher with more classes than
# the current count. Better hold onto the teacher name somewhere
# too!
#
# Your code goes below here.

my_dict = {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms',
                            'Technology Foundations'],
           'Kenneth Love': ['Python Basics', 'Python Collections'],
           'Dylan Cascio':
           ['Pythong 1', 'Chrome Dev Tools',
            'Getting Started with Squarespace', 'Another Class of Sorts']}


def most_classes(dict1):
    max_count = 0
    name = ''
    for entry in dict1.values():
        if len(entry) > max_count:
            max_count = len(entry)
            value = entry
            for key, values in dict1.items():
                if values == value:
                    name = key
    return name


print(most_classes(my_dict))

print("-----------")

# Next, create a function named num_teachers that takes the same dictionary
# of teachers and classes. Return the total number of teachers.


def num_teachers(dict1):
    teachers = 0
    for teacher in dict1.keys():
        teachers += 1
    return teachers


print(num_teachers(my_dict))

print("-----------")

# Now, create a function named stats that takes the teacher dictionary.
# Return a list of lists in the format [<teacher name>, <number of classes>].
# For example, one item in the list would be ['Dave McFarland', 1].


def stats(dict1):
    teachers = []
    for key, value in dict1.items():
        value = len(value)
        teachers.append([key, value])
    return teachers


print(stats(my_dict))
print("-----------")

# Great work! Finally, write a function named courses that takes the teachers
# dictionary. It should return a single list of all of the courses offered by
# all of the teachers.


def courses(dict1):
    course_list = []
    for course in dict1.values():
        course_list += course
    return course_list


print(courses(my_dict))

print("-----------")
print(70 + 2.5)
