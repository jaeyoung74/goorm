#구구단

def gugu(n):
    result = []
    i = 1
    while i < 10:
        result.append(n*i)
        i += 1
    return result

print(gugu(3))
