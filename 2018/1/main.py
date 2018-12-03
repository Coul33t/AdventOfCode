import pdb

with open('input.txt', 'r') as of:
    
    values = of.read().split('\n')
    for i in range(len(values)):
        values[i] = int(values[i])

    all_sums = set()
    new_sum = 0
    i = 0

    while True:
        new_sum = new_sum + values[i]
        
        if new_sum in all_sums:
            print(new_sum)
            break
        
        all_sums.add(new_sum)
        
        i += 1

        if i == len(values):
            i = 0
            
