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
    print("### DAY 1 ###")
    with open('data/day1.txt') as f:
        puzzle_input = f.readlines()

    entries = [(int(x), int(y)) for x in puzzle_input
               for y in puzzle_input if int(x) + int(y) == 2020][0]
    result = entries[0] * entries[1]
    print(f"The two numbers that sum to 2020 are {entries[0]} and {entries[1]}"
          f". The product is {result}.")

    entries = [(int(x), int(y), int(z)) for x in puzzle_input
               for y in puzzle_input for z in puzzle_input
               if int(x) + int(y) + int(z) == 2020][0]
    result = entries[0] * entries[1] * entries[2]
    print(f"The three numbers that sum to 2020 are {entries[0]}, {entries[1]}"
          f" and {entries[2]}. The product is {result}.")


def day2():
    """ Day 2: Password Philosophy

    Your flight departs in a few days from the coastal airport; the easiest
    way down to the coast from here is via toboggan.

    The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day.
    "Something's wrong with our computers; we can't log in!" You ask if you
    can take a look.

    Their password database seems to be a little corrupted: some of the
    passwords wouldn't have been allowed by the Official Toboggan Corporate
    Policy that was in effect when they were chosen.

    To try to debug the problem, they have created a list (your puzzle input)
    of passwords (according to the corrupted database) and the corporate
    policy when that password was set.

    For example, suppose you have the following list:

    1-3 a: abcde
    1-3 b: cdefg
    2-9 c: ccccccccc

    Each line gives the password policy and then the password. The password
    policy indicates the lowest and highest number of times a given letter
    must appear for the password to be valid. For example, 1-3 a means that
    the password must contain a at least 1 time and at most 3 times.

    In the above example, 2 passwords are valid. The middle password, cdefg,
    is not; it contains no instances of b, but needs at least 1. The first and
    third passwords are valid: they contain one a or nine c, both within the
    limits of their respective policies.

    How many passwords are valid according to their policies?
    """
    print("### DAY 2 ###")
    with open('data/day2.txt') as f:
        puzzle_input = f.readlines()

    legal_passwords_cnt = 0
    for i in puzzle_input:
        items = str(i).split(' ')
        occurence_limits = items[0].split('-')
        occurence_char = items[1][:-1]
        password = items[2]
        if (int(occurence_limits[0]) <= password.count(occurence_char)
                <= int(occurence_limits[1])):
            legal_passwords_cnt += 1
    print(f"According to the first set of rules, {legal_passwords_cnt} out of"
          f" {len(puzzle_input)} passwords are legal")

    """ Part Two

    While it appears you validated the passwords correctly, they don't seem to
    be what the Official Toboggan Corporate Authentication System is expecting.

    The shopkeeper suddenly realizes that he just accidentally explained the
    password policy rules from his old job at the sled rental place down the
    street! The Official Toboggan Corporate Policy actually works a little
    differently.

    Each policy actually describes two positions in the password, where 1 means
    the first character, 2 means the second character, and so on. (Be careful;
    Toboggan Corporate Policies have no concept of "index zero"!) Exactly one
    of these positions must contain the given letter. Other occurrences of the
    letter are irrelevant for the purposes of policy enforcement.

    Given the same example list from above:
        1-3 a: abcde is valid: position 1 contains a and position 3 does not.
        1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
        2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

    How many passwords are valid according to the new interpretation of the
    policies?
    """
    legal_passwords_cnt = 0
    for i in puzzle_input:
        items = str(i).split(' ')
        occurence_limits = items[0].split('-')
        occurence_char = items[1][:-1]
        password = items[2]
        # xor operation:
        if ((password[int(occurence_limits[0])-1] == occurence_char
            != password[int(occurence_limits[1])-1])
                or (password[int(occurence_limits[0])-1] != occurence_char
                    == password[int(occurence_limits[1])-1])):
            legal_passwords_cnt += 1
    print(f"According to the second set of rules, {legal_passwords_cnt} out of"
          f" {len(puzzle_input)} passwords are legal")


def day3():
    """ Day 3: Toboggan Trajectory ---

    With the toboggan login problems resolved, you set off toward the airport.
    While travel by toboggan might be easy, it's certainly not safe: there's
    very minimal steering and the area is covered in trees. You'll need to see
    which angles will take you near the fewest trees.

    Due to the local geology, trees in this area only grow on exact integer
    coordinates in a grid. You make a map (your puzzle input) of the open
    squares (.) and trees (#) you can see. For example:

    ..##.......
    #...#...#..
    .#....#..#.
    ..#.#...#.#
    .#...##..#.
    ..#.##.....
    .#.#.#....#
    .#........#
    #.##...#...
    #...##....#
    .#..#...#.#

    These aren't the only trees, though; due to something you read about once
    involving arboreal genetics and biome stability, the same pattern repeats
    to the right many times:

    ..##.........##.........##.........##.........##.........##.......  --->
    #...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
    .#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
    ..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
    .#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
    ..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
    .#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
    .#........#.#........#.#........#.#........#.#........#.#........#
    #.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
    #...##....##...##....##...##....##...##....##...##....##...##....#
    .#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

    You start on the open square (.) in the top-left corner and need to reach
    the bottom (below the bottom-most row on your map).

    The toboggan can only follow a few specific slopes (you opted for a cheaper
    model that prefers rational numbers); start by counting all the trees you
    would encounter for the slope right 3, down 1:

    From your starting position at the top-left, check the position that is
    right 3 and down 1. Then, check the position that is right 3 and down 1
    from there, and so on until you go past the bottom of the map.

    The locations you'd check in the above example are marked here with O
    where there was an open square and X where there was a tree:

    ..##.........##.........##.........##.........##.........##.......  --->
    #..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
    .#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
    ..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
    .#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
    ..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
    .#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
    .#........#.#........X.#........#.#........#.#........#.#........#
    #.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
    #...##....##...##....##...#X....##...##....##...##....##...##....#
    .#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

    In this example, traversing the map using this slope would cause you to
    encounter 7 trees.

    Starting at the top-left corner of your map and following a slope of right
    3 and down 1, how many trees would you encounter?
    """
    print("### DAY 3 ###")
    with open('data/day3.txt') as f:
        puzzle_input = f.readlines()

    def tree_encounters(stepX, stepY):
        tree_cnt = 0
        indX = 0
        indY = 0
        for indY in range(0, len(puzzle_input), stepY):
            if indX > len(puzzle_input[0]) - 2:
                indX -= len(puzzle_input[0]) - 1
            if puzzle_input[indY][indX] == '#':
                tree_cnt += 1
            indX += stepX
        return tree_cnt

    tree_cnt = tree_encounters(3, 1)
    print(f"Part 1: the number of trees encountered is: {tree_cnt}")

    score = 1
    for x, y in ([(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]):
        score *= tree_encounters(x, y)
    print(f"Part 2: the number of trees encountered multiplied together is: "
          f"{score}")


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
    # day2()
    day3()
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
