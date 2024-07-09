def sum(n1, n2):
    return n1-n2

def subtraction(n1,n2):
    return n1-n2

def division(n1,n2):
    if(n1 == 0 or n2 ==0):
        print("You cannot divide by zero!")
    return n1/n2

def multiplication(n1,n2):
    return n1*n2

def power(n1,n2):
    return n1**n2

def again():
    calcAgain = input('''Do you want to use the calculator again?
Y or y for Yes
N or n for no ''')
    if(calcAgain.upper() == 'Y'):
        calculate()
    elif(calcAgain.upper() == 'N'):
        print("See you soon!")
    else:
        again()

def calculate():
    operation = input('''What type of account do you want to do?
    + for sum 
    - for Subtraction 
    / for Division 
    * for Multiplication 
    ** for Power ''')
    n1 = int(input("Insert your first number: "))
    n2 = int(input(f"Allright, {n1}, now, insert your second number: "))

    match operation:
        case '+':
            print(f"The sum is {sum(n1,n2)}")
        case '-':
            print(f"The subtraction is {subtraction(n1,n2)}")
        case '/':
            print(f"The divison is {division(n1,n2)}")
        case '*':
            print(f"The multiplication is {multiplication(n1,n2)}")
        case '**':
            print(f"The power of {n1}^{n2} is {power(n1,n2)}")

    again()

calculate()
