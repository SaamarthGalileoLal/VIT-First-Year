def Calcfopy():
    a=float(input("Enter the first number: "))
    b=float(input("Enter the second number: "))
    add=a+b
    sub=a-b
    mul=a*b
    div=a/b
    print("If",a,"and",b,"are added then it will be",add)
    print("If",a,"and",b,"are Subtracted then it will be",sub)
    print("If",a,"and",b,"are multiplied then it will be",mul)
    print("If",a,"and",b,"are divided then it will be",div)

def calcdataskyoahhforcalcstuf():
    things=["+","-","*","/"]
    dathings=str(input("Enter the operation you want to perform (+, -, *, /): "))
    for i in things:
        if dathings==i:
            a=float(input("Enter the first number: "))
            b=float(input("Enter the second number: "))
            add=a+b
            sub=a-b
            div=a/b
            mul=a*b 
            if i=="+":
                add=a+b
                print("If",a,"and",b,"are added then it will be",add)
            elif i=="-":
                sub=a-b
                print("If",a,"and",b,"are Subtracted then it will be",sub)
            elif i=="*":
                mul=a*b
                print("If",a,"and",b,"are multiplied then it will be",mul)
            elif i=="/":
                div=a/b
                print("If",a,"and",b,"are divided then it will be",div)
        else:
            print("dang bro this aint no scientific calculator, you can only use +, -, *, /")
            pass

calcdataskyoahhforcalcstuf()
Calcfopy()