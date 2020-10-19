# ask the user to enter a score between 0 and 100
# cast it to an integer

score = int(input("Enter a score between 0 and 100: "))

# first tests if the score is more than 100
# then progressively tests the other grades.
if score >100:
	print("That score is more than the maximum score possible.")
elif score >= 90:
	print("You've got an A*")
elif score >= 80:
	print("You've got an A")
elif score >= 70:
	print("you've got a B")
elif score >= 60:
	print("you've got a C")
elif score >= 50:
	print("you've got a D")
elif score >= 40:
	print("you've got an E'")
else:
	print("You've got a U")

# another way to do it using just greater than

if score > 100:
	print("That score is more than the maximum score possible.")
elif score > 89:
	print("You've got an A*")
elif score > 79:
	print("You've got an A")
elif score > 69:
	print("you've got a B")
elif score > 59:
	print("you've got a C")
elif score > 49:
	print("you've got a D")
elif score > 39:
	print("you've got an E'")
else:
	print("You've got a U")


# using nested if statements:

if score <= 101:
    if score <= 89:
        if score <= 79:
            if score <= 69:
                if score <= 59:
                    if score <= 49:
                        if score <= 39:
                            print("You got a U")
                        else:
                            print("You got a E")

                    else:
                        print("You got a D")

                else:
                    print("You got a C")

            else:
                print("You got a B")
        else:
            print("You got a A")
    else:
        print("You got a A*")
else:
    print("You've entered a value higher than the maximum score.")
