import datetime
current_year = datetime.datetime.now().year
name = input ("Enter your name:")
age = int(input("Enter your age:"))
age_turn_100 = current_year + (100 - age)
output = f"Hello {name}, you will turn 100 years old in the year {age_turn_100}."
print (output)