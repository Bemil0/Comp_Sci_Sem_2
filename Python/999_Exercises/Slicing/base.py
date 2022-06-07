x = input("What is your First and Last name? ")
for y in range(0,len(x)):
    print(x[0+int(y):1+int(y)])


for y in range(0,len(x)):
    if x[0+y:1+y] == " ":
        
        t = 0+y
        r = 1+y
        last = (x[t+1:len(x)])
        first = (x[0:t-0])
        print(last + " " + first)