def day1():
    """ Day 1: Report Repair

    After saving Christmas five years in a row, you've decided to take a
    vacation at a nice resort on a tropical island. Surely, Christmas will go
    on without you. The tropical island has its own currency and is entirely
    cash-only. The gold coins used there have a little picture of a starfish;
    the locals just call them stars. None of the currency exchanges seem to
    have heard of them, but somehow, you'll need to find fifty of these coins
    by the time you arrive so you can pay the deposit on your room.

    To save your vacation, you need to get all fifty stars by December 25th.

    Collect stars by solving puzzles. Two puzzles will be made available on
    each day in the Advent calendar; the second puzzle is unlocked when you
    complete the first. Each puzzle grants one star. Good luck!
    Before you leave, the Elves in accounting just need you to fix your
    expense report (your puzzle input); apparently, something isn't quite
    adding up.

    Specifically, they need you to find the two entries that sum to 2020 and
    then multiply those two numbers together.
    """
    with open('data/day1.txt') as f:
        puzzle_input = f.readlines()

    entries = [(int(x), int(y)) for x in puzzle_input
               for y in puzzle_input if int(x) + int(y) == 2020][0]
    result = entries[0] * entries[1]

    print(f"Day 1 solution: <{result}>, which was found by multiplying "
          f"the numbers {entries[0]} and {entries[1]}")


def day2():
    raise NotImplementedError


def day3():
    raise NotImplementedError


def day4():
    raise NotImplementedError


def day5():
    raise NotImplementedError


def day6():
    raise NotImplementedError


def day7():
    raise NotImplementedError


def day8():
    raise NotImplementedError


def day9():
    raise NotImplementedError


def day10():
    raise NotImplementedError


def day11():
    raise NotImplementedError


def day12():
    raise NotImplementedError


def day13():
    raise NotImplementedError


def day14():
    raise NotImplementedError


def day15():
    raise NotImplementedError


def day16():
    raise NotImplementedError


def day17():
    raise NotImplementedError


def day18():
    raise NotImplementedError


def day19():
    raise NotImplementedError


def day20():
    raise NotImplementedError


def day21():
    raise NotImplementedError


def day22():
    raise NotImplementedError


def day23():
    raise NotImplementedError


def day24():
    raise NotImplementedError


def main():
    # day1()
    day2()
    # day3()
    # day4()
    # day5()
    # day6()
    # day7()
    # day8()
    # day9()
    # day10()
    # day11()
    # day12()
    # day13()
    # day14()
    # day15()
    # day16()
    # day17()
    # day18()
    # day19()
    # day20()
    # day21()
    # day22()
    # day23()
    # day24()


if __name__ == "__main__":
    main()
