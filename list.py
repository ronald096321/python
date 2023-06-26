
studentNames = ["Sohail" , "Sanjoy" , "Neeraj"];
scienceMarks = [30 , 30 , 50];
mathsMarks = [70, 70 , 90];
englishMarks = [80 , 80 , 70];
totalMarks = [];
studentPercentages = [];
maxScorrerName = '';
maxPercentScored = 0;
sortListOnPercentageNames  = [];
sortListOnPercentage = [];

# studentName = input("Enter student Name :");
# scienceMark = int(input("Enter Science Score : "));
# mathsMark = int(input("Enter Maths Score : "));
# englushMark = int(input("Enter English Score : "));

# studentNames.append(studentName);
# scienceMarks.append(scienceMark);
# mathsMarks.append(mathsMark);
# englishMarks.append(englushMark);


studentNames.append("Vinay");
scienceMarks.append(80);
mathsMarks.append(99);
englishMarks.append(88);

#Find the % of each student
for i in range(len(studentNames)) : 
    totalMarks.append(scienceMarks[i] + mathsMarks[i] + englishMarks[i]);
    studentPercentages.append(totalMarks[i] /300 *100 );
    # print('Total Marks of' , studentNames[i] , 'is' , totalMarks[i] );
    # print('Total Percentage of' , studentNames[i] , 'is' , studentPercentages[i] );
    

#Find the topper of the class
for index in range (len(studentNames)) : 
    tempMaxScore = studentPercentages[index];
    if tempMaxScore > maxPercentScored :
        maxPercentScored = tempMaxScore
        maxScorrerName = studentNames[index];

# print("Class topper is" , maxScorrerName , 'with ' , maxPercentScored , '%');
# print("student percentages" , studentPercentages);

#Sort the Lists based on Ranks
for x in range(0,len(studentNames)) : 
    for y in range (x + 1 , len(studentNames)) :
        if studentPercentages[x] < studentPercentages[y]  :
             tempPercent = studentPercentages[x];
             studentPercentages[x] = studentPercentages[y];
             studentPercentages[y] = tempPercent;
             tempStudentName = studentNames[x];
             studentNames[x] = studentNames[y];
             studentNames[y] = tempStudentName;

      

#Print first 3 Students
for index in range(0 , 3) : 
    print(studentNames[index] , 'Has secured' , index + 1 , 'Rank', 'With %' , studentPercentages[index]);

# print("Final sort List" , studentPercentages);
# print("Final sort List" , studentNames);
    


    