#input for bill amount, convert string type to int
#input for tip amount, covert string type to int
#input for number of people, convert string type to int
#150 split between 5 people with 12% is (150/5) *1.12 with 2 decimals
#
#
#
bill = float(input("What is the bill amount ?"))

tip = int(input("What is the tip amount?"))

people = int(input("How many people are there?"))

tiptopercent = tip/100
totalbillwithtip = bill + tiptopercent
billperperson = totalbillwithtip / people

final = round(billperperson, 2)

print(f"Each person pays: {final}")