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
#reorganising 3,1,4,2 then rest in order
reorganised_fragments = []
pattern = [2,0,3,1]
thefour = []
#gets the four at the indexes of pattern[]
print(f"fragmented: {fragmented_text}")
for i in range(len(pattern)):
    thefour.append(fragmented_text[pattern[i]])
    fragmented_text.remove(fragmented_text[pattern[i]])

#code above doesnt really work
#pls fix

print(f"\npattern: {pattern}\n")
print(f"the four: {thefour}")
print(f"newly removed: {fragmented_text}")

reorganised_fragments = thefour + fragmented_text
#index error on line above
#fix it. now.
print(f"reorganised: {reorganised_fragments}")