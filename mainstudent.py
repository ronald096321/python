from student.addstudent import addStudentToList;

print("Welcome to the student result management portal : ");
addStudent = input("Do you want to add stuydent Y/N : ");
students = [];
while(addStudent == 'Y' or addStudent == 'y') : 
    students.append(addStudentToList());
    addStudent = input("Do you want to add stuydent Y/N : ");

print('Students List' , students);