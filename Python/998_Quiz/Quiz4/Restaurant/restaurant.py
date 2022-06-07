import random
restaurant = input("Pick one of three restaurants; Cheesecakefactory, CPK, Starbucks")
Cheesecakefactory = ["FRIED SHRIMP PLATTER", "CHARGRILLED NEW YORK STEAK", "LASAGNA VERDE"]
CPK = ["MEAT CRAVERS PIZZA", "THE WORKS PIZZA", "GARLIC CREAM FETTUCINE"]
Starbucks = ["IMPOSSIBLE BREAKFAST SANDWICH", "BACON GOUDA AND EGG SANDWICH", "DOUBLE-SMOKED BACON CHEDDAR AND EGG SANDWICH"]
if restaurant == "Cheesecakefactory":
    print("Menu for Cheesecakefactory: " + str(Cheesecakefactory))
    w = (random.randrange(3))
    print("Our suggested menu item is: " + Cheesecakefactory[w])
elif restaurant == "CPK":
    print("Menu for CPK: " + str(CPK))
    w = (random.randrange(3))
    print("Our suggested menu item is: " + CPK[w])
elif restaurant == "Starbucks":
    print("Menu for Starbucks: " + str(Starbucks))
    w = (random.randrange(3))
    print("Our suggested menu item is: " + Starbucks[w])
else:
    print("Please enter one of the following: Cheesecakefactory, CPK, or Starbucks")