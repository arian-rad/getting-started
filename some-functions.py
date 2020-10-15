count = []


def print_moves(start, end):
    if start == 1:
        s = "A"
    if start == 2:
        s = "B"
    if start == 3:
        s = "C"
    if end == 1:
        e = "A"
    if end == 2:
        e = "B"
    if end == 3:
        e = "C"
    print(s, "->", e)
    count.append(1)


def hanoi(n, start, end):
    if n == 1:
        print_moves(start, end)
    else:
        other = 6 - (start + end)
        hanoi(n - 1, start, other)
        print_moves(start, end)
        hanoi(n - 1, other, end)


def factorial(n):
    if n == 1 or n == 0:
        return 1
    elif n < 0:
        raise ValueError("invalid input! n must be a non negative number")
    else:
        return n * factorial(n - 1)



def linear_recursive(array, item, length):
    if array[length] == item:
        return "found"
    else:
        if length - 1 >= 0:
            return linear_recursive(array, item, length - 1)
        return "not found"

