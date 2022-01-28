############# Day 3 - Part 1 #############

f = open('D:/JavaScript/advent_1/day3.txt')
dat3 = f.readlines()
diagnose = list() # transform original binary data to integer numbers and store in this list 
gamma_list = list() # store binary gamma rate
epsilon_list = list() # store binary epsilon rate
for dat in dat3:
    bi_num = dat.strip()
    diagnose.append(bi_num)

bit = len(diagnose[0])
for i in range(0, bit):
    count_0 = 0   # count the number of 0 for each bit
    count_1 = 0   # count the number of 1 for each bit
    for bi in diagnose:
        if bi[i] == '0':
            count_0 += 1
        elif bi[i] == '1':
            count_1 += 1
    if count_0 > count_1:
        gamma_list.append(0) #append the most common bit in gamma list
        epsilon_list.append(1) #append the least common bit in epsilon list
    elif count_0 < count_1:
        gamma_list.append(1) #append the most common bit in gamma list
        epsilon_list.append(0) #append the least common bit in epsilon list

gamma = 0   
epsilon = 0
for i in range(0, bit):   
    gamma += gamma_list[-1] * 2**i   # calculate decimal gamma rate
    epsilon += epsilon_list[-1] * 2**i  # calculate decimal epsilon rate
    gamma_list.pop() 
    epsilon_list.pop()
power_consumption = gamma * epsilon  # calculate power consumption
print(f'The power consumption is {power_consumption}.')
