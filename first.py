#print ("hellow world");

#name = "vinay";
#subject1 = 60;
#subject2 = 70;
#subject3 = 90;

#print(name , subject1+subject2+subject3);


#data1 = "name";
#data2 = 12.2;
#data3 = 12;
#data4 = [];

#print(type(data1),type(data2),type(data3),type(data4));


# name1 = input("Please Enter Your Name : ");
# print("Enterd Name" , name1);


# name = input("Enter student name :" );
# maths = int(input("enter maths score : "));
# science = int(input("enter science marks : "));
# englis = int(input("enter english score :"));
# totalmarks = maths+science+englis;
# percentage = int((totalmarks / 300 )*100);

# if percentage >= 90 : print(name , 'has total marks' , totalmarks , 'with percentage ' , percentage , 'has passed with S grade!' );

# elif percentage >= 80 & percentage < 90 : print(name , 'has total marks' , totalmarks , 'with percentage ' , percentage , 'has passed with A grade!' );

# elif percentage >= 70 & percentage < 80 : print(name , 'has total marks' , totalmarks , 'with percentage ' , percentage , 'has passed with B grade!' );

# elif percentage >= 60 & percentage < 70 : print(name , 'has total marks' , totalmarks , 'with percentage ' , percentage , 'has passed with C grade!' );

# elif percentage >= 50 & percentage < 60 : print(name , 'has total marks' , totalmarks , 'with percentage ' , percentage , 'has passed with D grade!' );

# elif percentage >= 30 & percentage < 50 : print(name , 'has total marks' , totalmarks , 'with percentage ' , percentage , 'has passed with D grade!' );

# else : print(name , 'has total marks' , totalmarks , 'with percentage' , percentage , 'has failed !')


operator1 = int(input("enter value1 : "));
if operator1 <= 0 : 
    operator1 = int(input("enter value1 greater then 0 : "));
operator2 = int(input("enter value2 : "));
if operator2 <= 0 : 
    operator2 = int(input("enter value2 greater then 0 : "));

operation = input("enter operation to perform : ");

if operation == "+" : print("Resule",operator1+operator2);
elif operation =="*" : print("Resule",operator1*operator2);
elif operation == "/" : print("Resule",operator1/operator2);
elif operation == "-" : print("Resule",operator1-operator2);
else : print("this operation cannot be performed ");