class Student:
    class_year = 2025
    num_student = 0

    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject
        Student.num_student += 1

    def show(self):
        print (f'Hey {self.name} is passed on {Student.class_year}')


student_1 = Student ('Mukesh', 25, 'Python')
student_2 = Student ('David', 30, 'Aws')

student_1.show ()
student_2.show ()
print(Student.num_student)
