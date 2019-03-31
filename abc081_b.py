# -*- coding: utf-8 -*-


def calc(inp_line):
    count = 0
    while True:
        for i, value in enumerate(inp_line):
            if value % 2 == 0:
                inp_line[i] = value / 2
            else:
                return count
        count = count + 1


if __name__ == "__main__":
    total = int(input())
    inp_line = [int(s) for s in input().split()]
    print(calc(inp_line))
