def runProgram(mem):

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
            ip +=4
        if opcode == 2:
            a = mem[ip + 1]
            b = mem[ip + 2]
            out = mem[ip + 3]
            mem[out] = mem[a] * mem[b]
            ip +=4

        # print('new address: {}\t{}'.format(ip,mem))

    return mem


def readIntcodeProgramFromFile(file):
    fileHandler = open(file)
    intcodeStrings = fileHandler.readline().strip().split(',')
    fileHandler.close()

    intcode = []

    for intcodeString in intcodeStrings:
        intcode.append(int(intcodeString))

    return intcode


def main():
    initialState = readIntcodeProgramFromFile('input.txt')

    targetOutput = 19690720

    for a in range(0, 100):
        for b in range(0, 100):
            result = tryInputs(initialState, a, b)
            print("a: {}, b: {}, result: {}".format(a,b,result))
            if result == targetOutput:
                return (a, b)
                # Solution a: 52, b: 96, result: 19690720


def tryInputs(initialState, a, b):
    stateCopy = []

    for address in initialState:
        stateCopy.append(address)

    stateCopy[1] = a
    stateCopy[2] = b

    result = runProgram(stateCopy)

    return result[0]


def test():
    # tests ([input],[expected])
    test1 = ([1,0,0,0,99],[2,0,0,0,99])
    test2 = ([2,3,0,3,99],[2,3,0,6,99])
    test3 = ([2,4,4,5,99,0],[2,4,4,5,99,9801])
    test4 = ([1,1,1,4,99,5,6,0,99],[30,1,1,4,2,5,6,0,99])

    tests = [test1, test2, test3, test4]

    for test in tests:
        result = runProgram(test[0])
        expected = test[1]

        if(result != expected):
            print(result)
            print(expected)
            raise AssertionError('Test suite not passed')

    print('Passed all tests')


if __name__ == "__main__":
    main()
