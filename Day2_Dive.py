############# Day 2 - Part 1 #############
print('---- Part 1 ----')
from fnmatch import fnmatchcase as match
f2 = open('D:/JavaScript/advent_1/day2_part2.txt')
dat2 = f2.readlines()

# extract polit directions (forward / down / up)


# create variables to calculate the distance in each direction
dist_horizontal = 0
dist_vertical = 0
for dir in dat2:
    dist = int(dir[-2])
    if match(dir, 'down*'):
        dist_vertical += dist  #down X increases the depth by X units
    if match(dir, 'up*'):
        dist_vertical -= dist  #up X decreases the depth by X units
    if match(dir, 'forward*'):
        dist_horizontal += dist  #forward X increases the horizontal position by X units

multi = dist_horizontal * dist_vertical
print(f'multiply horizontal position by depth: {multi} ')



############# Day 2 - Part 2 #############
print('---- Part 2 ----')
aim = 0
hor = 0
dep = 0
for row in dat2:
    X = int(row[-2])
    if match(row, 'down*'):  
        aim += X   #down X increases your aim by X units
    if match(row, 'up*'):
        aim -= X   #up X decreases your aim by X units
    if match(row, 'forward*'):
        hor += X      #forward X increases the horizontal position by X units
        dep += aim*X  #forward X increases your depth by your aim multiplied by X
final_multi = hor * dep
print(f'multiply final horizontal position by final depth: {final_multi}')





