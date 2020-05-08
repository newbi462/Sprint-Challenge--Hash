def intersection(arrays):

    """
    YOUR CODE HERE
    """
    speed = {}
    result = []
    #for x in arrays:
        #for y in x:
    for x in arrays[0]:
        speed[x] = 1

    count = 1
    while count < len(arrays)-1:
        for y in arrays[count]:
            #print(count)
            try:
                hold_test = speed[y]
                speed[y] = hold_test + 1
            except KeyError:
                pass
        count += 1

    for z in arrays[len(arrays)-1]:
        #print(z)
        try:
            hold_test2 = speed[z]
            #print(f"len test:{len(arrays)}")
            if speed[z] + 1 == len(arrays):
                result.append(z)
        except KeyError:
            pass

    #print(speed)
    return result


if __name__ == "__main__":
    arrays = [
    [1, 2, 3, 4, 5],
    [12, 7, 2, 9, 1],
    [99, 2, 7, 1,]
    ]

    #arrays.append(list(range(1000000,2000000)) + [1,2,3])
    #arrays.append(list(range(2000000,3000000)) + [1,2,3])
    #arrays.append(list(range(3000000,4000000)) + [1,2,3])


    print(intersection(arrays))
