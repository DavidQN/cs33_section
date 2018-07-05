# We create our list which is currently empty
l = []

# We store the input call onto a variable called 'name'
name = input()

# while 'name' variable does not have 'STOP' inputted continue doing everything inside the while loop
while name != "STOP":
    # add name onto the list 'l'
    l.append(name)
    # call 'name' again
    name = input()

# print the sorted list 'l'
print(sorted(l))

