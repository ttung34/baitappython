#Nhap diem cua sinh vien kieu 1
#self để gán vô các giá trị nằm trong init
#bên phải dùng để là giá trị ta truyền vô init
#Khai baos một cái hàm sử dụng đối tượng )    def print_info(self):
class Student:
    def __init__(self,id,name,grades):
        self.id=id
        self.name=name
        self.grades= grades
        self.gpa =0
    
    def print_info(self):
        print(f'student.ID:{self.id}')
        print(f'student name:{self.name}')
        for subject in self.grades:
            print(f'{subject}:{self.grades[subject]}')
        print(f'student gpa:{self.gpa}')
    
    def calculate_gpa(self):
        total =0
        for subject in self.grades:
            total +=self.grades[subject]
        self.gpa = total/len(self.grades)
    
    def add_new_subject(self):
        new_subject = input("Hay nhap so mon hoc moi: ")
        self.grades[new_subject] = float(input(f"Hay nhap so diem cho mon hoc{new_subject}"))

student_1_grades={"python":9,"web":10,"English":10}
student_1= Student(1, "Thanh Tung", student_1_grades)
student_1.print_info()
student_1.add_new_subject()
student_1.calculate_gpa()
student_1.print_info()
#student_2= Student(2,"Linh",student_1_grades)
#student_2.print_info()