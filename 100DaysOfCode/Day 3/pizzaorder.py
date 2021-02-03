print("welcome to python pizza deliveries")
size = input("what size pizza do you want? S, M, L")
add_pepperoni = input("Do you want pepperoni? Y or N")
extra_cheese = input("Do you want extra cheeese?")
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 17
elif size == "L":
    bill += 20

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
        bill += 1

print("Final bill:" + bill)