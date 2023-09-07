def leapcheck(year):
  if(year%400==0):
    print("the given year",year,"is leap year")
  elif(year%100==0):
    print("the given year",year,"is not a leap year")
  elif(year%4==0):
    print("the given year",year,"is leap year")
  else:
    print("the given year",year,"is not a leap year") 
year=int(input("enter the year"))
leapcheck(year)