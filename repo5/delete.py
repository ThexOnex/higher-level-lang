taille = 0
t = [1, 2, 3, 4, 5]
element = 2
taille = len(t)


def surprime(t, element):
    taille = len(t)
    pos = -1
    for i in range(taille):
        if t[i] == element:
            pos = i
            break
        i += 1

    for i in range(pos, taille-1):
        t[i] = t[i+1]

    taille -= 1
    t = t[:taille]
    if pos == -1:
        return -1
    return t


r = surprime(t, element)
if r == -1:
    print("on n'a pas trouver l'element")
else:
    print("le tableau : ", r)
