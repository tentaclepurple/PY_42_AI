# Put this at the top of your kata03.py file
kata = "The right format"

size = 39 - len(kata)
for i in range(size + 1):
    print("-", end="")
print(f"{kata}%")