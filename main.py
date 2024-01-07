#asks for message
message = str(input("Enter the text you want to encrypt? "))

def encrypt(text):
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
    #splits everything into four equal parts
    print(len(text))
    return text

final = encrypt(message)
print(final)