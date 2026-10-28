
def reverse_array(array):

    for number in range(len(array)):

        start = 0
        end = len(array[number]) - 1

        while start < end:

            temporaryArray = array[number][start]
            array[number][start] = array[number][end]
            array[number][end] = temporaryArray

            start += 1
            end -= 1
    return array


array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

reverse_array(array)

for row in array:
    print(row)
