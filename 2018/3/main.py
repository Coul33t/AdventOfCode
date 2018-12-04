import pdb
import re

def rect_overlaps(rect1, rect2):
    # 1 = top left x
    # 2 = top left y
    # 3 = width
    # 4 = height
    # top_right.x = rect[1] + rect[3]
    # bottom_left.x = rect[1]
    # top_right.y = rect[2]
    # bottom_left.y = rect[2] + rect[4]
    return not (rect1[1] + rect1[3] < rect2[1] or 
                rect1[1] > rect2[1] + rect2[3] or 
                rect1[2] > rect2[2] + rect2[4] or 
                rect1[2] + rect1[4] < rect2[2])

def overlapping2(data):
    overlaps_matrix = [[0 for y in range(len(data))] for x in range(len(data))]

    for i in range(len(data)):
        for j in range(len(data)):
            if i != j and rect_overlaps(data[i], data[j]):   
                overlaps_matrix[i][j] += 1

        if sum(overlaps_matrix[i]) == 0:
            return data[i][0]
           

def overlapping(data):
    max_width = max([x[1] + x[3] for x in data])
    max_height = max([x[2] + x[4] for x in data])
    
    canvas = [[0 for y in range(max_width)] for x in range(max_height)]

    for claim in data:
        for x in range(claim[2], claim[2] + claim[4]):
            for y in range(claim[1], claim[1] + claim[3]):
                canvas[x][y] += 1

    return sum(sum(i > 1 for i in row) for row in canvas)

if __name__ == '__main__':
    with open ('input.txt', 'r') as input_file:
        data = input_file.read().split('\n')
        for i in range(len(data)):
            data[i] = [int(x) for x in re.findall(r'(\d+)', data[i])]

        print(overlapping(data))
        print(overlapping2(data))
    