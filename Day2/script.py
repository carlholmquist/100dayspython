print("Welcome to the tip calculator")
total_bill = input("What was the total bill? $")
people_to_split = input("How many people tp split the bill?")
tip_percentage = input("What percentage tip would you like to give? 10, 12 or 15? ")

per_person_bill = float((float(total_bill)*((int(tip_percentage)/100)+1))/int(people_to_split))

print(f"Each person should pay ${round(per_person_bill,2)}")