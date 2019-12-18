import computer


def clone(array):
    copy = []

    for elem in array:
        copy.append(elem)

    return copy


def run(intcode, phase_sequence):
    # Amp inputs are [input signal, phase sequence], these will be popped in the correct order

    output = 0

    for amp in phase_sequence:
        mem = clone(intcode)
        output = computer.run(mem, [output, amp])

    return output


def find_max_signal(intcode):
    """ get the max value and sequence from an amp sequence """
    sequences = sequence_permutations([0, 1, 2, 3, 4])
    values = []

    for sequence in sequences:
        values.append(run(intcode, sequence))

    return max(values), sequences[values.index(max(values))]


# Shamelessly borrowed from https://www.codesdope.com/blog/article/generating-permutations-of-all-elements-of-an-arra/
def sequence_permutations(a):
    permutations = []

    def permutation(start, end):

        if end == start:
            permutations.append(clone(a))
            return
        for i in range(start, end+1):
            # swapping
            a[i], a[start] = a[start], a[i]
            # calling permutation function
            # by keeping the element at the index start fixed
            permutation(start+1, end)
            # restoring the array
            a[i], a[start] = a[start], a[i]

        return permutations

    permutation(0, len(a)-1)

    return permutations


def intcode_from_file(file):
    file_handler = open(file)
    intcode_strings = file_handler.readline().strip().split(',')
    file_handler.close()

    intcode = []

    for intcode_string in intcode_strings:
        intcode.append(int(intcode_string))

    return intcode


if __name__ == "__main__":
    intcode = intcode_from_file("intcode.txt")
    (max_signal, sequence) = find_max_signal(intcode)

    print('Max signal {} for sequence {}'.format(max_signal, sequence))
