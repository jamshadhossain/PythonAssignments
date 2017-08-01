lis = []
num = int(input("How many numbers would you like to enter: "))
for n in range(num):
    numbers = int(input("Enter your number:"))
    lis.append(numbers)
    lis.sort()
print("Maximum element in the list is :", lis[num-1])
print("Minimum element in the list is :", lis[0])
