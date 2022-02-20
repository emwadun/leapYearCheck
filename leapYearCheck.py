'''
Three criteria must be taken into account to identify leap years:
i -> The year must be evenly divisible by 4;
ii-> If the year can also be evenly divided by 100, it is not a leap year;
unless...
iii-> The year is also evenly divisible by 400. Then it is a leap year.

The complete list of leap years in the first half of the 21st century is therefore:
2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, and 2048.
'''
year = int(input("Enter the year to check if it is a leap year or not: "))

def leapYearCheck():
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"Year {year} is a leap year.")
            else:
                print(f"Year {year} is NOT a leap year.")
        else:
            print(f"Year {year} is a leap year.")         
    else:
        print(f"Year {year} is NOT a leap year.")
        

leapYearCheck()     

