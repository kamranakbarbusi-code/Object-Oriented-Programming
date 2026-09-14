while(True):
    print("1 Add an Item")
    print("2 Remove an Item")
    print("3 Sort")
    print("4 Replace an Item")
    print("5 Exit")
    choice = int(input("Enter your Choice:"))
    if choice ==5 :
        break

    if choice == 1:
        user_add = int(input("What item would you like to add?:"))
        mylist.append(user_add)
        print("The new list is:", mylist)

    elif choice == 2:
        user_remove = int(input("What item would you like to remove?:"))
        mylist.remove(user_remove)
        print("The new list is:", mylist)

    elif choice == 3:
        mylist.sort()

    elif choice == 4:
        old_element = int(input("What element would you like to change?:"))

        if old_element in mylist:
            index = mylist.index(old_element)
            new_element = int(input("What element would you like to replace it with?:"))
            mylist[index] = new_element
            print("The new list is:", mylist)

        else:
            print("Oops! That element is not in the list")






