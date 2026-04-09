text = input("Enter string: ")

seen = ""
dup = ""

for ch in text:
    if ch in seen and ch not in dup:
        dup += ch + " "
    else:
        seen += ch

print(dup)