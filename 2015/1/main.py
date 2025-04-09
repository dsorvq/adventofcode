def solve():
    instructions = input()

    floor = 0
    on_basement_position = None

    for i, instruction in enumerate(instructions):
        if instruction == "(":
            floor += 1
        elif instruction == ")":
            floor -= 1

        if floor == -1 and on_basement_position is None:
            on_basement_position = i + 1

    print(f"Resulted floor: {floor}")
    print(f"In basement for the first time: {on_basement_position}")


if __name__ == "__main__":
    solve()
