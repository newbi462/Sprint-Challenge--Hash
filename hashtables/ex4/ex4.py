def has_negatives(a):

    """
    YOUR CODE HERE
    """
    speed = {}
    result = []
    for x in a:
        key_neg = "neg" + str(x)
        key_pos = "neg" + str(x)

        if x < 0:
            try:
                hold_test = speed[key_neg]
            except KeyError:
                speed[key_neg] = True
        else:
            try:
                hold_test = speed[key_pos]
            except KeyError:
                speed[key_pos] = True

        try:
            if speed[key_pos] is True and speed[key_neg] is True:
                try:
                    if speed["result" + str(x)] is True:
                        pass
                except KeyError:
                    result.append(abs(x))
                    speed["result" + str(x)] = True
        except KeyError:
            pass

    print(speed)
    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
