class Student(object):
    def learn(self):
        return "Hello world!"
        
    def question(self, teacher):
        return teacher.answer()

class Teacher(object):
    def teach(self, student):
        return student.learn()
        
    def answer(self):
        return "Answer"

student = Student()
teacher = Teacher()

print(teacher.teach(student))