# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature.

# Prints whether it’s cold, warm, or hot using comparison operators.

# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”

# Starter Code:


temperature = int(input("Put your temperature (0-100): "))
if 85<= temperature <= 100:
    print("That is hot")
elif 50 <= temperature < 85:
    print("This is warm")
elif  -10 < temperature < 50:
    print("It is cold")
else:
    print("Extreme temperature warning") 