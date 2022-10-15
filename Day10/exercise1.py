# The List month_days contains the number of days in a month from January to December for a non-leap year. A leap year has 29 days in February.


from sqlalchemy import false


def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
          return True
     #   print("Leap year.")
      else:
        return False
      #  print("Not leap year.")
    else:
        return True
     # print("Leap year.")
  else:
    return False
   # print("Not leap year.")


def days_in_month(year,month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if is_leap(year) == True:
      month_days[1]=29
  return month_days[month-1]
   
  

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)







