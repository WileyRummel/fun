""" Isogram testing, write a function that determines if a string has no letters appreaing twice """
#convert the work into a string.  Sort the string with sort(), iterate through the list and compare each letter to the letter after.  
test = "Dermatoglyphics"
def iso(test):
    x = 1
    test = list(test.lower())
    test.sort()
    for i in test:
        if x < len(test):
            print(i + " , " + test[x])
            if i == test[x]:
                return False
            x += 1

    return True
print(iso(test))