f = 0
T = int(input())
result = ""
for i in range(T):
    N = input()
    if N.startswith('0'):
        for s in N:
            if s == '.':
                continue
            f = f + 1
        if f == 11:
            result += "YES\n"
        else:
            result += "NO\n"
        f = 0
    else:
        for s in N:
            try:
                x = int(s)
                f = f + 1
            except:
                continue
        if f == 10:
            result += "YES\n"
        else:
            result += "NO\n"
        f = 0
print(result)
