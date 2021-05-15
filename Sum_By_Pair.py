# O(n) solution for finding indices of pair of numbers that add up to a given number.

mapping_diff = {}


def print_pair(input_list, input_length, sum):
    key_1 = None
    key_2 = None
    for index in range(input_length):
        diff = sum - input_list[index]
        try:
            if mapping_diff[diff] == input_list[index]:
                key_1 = input_list[index]
                key_2 = diff
                print('Values are: ', input_list[index], ' & ', diff)
        except KeyError:
            mapping_diff[input_list[index]] = diff

    for index in range(input_length):
        mapping_diff[input_list[index]] = index
    print('At indices: ', mapping_diff.get(key_1), ' & ', mapping_diff.get(key_2))


if __name__ == '__main__':
    input_list = [1, 6, 8, 4, 6, 89, 7]
    sum = 14
    length = len(input_list)
    print_pair(input_list, length, sum)
