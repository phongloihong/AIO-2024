from abc import ABC, abstractmethod
import math


class Person(ABC):
    def __init__(self, name: str, yob: int):
        self._name = name
        self._yob = yob

    @abstractmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name: str, yob: int, grade: str):
        super().__init__(name, yob)
        self._grade = grade

    def describe(self):
        print(
            f'Student - Name: {self._name} - YoB: {self._yob} - Grade: {self._grade}')


class Teacher(Person):
    def __init__(self, name: str, yob: int, subject: str):
        super().__init__(name, yob)
        self._subject = subject

    def describe(self):
        print(
            f'Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self._subject}')


class Doctor(Person):
    def __init__(self, name: str, yob: int, specialist: str):
        super().__init__(name, yob)
        self._specialist = specialist

    def describe(self):
        print(
            f'Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self._specialist}')


class Ward:
    def __init__(self, name: str):
        self._name = name
        self._persons = []

    def add_person(self, person: Person):
        self._persons.append(person)

    def describe(self):
        print(f'Ward: {self._name}')
        for person in self._persons:
            person.describe()

    def count_doctor(self):
        count = 0
        for person in self._persons:
            if isinstance(person, Doctor):
                count += 1
        return count

    def sort_age(self):
        self._persons.sort(key=lambda x: x._yob, reverse=True)
        return self._persons

    def compute_average(self):
        teachers = [
            person for person in self._persons if isinstance(person, Teacher)]

        total = sum(person._yob for person in teachers)
        return total / len(teachers)


student1 = Student(name="studentA", yob=2010, grade="7")
student1.describe()

teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
teacher1.describe()

doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
doctor1.describe()


teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")

ward1 = Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.describe()

print(f"\nNumber of doctors : { ward1.count_doctor ()}")
assert ward1.count_doctor() == 2

print("\nAfter sorting Age of Ward1 people ")
ward1.sort_age()
ward1.describe()

print(f"\nAverage year of birth ( teachers ): { ward1.compute_average ()}")
assert math.isclose(ward1.compute_average(), 1982.0, rel_tol=1e-9)
