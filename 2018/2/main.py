import pdb

def checksum(data):
    twos = 0
    threes = 0

    two_found = False
    three_found = False

    for box in data:
        two_found = False
        three_found = False
        for letter in box:
            if not two_found and box.count(letter) == 2:
                twos += 1
                two_found = True
                
            if not three_found and box.count(letter) == 3:
                threes += 1
                three_found = True
    
    return twos * threes

def checksum2(data):
    for i, box in enumerate(data):
        current_box = list(box)
        for j in range(i, len(data)):
            if i != j:
                other_box = list(data[j])
                result = [abs(cb - ob) for cb, ob in zip([ord(x) for x in current_box], [ord(x) for x in other_box])]

                if sum(bool(x) for x in result) == 1:
                    return ('').join([x for i, x in enumerate(current_box) if current_box[i] == other_box[i]])


if __name__ == '__main__':
    with open('input.txt', 'r') as input_file:
        data = input_file.read().split('\n')
        print(checksum(data))
        print(checksum2(data))

    

