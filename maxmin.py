def minmax(l):
    min = l[0]
    max = l[0]

    for num in l[1:]:
        if num < min:
            min = num
        if num > max:
            max = num

    return [min, max]


l = [2, 4, 1, 0, 2, -1]
l = [20, 50, 12, 6, 14, 8]
l = [100, -100]
print(minmax(l))
