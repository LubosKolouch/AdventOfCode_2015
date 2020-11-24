""" Solution Day 3 Advent of code 2005 """


class InputHandler:
    """ class to handle the input """

    def __init__(self, input_f="input3"):
        self.data = None
        self.data_pos = 0
        self.load_input(input_f)

    def load_input(self, input_f):
        """ load the input file """
        with open(input_f, "r") as in_file:
            self.data = in_file.read().strip()

    def get_next_move(self):
        """ Get next move """
        self.data_pos += 1

        try:
            return self.data[self.data_pos-1]
        except IndexError:
            return None


class Santa:
    """ Sante mover """

    def __init__(self):
        self.pos_x = self.pos_y = 0
        self.visited = set()
        self.visited.add((self.pos_x, self.pos_y))

    def move(self, next_move):
        """ do the move """

        if next_move == "v":
            self.pos_y -= 1
        elif next_move == "^":
            self.pos_y += 1
        elif next_move == ">":
            self.pos_x += 1
        elif next_move == "<":
            self.pos_x -= 1
        else:
            raise Exception("error")

        self.visited.add((self.pos_x, self.pos_y))

    def get_visited_houses(self):
        """ return the solution for part 1 """

        return len(self.visited)


def run_part1(input_f="input1"):
    """ Get answer for part 1 """
    input_handler = InputHandler(input_f)

    santa_real = Santa()

    while 1:
        next_move = input_handler.get_next_move()

        if not next_move:
            break

        santa_real.move(next_move)

    print(f"Part1: {santa_real.get_visited_houses()}")


def run_part2(input_f="input3"):
    """ Get answer for part 2 """
    input_handler = InputHandler(input_f)

    santa_real = Santa()
    santa_robot = Santa()

    while 1:
        next_move = input_handler.get_next_move()

        if not next_move:
            break

        santa_real.move(next_move)
        next_move = input_handler.get_next_move()

        if not next_move:
            break

        santa_robot.move(next_move)

    total_set = santa_real.visited
    total_set.update(santa_robot.visited)
    print(f"Part 2: {len(total_set)}")
    return len(total_set)


def main():
    """ run """

    run_part1('input3')
    run_part2('input3')

    print("Running tests:")
    test1 = run_part2('input3_test1')
    assert test1 == 3

    test2 = run_part2('input3_test2')
    assert test2 == 3

    test3 = run_part2('input3_test3')
    assert test3 == 11


if __name__ == "__main__":
    main()
