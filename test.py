#ignore this file dear user, this means nothing to the actual project :>

var = "mio324nkl523"

for i in range(len(var)):
    try:
        print(int(var[i]))
    except ValueError:
        i += 1
        print(int(var[i]))