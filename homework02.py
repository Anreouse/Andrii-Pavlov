class MaxStudentsExceededError(Exception):
    """Виняток, що виникає при перевищенні максимальної кількості студентів у групі."""
    pass


class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Gender: {self.gender}, Age: {self.age}"


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Record Book: {self.record_book}"


class Group:
    MAX_STUDENTS = 10

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= self.MAX_STUDENTS:
            raise MaxStudentsExceededError(f"Cannot add more than {self.MAX_STUDENTS} students to the group.")
        self.group.add(student)

    def delete_student(self, last_name):
        student_to_remove = self.find_student(last_name)
        if student_to_remove:
            self.group.remove(student_to_remove)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number: {self.number}\n{all_students if all_students else "No students in this group."}'

gr = Group('PD1')

for i in range(10):
    st = Student('Male' if i % 2 == 0 else 'Female', 20 + i, f'FirstName{i}', f'LastName{i}', f'AN1{i}')
    gr.add_student(st)

print(gr)

try:
    st11 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    gr.add_student(st11)
except MaxStudentsExceededError as e:
    print(e)