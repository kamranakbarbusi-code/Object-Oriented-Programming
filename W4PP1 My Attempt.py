mylist = [3, 6, 8, 10, 15]

mylist.append(1)

mylist.remove(8)

mylist.sort()

print("The list is:", mylist)

replace = int(input("What number would you like to replace?:" ))

insert = int(input("What number would you like to insert?:" ))

if replace == 3:
    mylist.remove(3)
    mylist.append(insert)

elif replace == 6:
    mylist.remove(6)
    mylist.append(insert)

elif replace == 10:
    mylist.remove(10)
    mylist.append(insert)

elif replace == 15:
    mylist.remove(15)
    mylist.append(insert)

mylist.sort()
print("The new list is:", mylist)




