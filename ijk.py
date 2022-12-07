input("enter any data : ")
azhar = input()
if ord(azhar)>=65 and ord(azhar)<=90:
    print("you entered a upper case letter:")
    if azhar in ["A","E","I","O","U"]:
        print("you entered a vowel")
    else :
        print("you entered a consent")
elif  ord(azhar)>=97 and ord(azhar)<=122:
        print("you entered a lower case letter")
    if azhar in ["a","e","i","o","u"]:
        print("you entered a vowel")
    else :
        print("you entered a consent")
else :
    print("you did not enter alphabet")

