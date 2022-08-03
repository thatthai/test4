mes = input()
new_mes = ""

for c in mes :
    if c.isupper() :
        new_mes += c.lower()
    else :
        new_mes += c.upper()
print(new_mes)