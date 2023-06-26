def calcluatePercentageofStudent(subjects) :
    if len(subjects) > 0 :
        totalmarks = 0;
        maxMarks = len(subjects) * 100;
        for subject in range(len(subjects)) :
            totalmarks += subjects[subject]['marks'];
        return totalmarks / maxMarks * 100;