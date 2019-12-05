def runIntcodeProgram(intcode):

    index = 0

    while(index < len(intcode)):
        opcode = intcode[index]

        print('next input: {}'.format(intcode[index:index+4]))

        if opcode == 99:
            print('halting: {}'.format(index))
            break

        in1 = intcode[index + 1]
        in2 = intcode[index + 2]
        out = intcode[index + 3]

        if opcode == 1:
            intcode[out] = intcode[in1] + intcode[in2]
        if opcode == 2:
            intcode[out] = intcode[in1] * intcode[in2]
        index +=4

        print('new index: {}\t{}'.format(index,intcode))

    return intcode


def readIntcodeProgramFromFile(file):
    fileHandler = open(file)
    intcodeStrings = fileHandler.readline().strip().split(',')
    fileHandler.close()

    intcode = []

    for intcodeString in intcodeStrings:
        intcode.append(int(intcodeString))

    return intcode


def main():
    intcode = readIntcodeProgramFromFile('input.txt')

    # correct inputs
    intcode[1] = 12
    intcode[2] = 2

    result = runIntcodeProgram(intcode)

    print(result)


def test():
    # tests ([input],[expected])
    test1 = ([1,0,0,0,99],[2,0,0,0,99])
    test2 = ([2,3,0,3,99],[2,3,0,6,99])
    test3 = ([2,4,4,5,99,0],[2,4,4,5,99,9801])
    test4 = ([1,1,1,4,99,5,6,0,99],[30,1,1,4,2,5,6,0,99])

    tests = [test1, test2, test3, test4]

    for test in tests:
        result = runIntcodeProgram(test[0])
        expected = test[1]

        if(result != expected):
            print(result)
            print(expected)
            raise AssertionError('Test suite not passed')

    print('Passed all tests')


if __name__ == "__main__":
    main()
