x = int(input("How many numbers do you want: "))
lis = []
for o in range(0,x):
    import random
    z = (random.randrange(1,11))
    lis.append(z)
print("your numbers are: "+ str(lis))