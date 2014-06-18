

"""Problem from http://www.problemotd.com/problem/matrix-rotation/"""

def rotate_clockwise_90(matrix):
    # Rotation by -90 is rotation clockwise 90deg.
    # We implement this as a transpose followed by a reversal of each row
    output = [list(r) for r in zip(*matrix)]

    for r in output:
        r.reverse()
    return output

def rotate(matrix, angle):
    if angle == -90 or angle == 270:
        return rotate_clockwise_90(matrix)
    elif angle == 90:
        _tmp = rotate_clockwise_90(matrix)
        _tmp = rotate_clockwise_90(_tmp)
        _tmp = rotate_clockwise_90(_tmp)
        return _tmp
    elif angle == 180:
        _tmp = rotate_clockwise_90(matrix)
        _tmp = rotate_clockwise_90(_tmp)
        return _tmp
    elif angle == 0:
        return matrix
        

def main():
    matrix = [[1,2,3,4,5],
              [6,7,8,9,10],
              [11,12,13,14,15],
              [16,17,18,19,20],
              [21,22,23,24,25]]
    print "input:"
    print ",\n".join([str(r) for r in matrix])    
    print "\nrotate_clockwise_90:"
    output = rotate_clockwise_90(matrix)
    print ",\n".join([str(r) for r in output])
    print "\nrotate_counter-clockwise_90:"
    print ",\n".join([str(r) for r in rotate(matrix, 90)])


if __name__ == '__main__':
    main()
