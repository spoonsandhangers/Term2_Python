"""
Operator        Description
==              Equal to
!=              Not equal to
>               Greater than
<               Less than
>=              Greater than or equal to
<=              Less than or equal to
or              or
and             and
"""
# adjust these two variables to change the output
age = 18
birthday = False

if age > 18:
	print("You are already over 18")
elif age < 18:
	print("You are not 18 yet!")
elif age == 18 and birthday == True:
	print("It's your 18th birthday!")
else:
	print("You are 18 but it's not your birthday!")



