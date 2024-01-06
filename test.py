#ignore this file dear user, this means nothing to the actual project :>

#var = "mio324nkl523"
#for i in range(len())
#newvar = int("".join(filter(var.isdigit(), var)))

#print(newvar)


var = "abc123"

def getdigit(string):
    to_return = []
    for i in range(len(string)):
        if string[i].isalpha() == False:
            to_return.append(string[i])
    return to_return

print(getdigit(var))