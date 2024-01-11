#asks for message
message = str(input("Enter the text you want to encrypt? "))

def encrypt(text):
    fragmented_text = []
    #encodes
    text = text.encode("utf-8").hex()
    #splits into a list
    split_text = [*text]
    #converts every int to 4 bit binary
    for i in range(len(split_text)):
        if split_text[i].isalpha() == False:
            split_text[i] = bin(int(split_text[i]))[2:]
        if len(split_text[i]) == 3:
            split_text[i] = "0" + split_text[i]
    #joins the list back together and reverses it
    text = "".join(split_text)[::-1]
    #adds letters so it is divisable by 4
    while True:
        if (len(text)%4) == 0:
            break
        else:
            text = text+"H"
    #splits the text into segments of length four and adds to list fragmented_text
    while text != "":
        fragmented_text.append(text[:4])
        text = text[4:]
    return fragmented_text        

final = encrypt(message)
print(final)