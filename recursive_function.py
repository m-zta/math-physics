def f(x):
    if x == 0:
        return 1
    elif x > 0:
        return f(x - 1) + x
    else:
        print("x must be a non-negative integer")
        return None


def main():
    for i in range(1, 10):
        print(f"f({i}) = {f(i)}")


if __name__ == '__main__':
    main()
