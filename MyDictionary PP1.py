myplayers = {"Player 1":"Lebron James", "Player 2":"Steph Curry", "Player 3":"Anthony Edwards", "Player 4":"Victor Wembanyama"}
print(myplayers)
i = 1
while (True):
    print("1: Add Player")
    print("2: Remove Player")
    print("3: Replace Player")
    print("4: Print Player Dictionary")
    print("5: exit")
    choice = int(input("Enter your choice: "))
    if choice == 5:
        break

    if choice == 1 :
        addedplayer = input("What player would you like to add?")
        for player in myplayers:
            i = i + 1
        myplayers.update({"Player " + str(i): addedplayer})

        print("The list is now:", myplayers)

    elif choice == 2 :
        removeplayer = input("What player would you like to remove?")

        for i in myplayers:
            if myplayers[i] == removeplayer:
                del myplayers[i]
                break
        print("The list is now:", myplayers)


    elif choice == 3 :
        print(myplayers)
        oldplayer = input("What player would you like to change?")
        newplayer = input("What player would you like to add in replacement?")

        for i in myplayers:
            if myplayers[i] == oldplayer:
                myplayers[i] = newplayer
                print("The list is now:", myplayers)

    elif choice == 4 :
        print(myplayers)




