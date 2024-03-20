class Student:
    def __init__(salf) -> None:
        self.degree="UG"
    def __str__(self) -> str:
        return salf.degree+ "student"
    
class PGStudent(Student):
    def __init__(salf) -> None:
        super().__init__()
        self.degree="PG"

u=Student()
print(u.degree)

p=PGStudent()
print(p.degree)