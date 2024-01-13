import random
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
#randomising fragmented_text and storing the order in order list
print(f"\nfragmented text: {fragmented_text}\nfragmented text length: {len(fragmented_text)}\n")
order = []
#broken code starts here ----------
reorganised_fragmented_text = []
for i in range(len(fragmented_text)):
    chosen_index = random.randint(0,len(fragmented_text))
    if chosen_index in order:
        continue
    else:
        order.append(chosen_index)
        index_of_item_to_remove = fragmented_text.index(fragmented_text[chosen_index])
        reorganised_fragmented_text.append(fragmented_text.pop(index_of_item_to_remove))
#okay so the code above chooses the same index multiple times. 
#sometimes if you run the code it will work but only reorganise the first couple of objects in 
#the list, and sometimes it will spit out IndexError
#idk how to fix this
#bad code alert
#broken code ends ----------
print(f"\norder: {order}\norder length: {len(order)}\n")
print(f"\nreorganised fragmented text: {reorganised_fragmented_text}\nreorganised fragmented text length: {len(reorganised_fragmented_text)}\n")