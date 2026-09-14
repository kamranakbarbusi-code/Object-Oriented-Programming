mylist = [2, 56, 23, 11, 99, 32]

mylist.append(66)                             // adding an element to the list
print(mylist)

mylist.remove(99)                         // remove the element
print(mylist)

mylist.pop(2)                            // removes the last element in the list
print(mylist)


mylist.sort()                          //
print(mylist)

newlist = mylist.copy()
newlist.append(1000)

new_value = int(input("Enter a number: "))
if new_value in mylist:
    print("Element is present in the list")
else:
    print("Element is not present in the list")
