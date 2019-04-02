# -*- coding: utf-8 -*-


def calc(n_500, n_100, n_50, total):
    ans = 0
    for i in range(n_500+1):
        for j in range(n_100+1):
            for k in range(n_50+1):
                if 500*i + 100*j + 50 * k == total:
                    ans += 1
    return ans


if __name__ == "__main__":
    n_500 = int(input())
    n_100 = int(input())
    n_50 = int(input())
    total = int(input())

    print(calc(n_500, n_100, n_50, total))
