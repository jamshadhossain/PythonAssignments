temp=int(input("Enter Temperature: "))

def main():
    if temp >=60 and temp <=89:
        print("warm")
    elif temp>=90:
        print("hot")
    else:
        print("chilly")
main()
