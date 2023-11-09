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


def ChangePass(pw):
    if len(pw) != 4:
        return -1
    return 0


def Transaction(money, changes, acc1, mn1, mn2, mn3, old, new):
    print("      ====================== YOUR LOGS ============================      ")
    if changes == 1:
        print("--------------------------------------------------------------------")
        print("==========You sent ", acc1,
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


shifre = modpss = []
shifre = ['23456655866678', '34566549305646', '35675948390231']  # 14 num
modpss = ['9784', '3456', '5656']
stop = stop2 = Exit = False
account = choice = accToSend = moneyToGrab = MoneyToAdd = MoneyToTake = OldPass = NewPass = 0
#          MENU
Money = 2000

while (stop == False and not Exit):
    print("===================================Log in=========================================")
    number = input("Enter your acc number: ")

    Valid = validNum(number)  # i
    if Valid >= 0:
        print("This Account exist now enter its password")
        index = Valid
    else:
        print("  =======================this Account doesn't try again=========================")
        continue
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
            continue
    while (stop == False and not Exit):
        # print(modpss)
        print("==================================MENU================================")
        print("======================================================================")
        print("---Money in the bank--------------------------------------------------")
        print("----------------------------------------------------------------------")
        print("----", Money, " DH----------------------------------------------------")
        print("----------------------------------------------------------------------")
        print("----------------------------------------------------------------------")
        print("---------CHOICES---------------------------------Enter this number----")
        print("-send money to an other account  ============>           1           -")
        print("-add some money to your bank account     ============>    2          -")
        print("-take money from your account  ============>              3          -")
        print("-EXIT THE ACCOUNT                   ============>         4          -")
        print("-CHANGE THE PASSWORD              ============>           5          -")
        Transaction(Money, choice, accToSend, moneyToGrab,
                    MoneyToAdd, MoneyToTake, OldPass, NewPass)
        while (stop2 == False and not Exit):
            choice = int(input("Your choice is: "))
            if choice == 1:
                while (stop2 == False):
                    num = input(
                        "Enter the account that you want to send money: ")
                    accToSend = Myaccount(num, account)
                    valid = validNum(num)
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
                    Result = Money - moneyToGrab
                    if Result >= 0:
                        Money = Result
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
                # stop == True
                # # stop2 == True
                Exit == True
                break
            elif choice == 2:
                MoneyToAdd = int(input("ENTER THE MONEY HERE ==========>:"))
                Result = Money + MoneyToAdd
                Money = Result
                print("MONEY ADDED SUCCESSFULLY")
                break
            elif choice == 3:
                while (stop2 == False):
                    MoneyToTake = int(
                        input("TYPE HOW MUCH CASH YOU WANT TO TAKE FROM YOUR ACCOUNT : "))
                    Result = Money - MoneyToTake
                    if Result >= 0:
                        print("HERE IS THE CASH =======> ", MoneyToTake)
                        Money = Result
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
