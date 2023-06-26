def addSubjectToList() : 
    subject = input("Enter the subject name : ");
    marks  = int(input("Enter the Marks obtained "));
    return{
                "subject": subject,
                "marks" : marks
            }