myDictionary = {"Name":"Kamran",
                "Age":"19",
                "Friend":"Maaiki",
                "School":"John Brown University"}


myDictionary.update ({"Hometown":"Bentonville",
                      "Favortie Sport":"Basketball"})   # adding code

del myDictionary["Friend"]                      # deleting code

myDictionary["Hometown"] = "Minnesota"              # replacing code


fullname = input("Enter your full name: ")
myDictionary.update ({"Full Name":fullname})        # User inputs an (already) set input

print(myDictionary)

