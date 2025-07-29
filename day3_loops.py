# day3_loops.py

def multiples_of_three_list():
    return [(i, i/3) for i in range(1, 101) if i % 3 == 0]

if __name__ == "__main__":
    print(multiples_of_three_list())
