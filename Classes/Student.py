class Student:
    counter = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.counter += 1
        self._roll_number = 'A2025/{}/{:003d}'.format(self.name[:3].upper(), Student.counter)
        self.__file_no = 'FILE2025/{}/{:003d}'.format(self.name.upper(), Student.counter)

    def print_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll Number:", self._roll_number)
        print("File Number:", self.__file_no)

st1 = Student("Alice", 20)
st1.print_details()
st2 = Student("Bob", 22)
st2.print_details()
st3 = Student("Charlie", 23)
st3.print_details()

class Science(Student):
    def display_science(self):
        print(f"{self.name} is studying Science.")
        print(f"{self.name}'s age is {self.age}.")
        print("Accessing protected roll number:", self._roll_number)
        # print("Accessing private file number:", self.__file_no)  # This will raise an AttributeError  

sci_student = Science("David", 21)
sci_student.display_science()

