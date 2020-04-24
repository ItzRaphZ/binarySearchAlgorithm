import math

#Save the list in a local variable
file = open("list.txt", "r")

l = []

tmp = 0
for x in file:
    l.append(x)
    l[tmp] = l[tmp][:-1]
    tmp+=1

file.close()

#Creates the left, middle, right variables
firstNum = l[0]

if len(l)%2==0:
    middle = len(l)/2
    middle -= 1
else:
    middle = (len(l)-1)/2

middle = math.floor(middle)
middleNum = l[middle]

lastNum = l[len(l)-1]

#Create the algorithm
Running = True

while Running == True:
    print("Answer true or false.")
    option = input(f"Is the number higher than {middleNum}: ").lower()

    if option == "true":
        print("true")
    elif option == "false":
        print("false")
    else:
        print(f"\n\nERROR: Answer not \"true\" or \"false\". Please answer again.")

    print("\n\n")

    



print(firstNum)
print(middleNum)
print(lastNum)