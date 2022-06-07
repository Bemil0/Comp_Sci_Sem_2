sentence = "whale hello there. Don't we all love whales? I absolutely love whales! whales are so huge!!!"

x=0
for y in range(0,len(sentence)):
    if sentence[0+y:5+y] == "whale":
        x = x+1
        
print("There are "+str(x)+" whales") 










#with open('moby.txt') as f:
#    for line in f:
#        sentence = line.strip()
#        ##YOUR CODE GOES HERE
#
#f.close()
