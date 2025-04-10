import sys
import math


def solve():
    total_paper_need = 0
    total_reebon_need = 0
    for line in sys.stdin:
        sides = sorted([int(x) for x in line.split("x")])

        total_paper_need += sides[0]*sides[1]
        for i, _ in enumerate(sides):
            total_paper_need += 2 * (sides[i] * sides[(i + 1) % len(sides)])

        total_reebon_need += 2*sides[0] + 2*sides[1]
        total_reebon_need += math.prod(sides)

    print("Total wrapping paper need: ", total_paper_need)
    print("Total reebon need: ", total_reebon_need)


if __name__ == "__main__":
    solve()
