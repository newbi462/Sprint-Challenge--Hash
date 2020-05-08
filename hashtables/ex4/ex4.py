def has_negatives(a):

    """
    YOUR CODE HERE
    """
    speed = {}
    result = []
    for x in a:
        try:
            hold_test = speed["result" + str(abs(x))]
            if hold_test[0] == x:
                pass
            else:
                if len(speed["result" + str(abs(x))]) < 2:
                    speed["result" + str(abs(x))].append(x)

            if len(speed["result" + str(abs(x))]) == 2:
                result.append(abs(x))

        except KeyError:
            speed["result" + str(abs(x))] = []
            speed["result" + str(abs(x))].append(x)



    #print(speed)
    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
