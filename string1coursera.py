def initials(phrase):
    words = phrase.upper()
    result = words[0]
    for i in range(1,len(words)) :
        if words[i]==" ":
            result += words[i+1]
    return result

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS