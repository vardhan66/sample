year = int(input("Enter the Year: "))
if (year%400 == 0) or (year%4==0 and year%100!=0):
  print("Leap Year")
else:
  print("Not a Leap Year")