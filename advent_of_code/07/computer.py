def run(mem, input=None):

    ip = 0
    output = None

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
            # print('halting: {}'.format(ip))
            break

        # use the mode to get immediate or positional values
        # a = mem[ip + 1] if mode_a == 1 else mem[mem[ip + 1]]
        # b = mem[ip + 2] if mode_b == 1 else mem[mem[ip + 2]]

        arg_1 = mem[ip + 1] if ip + 1 < len(mem) else None
        arg_2 = mem[ip + 2] if ip + 2 < len(mem) else None
        arg_3 = mem[ip + 3] if ip + 3 < len(mem) else None

        # add
        if opcode == 1:
            val_1 = arg_1 if mode_1 == 1 else mem[arg_1]
            val_2 = arg_2 if mode_2 == 1 else mem[arg_2]
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
            mem[arg_1] = input.pop()
            ip += 2
        # write output to position of arg_1
        elif opcode == 4:
            output = arg_1 if mode_1 == 1 else mem[arg_1]
            ip += 2
        # jump-if-true
        elif opcode == 5:
            val_1 = arg_1 if mode_1 == 1 else mem[arg_1]
            val_2 = arg_2 if mode_2 == 1 else mem[arg_2]
            ip = val_2 if val_1 != 0 else ip + 3
        # jump-if-false
        elif opcode == 6:
            val_1 = arg_1 if mode_1 == 1 else mem[arg_1]
            val_2 = arg_2 if mode_2 == 1 else mem[arg_2]
            ip = val_2 if val_1 == 0 else ip + 3
        # less than
        elif opcode == 7:
            val_1 = arg_1 if mode_1 == 1 else mem[arg_1]
            val_2 = arg_2 if mode_2 == 1 else mem[arg_2]
            mem[arg_3] = 1 if val_1 < val_2 else 0
            ip += 4
        # equals
        elif opcode == 8:
            val_1 = arg_1 if mode_1 == 1 else mem[arg_1]
            val_2 = arg_2 if mode_2 == 1 else mem[arg_2]
            mem[arg_3] = 1 if val_1 == val_2 else 0
            ip += 4
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


if __name__ == "__main__":
    day_05()
