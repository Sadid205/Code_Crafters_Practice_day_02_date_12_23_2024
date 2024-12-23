def next_alphabet(charecter):
    char_int = ord(charecter)
    if charecter!="z":
        next_char = chr(char_int+1)
        return next_char
    else:
        return "a"

charecter_input = input("")
print(next_alphabet(charecter=charecter_input))