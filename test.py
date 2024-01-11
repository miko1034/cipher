#ignore this file, dear user, this means nothing to the actual project :>

def split(var):
    to_return = []
    while var != "":
        to_return.append(var[:4])
        var = var[4:]
    return to_return

var = "cooltext1"
print(f"the variable is: {var}")
print(f"the variable length is: {len(var)}")

while True:
    if (len(var)%4) == 0:
        break
    else:
        var = var+"H"
    

print(f"the variable length is: {len(var)}")
print(var)
fragmented_text = split(var)
print(fragmented_text)