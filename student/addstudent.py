from student.addsubject import addSubjectToList;
from student.calculatepercentage import calcluatePercentageofStudent;
def addStudentToList() :
    subjects = [];
    name = input("Please enter the student name : ");
    inputPlaceholder = "Do you want to add subject and marks of " + name + " " + "Y/N" + " :" ;
    addSubject = input(inputPlaceholder);
    while(addSubject == 'y' or addSubject == 'Y') :
        # print("add");
        subjects.append(addSubjectToList());
        print(subjects);
        addSubject = input(inputPlaceholder);
    percentage = calcluatePercentageofStudent(subjects);
    return {
        "name" : name,
        "subjects" : subjects,
        "percentage": percentage  
    };
  
