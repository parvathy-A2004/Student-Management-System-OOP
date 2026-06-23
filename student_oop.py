class Student:
    def __init__(self,id,name,course):
        self.id = id
        self.name = name
        self.course = course
    def display(self):
        print("ID:",self.id)
        print("Name:",self.name)
        print("Course:",self.course)
        print()

students = []

def createStudent():
        try:
            id = int(input("Enter id"))
        except ValueError:
            print("Enter valid input")
            return
        for i in students:
            if i.id == id:
                print("Duplicate id")
                return
            
        name = input("Enter name")
        course = input("Enter course")
        s = Student(id,name,course)
        students.append(s)

def searchStudent():
    try:
        st_id = int(input("Enter id"))
    except ValueError:
        print("Enter valid input")
        return

    found = False
    for i in students:
        if i.id == st_id:
            i.display()    
            found = True 
            break
    if not found:
        print("Student not found")


def viewStudents():
    if students:
         for i in students:
             i.display()
    else:
        print("No students")
def deleteStudent():
    if students:
        found = False
        try:
           stu_id = int(input("Enter id"))
        except ValueError:
            print("Enter valid input")
            return
        for i in students:
            if i.id == stu_id:
                students.remove(i)
                print("Deleted successfully")
                found = True
                break
        if not found:
            print("No student in this id")
    else:
        print("No students")

def updateStudent():
    if students:
        try:
            stu_id = int(input("Enter id"))
        except ValueError:
            print("Enter valid input")
            return
        
        found = False
        for i in students:
            if i.id == stu_id:
                try:
                    new_id = int(input("Enter new id"))
                except ValueError:
                    print("Enter valid input")
                    return
                for j in students:
                    if j.id == new_id and new_id != stu_id :
                         print("Student with this id already present")
                         return

                new_name = input("Enter name")
                new_course = input("Enter course")
                i.id = new_id
                i.name = new_name
                i.course = new_course
                print("Updated successfully")
                found = True
                break
                
                   
        if not found:
            print("No student in this id")
    else:
        print("No students")
                   
def countStudents():
    if students:
        print("Total no of students: ",len(students))
    else:
        print("No students")

def countStudentsByCourse():
    if students:
        count = 0
        found = False
        stu_course = input("Enter course")
        for i in students:
            if i.course.lower() == stu_course.lower():
                count +=1
                found = True
        if found:
            print("Total no of students in ",stu_course," is: ",count)
        else:
            print("No students in this course") 
    else:
        print("No students")

def searchByName():
    if students:
        stu_name = input("Enter name")
        found = False
        for i in students:
            if i.name.lower() == stu_name.lower():
                i.display()
                found = True
        if not found:
            print("No student in this name")
    else:
        print("No students")

def searchByCourse():
    if students:
        found = False
        stu_course = input("Enter course")
        for i in students:
            if i.course.lower() == stu_course.lower():
                i.display()
                found = True
        if not found:
            print("No students in this course")
    else:
        print("No students")

def sortById():
    if students:
        sorted_list = sorted(students, key= lambda x: x.id)
        for i in sorted_list:
            i.display()
    else:
        print("No students")

def sortByName():
    if students:
        sorted_list = sorted(students, key= lambda x: x.name.lower())
        for i in sorted_list:
            i.display()
    else:
        print("No students")

def saveToFile():
    if students:
        with open("stu_data.txt","w") as file:
            for i in students:
                file.write(f"{i.id},{i.name},{i.course}\n")
        print("Data save successfully")
    else:
        print("No students")
    
def loadFromFile():
    try:
        students.clear()
        with open("stu_data.txt","r") as file:
            for line in file:
                data = line.strip().split(",")
                s = Student(int(data[0]),data[1],data[2])
                students.append(s)
            print("loaded successfully")
    except FileNotFoundError:
        print("File not found")


while True:
    print("1.Create student")
    print("2.View students")
    print("3.Search student")
    print("4.Delete student")
    print("5.Update student")
    print("6.Count Students")
    print("7.Count students by course")
    print("8.Search student by name")
    print("9.Search student by course")
    print("10.Sort by id")
    print("11.Sort by name")
    print("12.Save to file")
    print("13.Load from file")
    print("14.Exit")
    try:
       choice = int(input("Enter your choice"))
    except ValueError:
        print("enter valid choice")
        continue

    if choice == 1:
        createStudent()

    elif choice == 2:
        viewStudents()

    elif choice == 3:
        searchStudent()

    elif choice == 4:
        deleteStudent()

    elif choice == 5:
        updateStudent()

    elif choice == 6:
        countStudents()
    
    elif choice == 7:
        countStudentsByCourse()

    elif choice == 8:
        searchByName()

    elif choice == 9:
        searchByCourse()

    elif choice == 10:
        sortById()
    
    elif choice ==11:
        sortByName()

    elif choice == 12:
        saveToFile()

    elif choice == 13:
        loadFromFile()

    elif choice == 14:
        print("program ends")
        break

    else:
        print("invalid choice")
        

