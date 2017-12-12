class Person(object):
    def __init__(self, name = 'Jane Doe', age = 30, gender = 'female'):
        self.name = name
        self.age = age
        self.gender = gender
        
    def introduce(self):
        print("Hi, I'm " + format(self.name) + ", a " + format(self.age) + " year old " + format(self.gender) + ".")
        
    def get_goal(self):
        print("My goal is: Live for the moment!")


class Student(Person):
    def __init__(self, name = 'Jane Doe', age = 30, gender = 'female', previous_organization = "The School of Life", skipped_days = 0):
        super().__init__(name, age, gender)
        self.previous_organization = previous_organization
        self.skipped_days = skipped_days
        
    def get_goal(self): 
        print("My goal is: Be a junior software developer.")
    
    def introduce(self): 
        print("Hi, I'm " + format(self.name) + ", a " + format(self.age) + " year old " + format(self.gender) + " from " + format(self.previous_organization) + " who skipped " + format(self.skipped_days) + " days from the course already.")
    
    def skip_days(self, number_of_days):
        self.skipped_days += number_of_days
        return self.skipped_days


class Mentor(Person):
    def __init__(self, name = 'Jane Doe', age = 30, gender = 'female', level = 'intermediate'):
        super().__init__(name, age, gender)
        self.level = level
    
    def get_goal(self): 
        print("My goal is: Educate brilliant junior software developers.")
    
    def introduce(self):
        print("Hi, I'm " + format(self.name) + ", a " + format(self.age) + " year old " + format(self.gender) + " " + format(self.level) + " mentor.")
    

class Sponsor(Person):
    def __init__(self, name = 'Jane Doe', age = 30, gender = 'female', company = 'Google', hired_students = 0):
        super().__init__(name, age, gender)
        self.company = company
        self.hired_students = hired_students
        
    def introduce(self):
        print("Hi, I'm " + format(self.name) + ", a " + format(self.age) + " year old " + format(self.gender) + " who represents " + format(self.company) + " and hired " + format(self.hired_students) + " students so far.")
    
    def hire(self):
        self.hired_students += 1
        return self.hired_students
    
    def get_goal(self):
        print("My goal is: Hire brilliant junior software developers.")
    
    
class PallidaClass(object):
    def __init__(self, class_name, students = [], mentors = []):
        self.class_name = class_name
        self.students = students
        self.mentors = mentors
        
    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
        
    def add_mentor(self, mentor):
        if mentor not in self.mentors:
            self.mentors.append(mentor)
            
    def info(self):
        print("Pallida " + format(self.class_name) + " class has " + str(len(self.students)) + " students and "  + str(len(self.mentors)) + " mentors.")


people = []

mark = Person('Mark', 46, 'male')
people.append(mark)
jane = Person()
people.append(jane)
john = Student('John Doe', 20, 'male', 'BME')
people.append(john)
student = Student()
people.append(student)
gandhi = Mentor('Gandhi', 148, 'male', 'senior')
people.append(gandhi)
mentor = Mentor()
people.append(mentor)
sponsor = Sponsor()
people.append(sponsor)      #this line was missing
elon = Sponsor('Elon Musk', 46, 'male', 'SpaceX')
people.append(elon)
student.skip_days(3)

for i in range(3):
    elon.hire()     #originally elon hired 5 people and sponsor 3

for i in range(5):
    sponsor.hire()

for member in people:
    member.introduce()
    member.get_goal()

badass = PallidaClass('BADA55')     #change from LagopusClass to PallidaClass
badass.add_student(student);
badass.add_student(john);
badass.add_mentor(mentor);
badass.add_mentor(gandhi);
badass.info();