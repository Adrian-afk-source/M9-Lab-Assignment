#Adrian Garcia
#11/19/24
#In problem 2 the code will give us a variable that is greater than 10 and then tell us what the third element is. 

L = [57, 83]
counter = 0
while counter <= 10:
    L.append(counter)
    counter += 1
print(f"The list has {len(L)} elements.")
print(f"The third element in the list is {L[2]}.")