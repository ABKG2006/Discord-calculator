e=2.718281828459045
pi=3.141592653589793
omited_chars="wyuığüadfghjklşzxvbmöçQWERTYUIOPĞÜİŞLKJHGFDSA!?_"
def calculate(express):
    if omited_chars in str(express):
        return "Invalid chars in expression"
    else:
        try:
            return str(eval(clean(express)))
        except:
            return "Invalid input"

        
def sqrt(a):
    return a**2
def taylorsin(a):
    return a-a**3/6+a**5/120-a**7/5040+a**9/362880-a**11/39916800+a**13/6227020800

def taylorcos(a):
    return 1-a**2/2+a**4/24-a**6/720+a**8/40320-a**10/3628800+a**12/479001600
def sin(a):
    a=a%(2*pi)
    region=a//(pi/2)
    a=a%(pi/2)
    match region:
        case 0:
            return taylorsin(a)
        case 1:
            return taylorcos(a)
        case 2:
            return -taylorsin(a)
        case 3:
            return -taylorcos(a)
def cos(a):
    a=a%(2*pi)
    region=a//(pi/2)
    a=a%(pi/2)
    match region:
        case 0:
            return taylorcos(a)
        case 1:
            return -taylorsin(a)
        case 2:
            return -taylorcos(a)
        case 3:
            return taylorsin(a)
def tan(a):
    return sin(a)/cos(a)
def cot(a):
    return cos(a)/sin(a)
def sec(a):
    return 1/cos(a)
def cosec(a):
    return 1/sin(a)
def clean(a):
    a = a.replace("^","**")
    a = a.replace("deg","*pi/180")
    return a