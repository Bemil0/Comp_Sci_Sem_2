x = int(input("Please enter the length of the line: "))
y = input("Please enter horizontal or vertical: ")
if y == "vertical":
    for z in range(0,x):
        print("*")
elif y == "horizontal":
    for z in range(0,x):
        print("*", end="")
else:
    print("Please choose either Horizontal or Vertical")