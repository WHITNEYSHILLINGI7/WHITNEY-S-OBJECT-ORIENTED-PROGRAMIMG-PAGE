class Student:
    def __init__(self, reg_number, name):
        self.reg_number = reg_number
        self.name = name

    def display_info(self):
        return(f" Registration Number:{self.reg_number} Name:{self.name}")

Student1 = Student("M23B13/020", "MUGISHA TEVIN")
Student2 = Student("M23B13/015", "AGABA MARION")
Student3 = Student("M23B13/007", "NIMUSIIMA IRENE")

print(Student1.display_info())   
print(Student2.display_info()) 
print(Student3.display_info())      