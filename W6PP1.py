
    def _init_(self):
        self.id = ""
        self.name = ""
        self.department = ""
    def create_new_student(self):
        self.id = input("Enter Student id: ")
        self.name = input("Enter Student name: ")
        self.department = input("Enter Student department: ")
    def print_info(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Department:", self.department)

Student = Student()
Student.create_new_student()
Student.print_info()



    def _init_(self):
        self.id = ""
        self.name = ""
        self.department = ""
        self.course = ""
        self.role = ""
    def create_new_faculty(self):
        self.id = input("Enter Faculty id: ")
        self.name = input("Enter Faculty name: ")
        self.department = input("Enter Faculty department: ")
        self.course = print("Enter Faculty course: ")
        self.role = input("Enter Faculty role: ")

