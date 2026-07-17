import sys


input = sys.stdin.read


def solve():
    pass


def main():
    global next_token
    input_data = input().split()
    if not input_data:
        return

    tokens = iter(input_data)
    next_token = lambda: next(tokens)

    HAS_TEST_CASES = True

    if HAS_TEST_CASES:
        t = int(next_token())
        for _ in range(t):
            n = int(next_token())
            k = int(next_token())
            solve(n, k)
    else:
        n = int(next_token())
        k = int(next_token())
        solve(n, k)


if __name__ == "__main__":
    main()
