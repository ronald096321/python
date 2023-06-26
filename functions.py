from calfunctions.add import add;
from calfunctions.multiply import mul;
from calfunctions.sub import sub;
from calfunctions.div import div;

def calculator(operand1 : int , operand2 : int , operation) :
    if operand1 > 0 and  operand2 > 0  :
        if operation == '+' :
            return add(operand1 , operand2) ;
        elif operation =='*' :
            return mul(operand1 , operand2);
        elif operation == '-' :
            return sub(operand1 , operand2);
        elif operation == '/' :
            return div(operand1 , operand2);
    else :
        print("Please enter the operands greater then 0");
  




 
a = int(input("Please enter the operand 1 : "));
b = int(input ("please enter the operand 2 : "));
c = input ("Please enter the operation to perform : ");

result = calculator(a , b , c)
print("result of the operation " , result);
    