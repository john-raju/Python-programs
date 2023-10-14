a=int(input("enter a year"));
if(a%4==0 and a%100!=0):
    print("leap year")
elif(a%400==0):
    print("leap year")
else:
    print("not leap")
