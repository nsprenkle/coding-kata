def run(mem, input=None):

    ip = 0

    while(ip < len(mem)):
        # normalize and parse instruction
        instruction = str(mem[ip]).zfill(5)

        # opcode is the last 2 digits of instruction
        opcode = int(instruction[3:5])

        # mode (0: position, 1: immediate) per param from first 3 digits
        mode_1 = int(instruction[2])
        mode_2 = int(instruction[1])
        mode_3 = int(instruction[0])

        # print('next input: {}'.format(mem[ip:ip+4]))

        if opcode == 99:
            print('halting: {}'.format(ip))
            break

        # use the mode to get immediate or positional values
        # a = mem[ip + 1] if mode_a == 1 else mem[mem[ip + 1]]
        # b = mem[ip + 2] if mode_b == 1 else mem[mem[ip + 2]]

        arg_1 = mem[ip + 1]
        arg_2 = mem[ip + 2]
        arg_3 = mem[ip + 3]

        # add
        if opcode == 1:
            val_1 = arg_1 if mode_1 == 1 else mem[arg_1]
            val_2 = arg_2 if mode_2 == 1 else mem[arg_2]
            # print('[{}] < {} + {}'.format(arg_3, arg_1, arg_2))
            mem[arg_3] = val_1 + val_2
            ip += 4
        # multiply
        elif opcode == 2:
            val_1 = arg_1 if mode_1 == 1 else mem[arg_1]
            val_2 = arg_2 if mode_2 == 1 else mem[arg_2]
            mem[arg_3] = val_1 * val_2
            ip += 4
        # write input
        elif opcode == 3:
            mem[arg_1] = input
            ip += 2
        # write output to position of arg_1
        elif opcode == 4:
            output = arg_1 if mode_1 == 1 else mem[arg_1]
            ip += 2
        else:
            raise Exception('Bad opcode {} at ip {}\n'.format(opcode, ip, mem))

    return output


def intcode_from_file(file):
    file_handler = open(file)
    intcode_strings = file_handler.readline().strip().split(',')
    file_handler.close()

    intcode = []

    for intcode_string in intcode_strings:
        intcode.append(int(intcode_string))

    return intcode


def day_05():
    file = '/Users/nsprenkle/Development/sandbox/adventofcode/05/day_05_input.txt'
    initial_state = intcode_from_file(file)

    output = run(initial_state, input=1)
    print('Output: {}'.format(output))


def day_02():
    initial_state = intcode_from_file('input.txt')

    target_output = 19690720

    for a in range(0, 100):
        for b in range(0, 100):
            result = test_input(initial_state, a, b)
            print("a: {}, b: {}, result: {}".format(a, b, result))
            if result == target_output:
                return (a, b)
                # Solution a: 52, b: 96, result: 19690720


def test_input(initial_state, a, b):
    state_copy = []

    for address in initial_state:
        state_copy.append(address)

    state_copy[1] = a
    state_copy[2] = b

    result = run(state_copy)

    return result[0]


if __name__ == "__main__":
    day_05()
