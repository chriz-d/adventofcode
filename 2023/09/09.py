with open("input.txt") as f:
    lines = f.read().split("\n")

sum_num = 0
master_list = []
for line in lines:
    numbers = [int(x) for x in line.split(" ")]
    sequence_list = [numbers]
    master_list.append(sequence_list)
    while not all([x == 0 for x in sequence_list[-1]]):
        new_list = []
        lowest_list = sequence_list[-1]
        for i in range(0, len(lowest_list) - 1):
            new_list.append(lowest_list[i+1] - lowest_list[i])
        sequence_list.append(new_list)
    sequence_list[-1].append(0)
    for i in range(len(sequence_list)-1, 0, -1):
        sequence_list[i-1].append(sequence_list[i][-1] + sequence_list[i-1][-1])
    sum_num += sequence_list[0][-1]
    
print(sum_num)

sum_num = 0
for sequence_list in master_list:
    sequence_list[-1].insert(0, 0)
    for i in range(len(sequence_list)-1, 0, -1):
        sequence_list[i-1].insert(0, sequence_list[i-1][0] - sequence_list[i][0])
    sum_num += sequence_list[0][0]
    
print(sum_num)