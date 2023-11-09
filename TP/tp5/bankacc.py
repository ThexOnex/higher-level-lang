def validNum(number):  # validating the account
    for i in range(len(shifre)):
        if number == shifre[i]:
            return i
    return -1


def validPss(number, Valid):  # validating the password of that account
    for i in range(len(modpss)):
        if number == modpss[Valid]:
            return 0
    return -1


def Myaccount(number, acc):  # is the account that we'll money to different that our account
    if acc == number:
        return -1
    return 0


def ChangePass(pw):  # VALIDATING PASSWORD
    if len(pw) != 4:
        return -1
    return 0


def Transaction(money, changes, mn1, mn2, mn3, old, new, acc2):
    print("      ====================== YOUR LOGS ============================      ")
    if changes == 1:
        print("--------------------------------------------------------------------")
        print("==========You sent ", acc2,
              " This Amount of Money :", mn1, " DH ===========")
        print("----------------------------------------------------------------------")
        print("===         Money Left In Your account : ",
              money, " DH           ===")
        print("--------------------------------------------------------------------------")
    elif changes == 2:
        print("--------------------------------------------------------------------")
        print("===========You added this amount of money to you ACCOUNT: ",
              mn2, " DH =====")
        print(
            "------------------------------------------------------------------------------")
        print("========== Money that you have at your bank acount Right Now",
              money, " DH ==========")
        print("---------------------------------------------------------------------------------")
    elif changes == 3:
        print("--------------------------------------------------------------------")
        print("=== Amount of cash that you took from your ACCOUNT : ", mn3, " DH ====")
        print("--------------------------------------------------------------------")
        print("========== Money that you have at your bank acount Right Now",
              money, " DH ==========")
        print("--------------------------------------------------------------------")
    elif changes == 5:
        print("--------------------------------------------------------------------")
        print("===YOU CHANGED YOUR PASSWORD FROM ", old, " To ", new)
# ADMIN


def searchNum(num):
    for i in range(len(shifre)):
        if shifre[i] == num:
            return i
    return -1


def founAcc(num, index):
    print("FULL NAME                                  ", fullNames[index])
    print()
    print("--------------------------------------------------------------------")
    print("--------------------------------------------------------------------")
    print()
    print("ACOUNT NUMBER                                ", num)
    print("CASH IN DH                                   ",
          Money[index], "dh   ")
    print()
    print("--------------------------------------------------------------------")
    print("--------------------------------------------------------------------")


def validNumCreate(num):
    if len(num) != 14:
        return -1
    return 0


def AddAccount(addmoney, number, name, pw):
    Money.append(addmoney)
    shifre.append(number)
    fullNames.append(name)
    modpss.append(pw)


def DeleteAcc(index):
    del shifre[index]
    del Money[index]
    del modpss[index]
    del fullNames[index]


shifre = modpss = fullNames = []
fullNames = ['SALAH EDDIN', 'SARA CHAKIR', 'LAILA LALAOUI']
shifre = ['23456655866678', '34566549305646', '35675948390231']  # 14 num
modpss = ['9784', '3456', '5656']
Money = [2000, 1200, 12030]
stop = stop2 = False
account = choice = accToSend = moneyToGrab = MoneyToAdd = MoneyToTake = OldPass = index2 = NewPass = 0

while (stop == False):  # ADMIN
    print("===================================Log in=========================================")
    print("=============USER ACCOUNT ========================= ADMIN ======================")
    print("If you want to Enter ADMIN MODE Enter 'admin' and for logining to Your ACCOUNT 'user'")
    while (not stop2):
        admin = input("========>   ")
        if admin == 'admin':
            adminpss = '2222'
            while (not stop):
                isadminpss = input("ADMIN PASSWORD : ")
                if adminpss != isadminpss:
                    print(" ⛔WRONG PASSWORD⛔")
                    print("try again please")
                    continue
                break
            break
        elif admin == 'user':
            break
        else:
            print("WRONG Try again")
    if admin == 'admin':
        break
    while (not stop2):
        number = input("Enter your acc number: ")
        Valid = validNum(number)  # i
        if Valid >= 0:
            print("This Account exist now enter its password")
            index = Valid
            break
        else:
            print(
                "  =======================this Account doesn't try again=========================")
    while (stop2 == False):
        mp = input("Password: ")
        Passed = validPss(mp, Valid)
        if Passed == 0:
            print(
                "===========================WELCOME=======================================")
            account = number
            PassWrd = mp
            break
        else:
            print(
                "  =======================this Password is wrong=========================")
    while (stop == False):
        print("==================================MENU================================")
        print("======================================================================")
        print("---Money in the bank--------------------------------------------------")
        print("----------------------------------------------------------------------")
        print(
            "----", Money[index], " DH----------------------------------------------------")
        print("----------------------------------------------------------------------")
        print("----------------------------------------------------------------------")
        print("---------CHOICES---------------------------------Enter this number----")
        print("-send money to an other account  ============>           1           -")
        print("-add some money to your bank account     ============>    2          -")
        print("-take money from your account  ============>              3          -")
        print("-EXIT THE ACCOUNT                   ============>         4          -")
        print("-CHANGE THE PASSWORD              ============>           5          -")
        Transaction(Money[index], choice, moneyToGrab,
                    MoneyToAdd, MoneyToTake, OldPass, NewPass, shifre[index2])
        while (stop2 == False):
            choice = int(input("Your choice is: "))
            if choice == 1:
                while (stop2 == False):
                    num = input(
                        "Enter the account that you want to send money: ")
                    accToSend = Myaccount(num, account)
                    valid = validNum(num)
                    index2 = Valid
                    if valid >= 0 and accToSend == 0:
                        print(
                            "========                Acount found               ===========")
                        break
                    elif accToSend != 0 or valid == -1:
                        print(
                            "========                Acount NON found            ===========")
                        print(
                            "=====================PLEASE TRY AGAIN==========================")
                        if accToSend != 0:
                            print("you might have entered the same account number")
                        continue
                while (stop2 == False):
                    moneyToGrab = int(
                        input("Enter How Much You Want to send this user: "))
                    Result = Money[index] - moneyToGrab
                    if Result >= 0:
                        Money[index] = Result
                        Money[index2] += moneyToGrab
                        print(
                            "=============     MONEY SENT SUCCESSFULY      ============")
                        break
                    elif Result < 0:
                        print(
                            "The Amount Of Money That You Have Right Now is not enought")
                        print(
                            "===========           PLEASE TRY AGAIN           ==============")
                        continue
                break
            elif choice == 4:
                break
            elif choice == 2:
                MoneyToAdd = int(input("ENTER THE MONEY HERE ==========>:"))
                Result = Money[index] + MoneyToAdd
                Money[index] = Result
                print("MONEY ADDED SUCCESSFULLY")
                break
            elif choice == 3:
                while (stop2 == False):
                    MoneyToTake = int(
                        input("TYPE HOW MUCH CASH YOU WANT TO TAKE FROM YOUR ACCOUNT : "))
                    Result = Money[index] - MoneyToTake
                    if Result >= 0:
                        print("HERE IS THE CASH =======> ", MoneyToTake)
                        Money[index] = Result
                        break
                    else:
                        print(
                            "You don't have enough money in your bank account at the moment please try again")
                        continue
                break
            elif choice == 5:
                while (not stop2):
                    IsPassWrd = input("Enter Your Password ===>  : ")
                    if IsPassWrd == PassWrd:
                        while (not stop2):
                            NewPass = input("Enter your new password")
                            r = ChangePass(NewPass)
                            if r == 0:
                                OldPass = PassWrd
                                PassWrd = NewPass
                                modpss[index] = PassWrd
                                print("PASSWORD CHANGED SUCCESSFULLY")
                                break
                            else:
                                print(
                                    "Your Password should have 4 digits =try again=")
                        break
                    else:
                        print("This is not your current password try again")
                        continue
                break
            else:
                print("Enter only one of these numbers: 1, 2 and 3")
                continue
        if choice == 4:
            break
    if choice == 4:
        break
while (not stop and choice != 4):
    print(" ----------------------------------------------------------------------------------")
    print("================================ HELLO ADMIN =======================================")
    print("       ⌕______________________________________________________________  search      ")
    print("              DO YOU WANT TO SEARCH FOR AN ACCOUNT ?           TYPE        1  ")
    print("                    TO CREAT AN ACCOUNT                        TYPE        2  ")
    print("                    TO DELETE AN ACCOUNT                       TYPE        3  ")
    print("                    TO EXIT                                    TYPE        4")
    print("                    TO ADD MONEY TO AN ACCOUNT                 TYPE        5  ")
    print("                    TO CHANGE INFORMATIONS OF AN ACCOUNT       TYPE        6")
    choice = int(input("TYPE YOUR CHOICE => "))
    if choice == 1:
        print("Enter the account you want to search for")
        number = input("⌕_________________")
        print("search phase started")
        print("---------------------------searching %0")
        print("---------------------------searching %10")
        print("---------------------------searching %20")
        isFound = searchNum(number)
        print("---------------------------searching %50")
        print("---------------------------searching %80")
        print("---------------------------searching %100")
        print("SEARCH COMPLETED")
        if isFound == -1:
            print("THIS ACCOUNT DOESN'T EXIST ", number)
        else:
            print("=============✅  ACOUNT FOUND ✅===================")
            founAcc(number, isFound)
        continue
    elif choice == 2:
        print("------------------------ CREATE AN ACCOUNT --------------------")
        print("---------------------------------------------------------------")
        while (not stop):
            number = input("ACCOUNT NUMBER =======> ")
            isExist = validNum(number)
            validnum = validNumCreate(number)
            if isExist != -1:
                print("This account already exist ", number)
                print("          PLEASE TRY AGAIN")
                continue
            if validnum == -1:
                print("YOU SHOULD WRITE A NUMBER THAT GOT 14 DIGITS EXACTLY")
                print("          PLEASE TRY AGAIN")
                continue
            print("------------------------------------------------------------------------------------------------")
            name = input("FULL NAME =======> ")
            print("------------------------------------------------------------------------------------------------")
            pw = input("PASSWORD =======> ")
            R = ChangePass(pw)
            if R == -1:
                print("Pass word non valid please write 4 digit in your password")
                continue
            print(
                "---------------------------------------------------------------------------------------------")
            addMoney = int(
                input("Enter the cash you want to add to this account =======> "))

            print(
                "============================✅ACCOUNT CREATED SUCCESSFULY✅=========================")
            AddAccount(addMoney, number, name, pw)
            break
        continue
    elif choice == 3:
        print("========================== REMOVING ACCOUNT ===========================")
        while (not stop):
            number = input("ACCOUNT =======> ")
            isExist = validNum(number)
            if isExist == -1:
                print("                 ⛔ THIS ACCOUNT DOESN'T EXIST ⛔            ")
                continue
            DeleteAcc(isExist)
            print(
                "=====================      ✅ ACCOUNT DELETED SUCCESSFULLY ✅   ================================")
            break
        continue
    elif choice == 4:
        break
    elif choice == 5:
        print(" =============================== SENDING MONEY TO AN ACCOUNT =========================")
        while (not stop):
            number = input("ACCOUNT =======> ")
            isExist = validNum(number)
            if isExist == -1:
                print("                 ⛔ THIS ACCOUNT DOESN'T EXIST ⛔            ")
                continue
            print(" MONEY ON THE BANK ACCOUNT NOW ", Money[isExist])
            MoneyToAdd = int(input("MONEY TO SEND =======> "))
            Money[isExist] += MoneyToAdd
            print(
                "=====================      ✅ MONEY SENT SUCCESSFULLY ✅   ================================")
            print(" MONEY ON THE BANK ACCOUNT ", Money[isExist])
            continue
    elif choice == 6:
        print("========================= CHANGING ACCOUNT INFOS ==========================")
        while (not stop):
            number = input("ACCOUNT =======> ")
            isExist = validNum(number)
            if isExist == -1:
                print("                 ⛔ THIS ACCOUNT DOESN'T EXIST ⛔            ")
                continue
            print("-------------------------------------------------------------------")
            print("  to change its number --------------------------------1")
            print("  to change its names  --------------------------------2")
            print("  to change its password ------------------------------3")
            while (not stop):
                choiceAD = int(input("YOUR CHOICE IS : "))
                if choiceAD == 1:
                    num = input("NEW ACCOUNT NUMBER =======> ")
                    isval = validNumCreate(num)
                    if isval == -1:
                        print("⛔ Non valid number account try again ")
                        continue
                    shifre[isExist] = num
                    print("                   ✅NUMBER CHANGED SUCCESSFULLY✅")
                    break
                elif choiceAD == 2:
                    name = input("NEW FULL NAME ======> ")
                    fullNames[isExist] = name
                    print("                 ✅NAME CHANGES SUCCESSFULLY✅")
                    break
                elif choiceAD == 3:
                    while (not stop):
                        Pass = input("ENTER ACCOUNT PASSWORD : ")
                        if Pass != modpss[isExist]:
                            print("⛔ WRONG PASSWORD")
                            continue
                        while (not stop):
                            NewPass = input("NEW PASSWORD =======> ")
                            r = ChangePass(NewPass)
                            if r == -1:
                                print("⛔TRY AGAIN | PASSWORD SHOULD BE 4 DIGITS")
                                continue
                            break
                        modpss[isExist] = NewPass
                        print("               ✅PASSWORD CHANGED SUCCESSFULY✅")
                        break
                    break
                else:
                    print("type 1,2 or 3")
            break

    else:
        print("TYPE either one of these numbers : 1,2,3,4 and 5")
        continue
