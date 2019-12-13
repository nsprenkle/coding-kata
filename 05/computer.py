def run(mem):

    ip = 0

    while(ip < len(mem)):
        opcode = mem[ip]

        # print('next input: {}'.format(mem[ip:ip+4]))

        if opcode == 99:
            # print('halting: {}'.format(ip))
            break

        if opcode == 1:
            a = mem[ip + 1]
            b = mem[ip + 2]
            out = mem[ip + 3]
            mem[out] = mem[a] + mem[b]
            ip += 4
        if opcode == 2:
            a = mem[ip + 1]
            b = mem[ip + 2]
            out = mem[ip + 3]
            mem[out] = mem[a] * mem[b]
            ip += 4

        # print('new address: {}\t{}'.format(ip,mem))

    return mem


def intcode_from_file(file):
    file_handler = open(file)
    intcode_strings = file_handler.readline().strip().split(',')
    file_handler.close()

    intcode = []

    for intcode_string in intcode_strings:
        intcode.append(int(intcode_string))

    return intcode


def main():
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
    main()
