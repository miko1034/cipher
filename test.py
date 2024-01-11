#ignore this file dear user, this means nothing to the actual project :>

#var = "mio324nkl523"
#for i in range(len())
#newvar = int("".join(filter(var.isdigit(), var)))

#print(newvar)
        #make it so it appends furst 4 letters to a list, joins the list and 
        #then appends to a list of fragments that is the returned
def split(var):
    to_return = []
    #gets first 4 of var
    while var != "":
        to_return.append(var[:4])
        var = var[4:]
    return to_return

var = "mikolaj"
print(f"the variable is: {var}")
print(f"the variable length is: {len(var)}")

while True:
    if (len(var)%4) == 0:
        break
    else:
        var = var+"H"
    

print(f"the variable length is: {len(var)}")
print(var)
print(split(var))