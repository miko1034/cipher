#asks for message
message = str(input("Enter the text you want to encrypt? "))

def encrypt(text):
    text = text.encode("utf-8")
    text = text.hex()
    return text

for i in range(len(message)):
    if message[i].isalpha():
        pass

