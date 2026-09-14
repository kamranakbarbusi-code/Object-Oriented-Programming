mylist = [3, 6, 8, 10, 15]

mylist.append(1)

mylist.remove(8)

mylist.sort()

print("The list is:", mylist)

old_element = int(input("What element would you like to change?:"))

if old_element in mylist:
    index = mylist.index(old_element)
    new_element = int(input("What element would you like to replace it with?:"))
    mylist[index] = new_element
    print("The new list is:", mylist)

else:
    print("Oops! That element is not in the list")

sort_option = input("Would you like to sort the list?")

if sort_option == "Yes" or "yes":
    mylist.sort()
    print("The list is:", mylist)
elif sort_option == "No":
    exit
