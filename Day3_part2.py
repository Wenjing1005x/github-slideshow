############# Day 3 - Part 2 #############

f = open('D:/JavaScript/advent_1/day3.txt')
dat3 = f.readlines()
oxy_dict = dict()
co2_dict = dict()
for key in range(0, len(dat3)):
    oxy_dict[key] = dat3[key].strip()
    co2_dict[key] = dat3[key].strip()

bit_oxy = len(oxy_dict[0])
bit_co2 = len(co2_dict[0])

# Oxygen: only keep the most common value, if equal, keep 1
for i in range(0, bit_oxy):
    #print(f'i = {i}')
    count_0 = 0
    count_1 = 0
    for key in oxy_dict:
        if oxy_dict[key][i] == '1':
            count_1 += 1
        else:
            count_0 += 1
    #print(count_0,count_1)
    if count_0 > count_1:
        most = '0'
    else:
        most = '1'
    #print(f'most = {most}')
    delete_key = list()
    for key in oxy_dict:
        if oxy_dict[key][i] != most:
            delete_key.append(key)
    for de in delete_key:
        if len(oxy_dict) > 1:
            #print(f'delete {de}: {oxy_dict[de]}')
            oxy_dict.pop(de)
        else:
            break

# CO2: only keep the least common value, if equal, keep 0
for i in range(0, bit_co2):
    #print(f'i = {i}')
    count0 = 0
    count1 = 0
    for key in co2_dict:
        if co2_dict[key][i] == '1':
            count1 += 1
        else:
            count0 += 1
    #print(count0,count1)
    if count0 > count1:
        least = '1'
    else:
        least = '0'
    #print(f'least = {least}')
    delete_key = list()
    for key in co2_dict:
        if co2_dict[key][i] != least:
            delete_key.append(key)
    for de in delete_key:
        if len(co2_dict) > 1:
            #print(f'delete {de}: {co2_dict[de]}')
            co2_dict.pop(de)
        else:
            break

# calculate oxygen generator rating
for key in oxy_dict:
    oxy_bina = oxy_dict[key]
bit = len(oxy_bina)
oxy_str = oxy_bina
oxy = 0
for b in range(0, bit):
    oxy += 2**b * int(oxy_str[-1])
    oxy_str = oxy_str[:-1]

# calculate CO2 scrubber rating
for key in co2_dict:
    co2_bina = co2_dict[key]
bit_1 = len(co2_bina)
co2_str = co2_bina
co2 = 0
for b in range(0, bit_1):
    co2 += 2**b * int(co2_str[-1])
    co2_str = co2_str[:-1]

# calculate life support rating
life_support = oxy * co2
print(f'life support rating: {life_support}')
