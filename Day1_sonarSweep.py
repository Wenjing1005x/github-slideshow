############# Day 1 - Part 1 #############
f = open('D:/JavaScript/advent_1/day1_part1.txt')
data = f.readlines()
depth = list()
for item in data:
    dat_num = int(item)
    depth.append(dat_num)
increase = 0
nochange = 0
decrease = 0
for i in range(1,len(depth)):
    if depth[i-1] < depth[i]:
        increase += 1
    elif depth[i-1] > depth[i]:
        decrease += 1
    else:
        nochange += 1
print(f'increase: {increase}\ndecrease: {decrease}\nno change: {nochange}')

############# Day 1 - Part 2 #############
window = [None] * 3
create_sum = dict()
increase2 = 0
decrease2 = 0
nochange2 = 0
win_inital = [depth[0] ,depth[1], depth[2]]
create_sum['WINDOW0'] = sum(win_inital)
for i in range(1,len(depth)-2):
    window[0] = depth[i]
    window[1] = depth[i+1]
    window[2] = depth[i+2]
    key = f'WINDOW{i}'
    former_key = f'WINDOW{i-1}'
    val = sum(window)
    create_sum[key] = val
    if val > create_sum[former_key]:
        increase2 += 1
    elif val < create_sum[former_key]:
        decrease2 += 1
    else:
        nochange2 += 1
print(f'increase2: {increase2}\ndecrease2: {decrease2}\nno change2: {nochange2}')
#print(create_sum)

        


