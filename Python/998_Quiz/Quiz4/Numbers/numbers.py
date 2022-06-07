mynumbers = [6,9,32,28,15,22,3,18]

q = (mynumbers[0] + mynumbers[1] + mynumbers[2] + mynumbers[3] + mynumbers[4] + mynumbers[5] + mynumbers[6] + mynumbers[7])
w = q/len(mynumbers)
print("The Average is: "+ str(w))

a = 100000000 
for i in mynumbers:
    if i < a:
        a = i 
print("The minimum is: "+str(a))

b = 0 
for i in mynumbers:
    if i > b:
        b = i 
print("The Maximum is: "+str(b))
