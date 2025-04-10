import sys
import math


def part_one(directions):
    visited_houses = set()
    current_x, current_y = 0, 0

    moves = {
        '<': (-1, 0),
        '^': (0, 1),
        '>': (1, 0),
        'v': (0, -1)
    }

    visited_houses.add((current_x, current_y))
    for direction in directions:
        dx, dy = moves[direction]
        current_x += dx
        current_y += dy
        
        visited_houses.add((current_x, current_y))

    return len(visited_houses)


def part_two(directions):
    visited_houses = set()

    moves = {
        '<': (-1, 0),
        '^': (0, 1),
        '>': (1, 0),
        'v': (0, -1)
    }
    santas_positions = [(0, 0), (0, 0)]

    visited_houses.add((0, 0))
    for i, direction in enumerate(directions):
        dx, dy = moves[direction]
        santa_id = i % len(santas_positions)

        x, y = santas_positions[santa_id]
        x += dx
        y += dy
        santas_positions[santa_id] = (x, y)

        visited_houses.add(santas_positions[santa_id])

    return len(visited_houses)


def solve():
    directions = input().strip()
    print("Part 1:", part_one(directions))
    print("Part 2:", part_two(directions))


if __name__ == "__main__":
    solve()
