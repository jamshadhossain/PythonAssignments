def greeting():
    myName = input('What is your name?: ')
    print('It is nice to meet you, ' + myName)
    favColor = input('what is your favorite color?: ')
    print(favColor + "? That's a nice color")
    favFood = input("what is your favorite Food?: ")
    print(favFood + " sounds yummy")
    a = input("Do you have to go?: ")
    if a=="no" or "n" or "nah":
        greeting()
    else:
        print("bye bye!")

greeting()
