#ignore this file, dear user, this means nothing to the actual project :>
#this file is a mess
#i barely know whats going on here...

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
    

print(f"the variable length is after fillage: {len(var)}")
print(var)
fragmented_text = split(var)

#now carrying on from main function
from main import encrypt

fragmented_text = encrypt(var)
print(fragmented_text)
#reorganising 3,1,4,2 then rest in order
reorganised_fragments = []
pattern = [2,0,3,1]
i = 0
while len(reorganised_fragments) != 4:
    reorganised_fragments.append(fragmented_text[pattern[i]])
    fragmented_text.remove(fragmented_text[pattern[i]])
    i  = i + 1 # uh not sure if it works but imma just guess it is :)

        

#index error on line above
#fix it. now.
print(f"reorganised: {reorganised_fragments}")