from collections import Counter


def t3(n, arr):
    print(Counter(arr).most_common(1))
    a, b = Counter(arr).most_common(1)[0]
    print(a if b > n/2 else -1)


t3(5, [1, 1, 1, 1, 2, 2, 2])
