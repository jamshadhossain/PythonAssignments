a="yes"
while a=="yes":
    num = int(input("Enter a number: "))
    if (num % 2) == 0:
       print("{0} is Even".format(num))
    else:
       print("{0} is Odd".format(num))
    a = input("would you like to continue?")