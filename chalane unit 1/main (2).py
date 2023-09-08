#leap year

"""
year%4==0&
year%100 !=0/
year%400==0

"""
def isleapYear(year):
  if(year  %4==0and year  %100 !=0)or year%400==0:
    return True
  else:
    return False

year=2023

if isleapYear(year):
  print('{} is a leap year.'.format(year))
else:
  print('{} isnnot a  leap year.'.format(year))