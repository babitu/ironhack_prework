# Assign problem data to variables with representative names
# well height, daily advance, night retreat, accumulated distance
well_height = 125
daily_advance = 30
night_retreat = 20
accumulated_distance = 0

# Assign 0 to the variable that represents the solution
days = 0

# Write the code that solves the problem
while accumulated_distance < well_height:
    if days > 0:
        accumulated_distance = accumulated_distance - night_retreat
    accumulated_distance = accumulated_distance + daily_advance
    days+=1

# Print the result with print('Days =', days)
print('Days= ', days)
