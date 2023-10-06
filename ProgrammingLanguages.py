#SCT211-0046/2022 Britney Knight

#QUSTION 3

identity= input("Enter your name :")
print("hello ",identity)
year1=int(2023)
year2=int(input("enter your year of birth :"))
age1=year1-year2
age2=age1*12
age3=age1*365

print(identity , "is" ,age1, "years old,", age2, "months old and " ,age3, "days old")


#QUESTION TWO

bill=float(input("Enter total bill :"))
tip=int(input("Enter tip as 10,12, or 15 , percentage  of the total bill :"))
people=int(input("Number of people splitting the bill :"))
averagebill=(bill+((tip/100)*bill))/people
print("each person should pay " ,averagebill)


#QUESTION THREE
weight=float(input("Enter your weight in kilograms: "))
height=float(input("Enter your height in metres: "))
BMI=weight/(height**2)
print("your body mass index is " ,BMI)
if BMI<18.5:
    print("You are underweight")
elif BMI>24.9:
    print("You are overweight")
else:
    print("you are normalweight")    


#QUESTION FOUR
year1=int(input("enter year: "))
if (year1%400==0) or (year1%4==0 and year1%100!=0) :
    print(year1 , " is a leap year ." )
else :
    print(year1 ," is not a leap year. ")    

