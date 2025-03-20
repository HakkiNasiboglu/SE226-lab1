import random
import string

passwords = []
for _ in range(5):
    password = ''.join(random.choices(string.ascii_lowercase, k=15))
    passwords.append(password)

print("Chose 5 letters (lowercase only) and their replacements (3 each):")
escape=0
Dict={}
while escape < 5 :
    char=input("Enter a lowercase letter")
    replacements=set()
    for x in range(3):
        rp=input("Enter 3 replacements for each letter:")
        replacements.add(rp)
    Dict[char]=replacements
    escape = escape + 1
print(Dict)

for p in passwords: 
    newPass = []
    for c in p:
        if c in Dict:
            new = random.choice(list(Dict[c]))
            newPass.append(new)
        else:
            newPass.append(c)
            




print("GENERATED PASSWORDS:")
print("STRONG PASSWORDS:")
print(newPass)
print("WEAK PASSWORDS:")
