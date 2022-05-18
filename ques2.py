year=int(input("Enter a year : "))

if year%400==0:
    print("yes , leap year")
elif year%4==0 and year%100!=0:
    print("yes, leap year")
else:
    print("not a leap year")