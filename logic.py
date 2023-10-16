import requests
i=1j
e=2.718281828459045
pi=3.141592653589793
clean_dict={"^":"**","deg":"*pi/180","1j":"i","j":"i","print":"",":":"/","send":"","import":""}
def calculate(express):
    try:
        x=eval(clean(express))
        if x.imag!=0: 
            if x.real!=0:
                x=clean(str(x))
                return x[1:-1]
            else:
                x=clean(str(x))
                return x
        else:
                return str(x.real)
    except:
        return "invalid input"


        
def sqrt(a):
    return a**(1/2)
def taylorsin(a):
    return a-a**3/6+a**5/120-a**7/5040+a**9/362880-a**11/39916800+a**13/6227020800

def taylorcos(a):
    return 1-a**2/2+a**4/24-a**6/720+a**8/40320-a**10/3628800+a**12/479001600
def sin(a):
    if a.imag==0:
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
    else:
        return (e**(i*a)-e**(i*-a))/(2*i)
def cos(a):
    if a.imag==0:
        a=a%(2*pi)
        region=a.real//(pi/2)
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
    else:
        return (e**(i*a)+e**(i*-a))/2
def tan(a):
    return sin(a)/cos(a)
def cot(a):
    return cos(a)/sin(a)
def sec(a):
    return 1/cos(a)
def cosec(a):
    return 1/sin(a)
def clean(a):
    for i in clean_dict.keys():
        a=a.replace(i,clean_dict[i])
    return a
def get_foxxo():
    res = requests.get('https://randomfox.ca/floof')
    data = res.json()
    return data['image']
