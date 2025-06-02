str = input()
new_str = ''
for alpha in str:
    if alpha.isupper() == True:
        new_str += alpha.lower()
    elif alpha.islower() == True:
        new_str += alpha.upper()

print(new_str)