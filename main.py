#asks for message
message = str(input("Enter the text you want to encrypt? "))

def encrypt(text):
    text = text.encode("utf-8").hex()
    for i in range(len(message)):
        if text[i].isalpha() == False:
            text[i].replace(text[i],bin(text[i])[2:])
        else:
            pass
    return text

final = encrypt(message)
print(final)