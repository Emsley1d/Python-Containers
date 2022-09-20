# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

month=input("Please enter the month of the year (Jan - Dec):")
day=int(input("Please enter the day of the month:"))

if month in ('Jan', 'Feb'):
    print(month, day, "is in Winter")
elif month in ('Apr', 'May'):
    print(month, day, "is in Spring")
if month in ('Jul', 'Aug'):
    print(month, day, "is in Summer")
elif month in ('Oct', 'Nov'):
    print(month, day, "is in Autumn")

if month == 'Dec' and day >= 21:
    print(month, day, "is in Winter")
elif:
    print(month, day, "is in Autumn")
elif month == 'Mar' and day >= 19:
    print(month, day, "is in Winter")
else:
    print(month, day, "is in Spring")

if month == 'Jun' and day >= 21:
    print(month, day, "is in Summer")
else:
    print(month, day, "is in Spring")

if month == 'Sep' and day >= 22:
    print(month, day, "is in Autumn")
else:
    print(month, day, "is in Summer")








# if month in ('Dec', 'Jan', 'Feb'):
#     elif 'Dec' and day < 21 else 'Winter'
#     print(month, day, "is in Winter")

#     # elif day in ()
# elif month in (('Mar', 'Apr', 'May')):
#     print(month, day, "is in Spring")
# elif month in (('Jun', 'Jul', 'Aug')):
#     print(month, day, "is in Summer")
# elif month in (('Sep', 'Oct', 'Nov')):
#     print(month, day, "is in Autumn")



# if mo in ('Jan', 'Feb', 'Mar'):
#   season = 'Winter'
# elif mo in ('Apr', 'May', 'Jun'):
#   season = 'Spring'
# elif mo in ('Jul', 'Aug', 'Sep'):
#   season = 'Summer'
# else:
#   season = 'Fall'
# if mo == 'Mar' and day > 19:
#   season = 'Spring'
# elif mo == 'Jun' and day > 20:
#   season = 'Summer'
# elif mo == 'Sep' and day > 21:
#   season = 'Fall'
# elif mo == 'Dec' and day > 20:
#   season = 'Winter'
# print(f'{mo} {day} is in {season}')