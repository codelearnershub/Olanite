# rotate matrix anti-clockwise r times


import array
def rotateMatrix(m: int, n: int, r: int, array: array):
    temp: int = array[0][0]
    dept: int = 0
    pos: int = 0
    while r != 0:
        while dept < m - 1:
            val = temp
            temp = array[dept + 1][pos]
            array[dept + 1][pos] = val
            dept += 1
        while pos < n - 1:
            val = temp
            temp = array[dept][pos + 1]
            array[dept][pos + 1] = val
            pos += 1
        while dept > 0:
            val = temp
            temp = array[dept - 1][pos]
            array[dept - 1][pos] = val
            dept -= 1
        while pos > 0:
            val = temp
            temp = array[dept][pos - 1]
            array[dept][pos - 1] = val
            pos -= 1
        rotateInnerMatrix(m=m - 1, n=n - 1, array=array)
        r -= 1


def rotateInnerMatrix(m: int, n: int, array: array):
    temp: int = array[1][1]
    dept: int = 1
    pos: int = 1
    while(True):
        while dept < m - 1:
            val = temp
            temp = array[dept + 1][pos]
            array[dept + 1][pos] = val
            dept += 1
        while pos < n - 1:
            val = temp
            temp = array[dept][pos + 1]
            array[dept][pos + 1] = val
            pos += 1
        while dept > 1:
            val = temp
            temp = array[dept - 1][pos]
            array[dept - 1][pos] = val
            dept -= 1
        while pos > 1:
            val = temp
            temp = array[dept][pos - 1]
            array[dept][pos - 1] = val
            pos -= 1
        break


_2Darray: array = [[1, 2, 3, 9],
                   [4, 5, 6, 4],
                   [7, 8, 9, 3],
                   [10, 11, 12, 2]]

rotateMatrix(4, 4, 1, _2Darray)

print(_2Darray)
