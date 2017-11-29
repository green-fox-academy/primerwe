students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

# create a function that takes a list of students and prints:
# - Who has got more candies than 4 candies

# create a function that takes a list of students and prints: 
#  - how many candies they have on average

def list_of_students(students):
    listOf = ""
    for i in range(len(students)):
        if students[i]['candies'] > 4: 
            listOf += students[i]['name']
    print(listOf)

print(list_of_students(students))

def average_candy(students):
    averageCandy = 0
    for i in range(len(students)):
        averageCandy += students[i]['candies']
    print(averageCandy / (len(students)))

print(average_candy(students))
