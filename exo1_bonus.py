# Assign problem data to variables with representative names
# well height, daily advance, night retreat, accumulated distance
well_height = 125
advance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
night_retreat = 20
accumulated_distance = 0

# Assign 0 to the variable that represents the solution
days = 0

# Write the code that solves the problem
for daily_advance in advance_cm:
    if days > 0:
        accumulated_distance -= night_retreat
    accumulated_distance += daily_advance
    days += 1
    if accumulated_distance >= well_height:
        break

# Print the result with print('Days =', days)
print('Days=', days)

# What is its maximum displacement in a day? And its minimum?
maximum_displacement = max(advance_cm)-night_retreat
minimum_displacement = min(advance_cm)-night_retreat

# What is its average progress?
average_progress = well_height/days

# What is the standard deviation of its displacement during the day?
displacement_daily = list(map(lambda x: x-night_retreat, advance_cm[:days]))
import statistics
statistics.stdev(displacement_daily)
