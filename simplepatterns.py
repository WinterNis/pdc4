from collections import Counter

with open('data/yolo.txt', 'r') as file:
    result = {}
    for line in file:
        line = line.split(';')[1]
        line = line.split(',')[1::2]
        print(len(line))
        for current_p_size in range(2, int(len(line)/100)):
            l = [tuple(line[i:i+current_p_size]) for i in range(len(line)-current_p_size+1)]
            result.update(Counter(l))
            print(current_p_size)

    print(len(result.keys()))
