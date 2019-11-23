import re
while True:
    

    print("Input desired string")
    print("Type STOP to end program")
    string=input()
    if string == ("STOP"):
        break
    print("this puts W infront of everything")
    newString = re.compile(r'(\w)(\w*)')
    print(newString.sub(r'w\2',  string))
    #print(newString)

    print()
    print("This makes things go UwU")
    newString = re.sub(r'[l]', "w", string,re.IGNORECASE)
    newString = re.sub(r'[o]', "oo", newString,re.IGNORECASE)
    newString= re.sub(r'[r]', "w", newString,re.IGNORECASE)
    print (newString)

    print()
    print("Pig Latin maybe")
    namesRegex = re.compile(r'(\w)(\w*)')
    print(namesRegex.sub(r'\2\1ay',  string))

    print()
    print("The selfish program")
    namesRegex = re.compile(r' [A-Z]\w*')
    selfish =(namesRegex.sub(r'Evan',  string))
    namesRegex = re.compile(r'[A-Z]\w*.[A-Z]\w*')
    selfish =(namesRegex.sub(r'Evan Fisher',  selfish))
    namesRegex = re.compile(r'[A-Z]\w*.[A-Z]\w*.[A-Z]\w*')
    selfish =(namesRegex.sub(r'Evan Fisher-Perez',  selfish))
    namesRegex = re.compile(r'[A-Z]\w*.[A-Z]\w*.[A-Z]\w*.[A-Z]\w*')
    selfish =(namesRegex.sub(r'Evan Michael Fisher-Perez',  selfish))
    print(selfish)

    print()
    print("another command")


print("you have broken out")
#Exit Command
print("Press enter to exit:")
input()
