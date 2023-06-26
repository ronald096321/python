print ("Welcome to student marks portal");
numberOfStudents = input("Do you want to add a student Y / N : ");
students = [];
while (numberOfStudents =='Y') :
    subjects = [];
    totalMarks = 0;
    name = input("Please enter the name of the student : "); 
    addSubject = input("Do you want to add subject and marks of students Y / N : ");
    while(addSubject == 'Y') : 
        subjectName = input("Enter Subject name : ");
        subjectMarks = int(input("Enter Marks : "));
        totalMarks += subjectMarks;
        subDict = {
            "S_subject" : subjectName,
            "S_marks" : subjectMarks
        }
        subjects.append(subDict);
        addSubject = input("Do you want to add subject and marks of students Y / N");

    Maxscore =  len(subjects) * 100 ; 
    print('max score ' , Maxscore)
    percentage = (totalMarks / Maxscore) * 100 ;
    print("Percentage" ,percentage);
    student = {
        "S_name" : name,
        "S_subjects" : subjects,
        "totalMarks" : totalMarks,
        "S_percentage" : percentage
    }
    
    students.append(student);
    numberOfStudents = input("Do you want to add student Y /N : ");


print('students added are ' , students);



