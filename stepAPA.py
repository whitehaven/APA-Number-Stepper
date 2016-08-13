def step_fold(data):
    if len(data) < 2:
        result = data
        return result

    pairs = []

    """
    does data[n] + 1== data[n+1]?
        if so, extend the range of the pair to data n+1 and look at the next
        if no, save te range, start a new one,

    then, compare numbers as char to find places to move
    (101, 110)
    1 == 1
    0 != 1
    1

    print first number
    101-
    at unequal point onward, print chars from second number
    10

    result = 101-10

    """

    result = []
    return result

if __name__ == "__main__":
    data = [1, 0]
    stepping_data = step_fold(data)
    print("data = ", data)
    print("stepping = ", stepping_data)
