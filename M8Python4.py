def checkLeapYear(year):
    #Check if the year is evenly divisible by 4
    if (year % 4) == 0:
        #Check if the year is evenly divisible by 100
        if (year % 100) == 0:
            #Check if the year is evenly divisible by 400
            if (year % 400) == 0:
                #Print it is a leap year
                print("{0} is a leap year".format(year))
            #Else it is not a leap year
            else:
                print("{0} is not a leap year".format(year))
        #if the year is not divisible by 100 then Leap year
        else:
            print("{0} is a leap year".format(year))
    else:
        print("{0} is not a leap year".format(year))


checkLeapYear(2021)
checkLeapYear(2000)

