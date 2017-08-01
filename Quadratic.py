print("Welcome to the Program! Please enter value of A,B,C and X at the corresponding prompts")
a=int(input("What is the value of A: "))
b=int( input("What is the value of B: "))
c= int(input("What is the value of C: "))
x= int(input("What is the value of X: "))
answer= a*(x**2)+b*x+c
print("The following quadratic was entered:",a,"X^2+",b,"X+",c)
print("The value of the quadratic is ",answer)