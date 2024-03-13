def main():
    message = input("MEssage:").encode("utf-8").hex()
    it = iter(message)
    message = []
    for i in it:
        print(i)
        if i.isalpha() == False:
            message.append(bin(i))
            next(it)
            continue
        message.append(i)
        next(it)
            
    print(message)


main()