#data types
#strings
#int
#float
#boolean

#print("Hello" [0]) gives the first character
#type gives the datatype
#print(type(var))
#type casting is  when you have var = 9 but to change it to a string do new_var = (str(var))
#a = float(123) print(type(a))
#print(str(70)+str(100)) will give 70100


#challenge
two_digit_number = input("type a two digit number here: ")
first_digit = two_digit_number[0] #current datatype is a string so convert to string
second_digit = two_digit_number[1] #current datatype is a string so convert to string
result = int(first_digit)+int(second_digit)

print(result)

#mathamatical operations
#2**3 is exponenet

#bmi calculator
weight = input("enter your weight ")
height = input("enter you height")


bmi= int(weight)/float(height)*2
print(bmi)
#print bmi as an int
bmi_int = int(bmi)
print(bmi_int)

# number precision
print(round(2.66666666666666666666,2))
print(8//3) #floor divison
score = 0
height = 1.8
isWinning = True
#f-string
#print(f"you score is {score}, your height is {height}, you are winning is {isWinning}")


age = input("What is your current age?")
age_int = int(age)
years = 90 - age_int
days = years*365
weeks=years*52
months=years*12

#message =f"you have {days}, {weeks}weeks, {months}months, {years} years remaining "
#print(message)

print(6+4/2-(1*2))