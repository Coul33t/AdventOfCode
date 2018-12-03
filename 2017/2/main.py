import pdb

def checksum(matrix):
    cumsum = 0
    for row in matrix:
        cumsum += max(row) - min(row)

    return cumsum

def checksum2(matrix):
    cumsum = 0
    for row in matrix:
        tmp_lst = [[row[i] / row[j] for j in range(len(row)) if i != j and row[i] / row[j] % 1 == 0] for i in range(len(row))]
        cumsum += int([x for x in tmp_lst if any(x)][0][0])
    return cumsum


if __name__ == '__main__':
    with open('input.txt', 'r') as input_file:
        matrix = input_file.read()
        matrix = [[int(x) for x in splitted.split('\t')] for splitted in matrix.split('\n')]
        print(checksum(matrix))
        print(checksum2(matrix))
        