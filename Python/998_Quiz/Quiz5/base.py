n = input("What is your favorite number? (My favorite number is 00) ")
a = int(input("What is your age? "))
x = int(n[22:len(n)])*a
n = n[0:22]
print(n+str(x))