height = float(input(" enter your height"))
weight = float(input("enter your weight"))

bmi = round(weight /(height ** 2))


if bmi< 18.5:
    print("your bmi is" + bmi + "and you are underweight")
elif bmi < 25:
    print("your bmi is normal weight ")
elif bmi < 30:
    print(" your bmu is overweight")
elif bmi < 35:
    print(" your bmi is obses")
else:
    print("you are clinically obese")