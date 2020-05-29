def square(x):
    return x*x


def cube(x):
    return x*x*x


def length(x):
    counter = 0
    for j in x:
        counter += 1
    return counter


def min(x, y):
    if x < y:
        return x
    elif x > y:
        return y
    else:
        return x


def max(x, y):
    if x < y:
        return y
    elif x > y:
        return x
    else:
        return x


def fact(x):
    prod = 1
    for i in x:
        prod = prod * i
    return prod


def main():
    print("This is the file with all accessible functions.")


if __name__ == "__main__":
    main()
