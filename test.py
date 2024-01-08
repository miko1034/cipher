#ignore this file dear user, this means nothing to the actual project :>

#var = "mio324nkl523"
#for i in range(len())
#newvar = int("".join(filter(var.isdigit(), var)))

#print(newvar)


var = "11"
print(f"the variable is: {var}")
print(f"the variable length is: {len(var)}")

while True:
    if (len(var)%4) == 0:
        break
    else:
        var = var+"H"

print(f"the variable length is: {len(var)}")
print(var)