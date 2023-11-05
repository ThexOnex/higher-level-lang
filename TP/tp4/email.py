stop = False
no_special = ['!', '#', '$', '%', '^', '&', '*',
              '(', ')', '+', '=', '[', ']', '{', '}', '\\', '|', ';', ':', "'", '"', ',', '<', '>', '/', '?']
yes_special = ['-', '_', '.']
special = ['!', '@', '#', '$', '%', '^', '&', '*',
           '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '\\', '|', ';', ':', "'", '"', ',', '<', '>', '/', '?']

while (stop == False):
    first = second = third = ""
    aro = spe1 = spe2 = spe3 = 0
    bolSpecial = stop = False
    email = input("Entrer votre Email: ")
    taille = len(email)
    if (email[0] == '@' or email[0] == '-' or email[0] == '_'):  # check first char
        print("no special characters in the beginning")
        continue
    j = 0
    for i in range(taille):  # check only one @
        if email[i] == '@':
            j += 1
    if j != 1:
        print("Entrer une seule @")
        continue

    for i in range(taille):  # create first
        if email[i] != '@':
            first += email[i]
        else:
            aro = i
            first += '@'
            break

    bolSpecial = False
    for i in range(len(first)):  # check special before @
        for j in range(len(no_special)):
            if first[i] == no_special[j]:
                bolSpecial = True
                break
    if bolSpecial == True:
        print("- _ . are the only special characters you can write")
        continue
    j = 0
    for i in range(aro, taille):  # check only one . after @
        if email[i] == '.':
            j += 1
    if j != 1:
        print("Enter only one . after @ ")
        continue
    second = ""
    bolSpecial = False
    for i in range(aro+1, taille):  # creat second
        if email[i] != '.':
            second += email[i]
        else:
            spe1 = i
            second += '.'
            break

    for i in range(len(second)):  # check special before @
        for j in range(len(no_special)):
            if second[i] == no_special[j]:
                bolSpecial = True
                break
    if bolSpecial == True:
        print("no special charcaters after @")
        continue
    bolSpecial = False
    third = ""
    for i in range(spe1+1, taille):  # creat third
        third += email[i]

    for i in range(spe1, taille):  # no special in third even .
        if email[i] == (special[j] or '.'):
            bolSpecial = True
            break
    if bolSpecial == True:
        print("no special charcaters after '.'")
        continue

    if (len(first) < 2 or len(second) < 2 or len(third) < 2):
        print("You should write a text before @ also before . and after it ")
        continue
    break

print("valid email ")
