#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):

    """
    YOUR CODE HERE
    """
    speed = {}
    route = []
    for x in tickets:
        #print(x.source)
        #print(f"{x.destination}\n")
        speed[x.source] = x.destination

    count = 0
    route.append(speed["NONE"])
    while count < length-1:
        route.append(speed[route[count]])
        count += 1
        print(route)




    return route
