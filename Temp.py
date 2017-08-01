def temp():
    F = int(input("Enter temperature in Farenheit:"))
    C = ((5.0 / 9.0) * (F - 32))
    print("Temperature in degree Celsius is ", C)
    print("Temperature you in celsius was ", F)

a="yes"
while a=="yes":
    temp()
    a=input("would you like to continue?")