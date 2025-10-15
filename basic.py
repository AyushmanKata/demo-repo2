user = int(input("Enter a number: "))
if user % 2 == 0:
    print("{} is even".format(user))
else:
    print("{} is odd".format(user))
print()
user = str(input("Press any key to exit : ")).lower