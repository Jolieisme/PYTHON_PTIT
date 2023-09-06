s = input().lower()
if s[len(s) - 3:] == ".py":
    print("yes")
else:
    print("no")