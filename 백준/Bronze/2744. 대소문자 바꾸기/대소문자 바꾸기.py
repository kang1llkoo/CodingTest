words = input()
ans = ""
for word in words:
    if word.isupper() == 1:
        ans += word.lower()
    elif word.islower() == 1:
        ans += word.upper()

print(ans)