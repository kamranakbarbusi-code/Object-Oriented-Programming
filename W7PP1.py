myStudentsList = []
myFacultyList = []
myCourseList = []

class Student:
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

class Faculty:

    def _init_(self):
        self.id = ""
        self.name = ""
        self.department = ""
        self.course = ""
        self.role = ""


    def create_new_faculty(self):
        self.id = input("Enter Faculty id:")
        self.name = input("Enter Faculty name: ")
        self.department = input("Enter Faculty department: ")
        self.course = print("Enter Faculty course: ")
        self.role = input("Enter Faculty role: ")

class Courses:

    def init_(self):
        self.course_id = ""
        self.course_name = ""
        self.faculty_id = ""
        self.students = []

    def create_courses(self):
        self.course_id = input("Enter Course ID: ")
        self.course_name = input("Enter Course name: ")

    def assign_faculty(self, faculty_id):
        self.faculty_id = faculty_id

    def teaching_faculty(self, faculty_id):
        print("Teaching Course: ", self.faculty_id)

    def enrolled_student(self, student_id):
        print("Enrolled Students:", self.students)


#Get how many faculty you want to create from the user
#iterate that in a for loop

numberFaculty = int(input("How many faculty do you want to create? "))
for i in range(numberFaculty):
    fac = Faculty()
    fac.creat_faculty()
    myFacultyList.append(fac)



#Get how many students you want to create from the user
#iterate that in a for loop

numberStudents = int(input("How many students do you want to create? "))
for i in range(numberStudents):
    stu = Student()
    stu.create_new_student()
    myStudentsList.append(stu)


#Get how many Courses you want to create from the user
#iterate that in a for loop
numberCourses = int(input("How many courses do you want to create? "))
for i in range(numberCourses):
    cou = Course()
    cou.create_new_course()

    faculty_id = input("Enter Faculty ID for this course: ")
    cour.assign_faculty(faculty_id)

    student_id = input("Enter Student ID to register for this course: ")
    cour.register_student(student_id)

    mycourse.append(cou)


