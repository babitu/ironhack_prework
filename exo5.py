# assign a variable to the list of temperatures
y = [33,66,65,0,59,60,62,64,70,76,80,81,80,83,90,79,61,53,50,49,53,48,45,39]

# 1. Calculate the minimum of the list and print the value using print()
print(min(y))

# 2. Calculate the maximum of the list and print the value using print()
print(max(y))

# 3. Items in the list that are greater than 70ºC and print the result
print([i for i in y if i>70])

# 4. Calculate the mean temperature throughout the day and print the result
mean_temperature = sum(y)/len(y)
print(mean_temperature)

# 5.1 Solve the fault in the sensor by estimating a value

# 5.2 Update of the estimated value at 03:00 on the list
y = [33,66,65,62,59,60,62,64,70,76,80,81,80,83,90,79,61,53,50,49,53,48,45,39]

# Bonus: convert the list of ºC to ºFarenheit
def conv(x):
    return(1.8*x+32)
Farenheit_y = list(map(lambda x: conv(x), y))

# Print True or False depending on whether you would change the cooling system or not
for i in range(len(y)-4):
    if y[i] > 70 and y[i+1] > 70 and y[i+2] >70 and y[i+3] > 70:
        result = 1
print (sum(y)/len(y))
if result or sum(i for i in y if i>80) or sum(y)/len(y) > 65:
    print ("True")
else:
    print ('False')

# 1. We want the hours (not the temperatures) whose temperature exceeds 70ºC
hours = []
for i in range(len(y)):
    if y[i]>70:
        hours.append(i)
print(hours)
# 2. Condition that those hours are more than 4 consecutive and consecutive,
# not simply the sum of the whole set. Is this condition met?
# 3. Average of each of the lists (ºC and ºF). How they relate?
# 4. Standard deviation of each of the lists. How they relate?
