def is_even(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    return n % 2 == 0


if __name__ == "__main__":
    test_values = [0, 1, 2, 15, 20, -4, 3.5, "4"]
    for val in test_values:
        print(f"{val} is even? {is_even(val)}")
