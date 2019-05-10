from math import sqrt

# Variables
points = [(4, 5), (-0, 2), (4, 7), (1, -3), (3, -2), (4, 5),
          (3, 2), (5, 7), (-5, 7), (2, 2), (-4, 5), (0, -2),
          (-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2),
          (5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]

# 1. Robin Hood is famous for hitting an arrow with another arrow. Did you get it?
results = {i: points.count(i) for i in points}
print (results)

# 2. Calculate how many arrows have fallen in each quadrant.
quandrant1 = 0
quandrant2 = 0
quandrant3 = 0
quandrant4 = 0

for i in points:
    if (i[0]>0 and i[1]>0):
        quandrant1 += 1
    if (i[0]>0 and i[1]<0):
        quandrant4 += 1
    if (i[0]<0 and i[1]>0):
        quandrant2 += 3
    if (i[0]<0 and i[1]<0):
        quandrant3 += 1
print(quandrant1,quandrant2,quandrant3,quandrant4)

# 3. Find the point closest to the center. Calculate its distance to the center
# Defining a function that calculates the distance to the center can help.
def distance_center(x):
    return(sqrt(x[0]**2 + x[1]**2))
distance = list(map(lambda x: distance_center(x), points))
min_distance = min(distance)
point_closest = points[distance.index(min_distance)]
print(point_closest)

# 4. If the target has a radius of 9, calculate the number of arrows that
# must be picked up in the forest.
sum(1 for i in distance if i>9)
