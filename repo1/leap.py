#A leap year program in Python takes a year as input and checks if the year is a leap year or not


#The following equations must be true for the leap year:

#The year must divide evenly by 400. year/400==0
#The year should divide evenly by 4, but not by 100. year/4 and year/100 != 0

year = 0
leap = False
year = int(input("enter the year : "))
if(year%400==0):
    leap = True
else:
    if(year%4==0 and year%100!=0):
        leap = True
    else:
        leap = False

if(leap == True):
    print("yes")
else:
    print("no")