#Save the list in a local variable
file = open("list.txt", "r")

l = []

tmp = 0
for x in file:
    l.append(file.readline())
    l[tmp] = l[tmp][:-1]
    tmp+=1

file.close()