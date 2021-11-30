def rec_subset_sum_count(numbers, wanted_sum, current_sum, idx):
    """
    :param numbers: list of integers.
    :param wanted_sum: integer, the wanted sum.
    :param current_sum: integer, temporary sum.
    :param idx: integer, moving index.
    :return: number of combinations to get the wanted sum.
    """
    if current_sum == wanted_sum:
        return 1
    if current_sum > wanted_sum or idx > len(numbers) - 1:
        return 0
    return rec_subset_sum_count(numbers, wanted_sum, current_sum + numbers[idx], idx + 1) + \
           rec_subset_sum_count(numbers, wanted_sum, current_sum, idx + 1)


def subset_sum_count(ls, num):
    """
    :param ls: list of integers.
    :param num: integer, the wanted sum.
    :return: number of combinations to get the wanted sum.
    """
    return rec_subset_sum_count(ls, num, 0, 0)


def recursive_subset_sums(numbers, wanted_sum, current_sum, current_numbers, idx, total_lists):
    """
    :param numbers: list of integers.
    :param wanted_sum: integer, the wanted sum.
    :param current_sum: integer, temporary sum.
    :param current_numbers: integer, temporary sum.
    :param idx: integer, moving index.
    :param total_lists: list, contains lists of all combinations of getting wanted sum.
    :return: list of lists with combinations of getting the wanted sum.
    """
    if current_sum == wanted_sum:
        total_lists.append(current_numbers)
    elif current_sum < wanted_sum and idx < len(numbers):
        recursive_subset_sums(numbers, wanted_sum, current_sum + numbers[idx],
                              current_numbers + [numbers[idx]], idx + 1, total_lists)  # with
        recursive_subset_sums(numbers, wanted_sum, current_sum, current_numbers, idx + 1, total_lists)


def subset_sums(ls, num):
    """
    :param ls: list of integers.
    :param num: integer, the wanted sum.
    :return: list of lists with combinations of getting the wanted sum.
    """
    total_lists = []
    recursive_subset_sums(ls, num, 0, [], 0, total_lists)
    return total_lists


def recursive_subset_sum_memo(numbers, wanted_sum, current_sum, current_numbers, idx, blacklist):
    """
    :param numbers: list of integers.
    :param wanted_sum: integer, the wanted sum.
    :param current_sum: integer, temporary sum.
    :param current_numbers: integer, temporary sum.
    :param idx: integer, moving index.
    :param blacklist: list, list which memorized all False combinations
    :return: bool, True weather there is combination of numbers that their sum is wanted sum.
    """
    if current_numbers not in blacklist:
        if current_sum == wanted_sum:
            return True
        elif current_sum < wanted_sum and idx < len(numbers):
            if recursive_subset_sum_memo(numbers, wanted_sum, current_sum + numbers[idx],
                                         current_numbers + [numbers[idx]], idx + 1, blacklist) or \
                    recursive_subset_sum_memo(numbers, wanted_sum, current_sum, current_numbers, idx + 1, blacklist):
                return True
        blacklist.append(current_numbers)
    return False


def subset_sum_memo(ls, num):
    """
    :param ls: list of integers.
    :param num: integer, the wanted sum.
    :return: bool, True weather there is combination of numbers that their sum is wanted sum.
    """
    return recursive_subset_sum_memo(ls, num, 0, [], 0, [])


def recursive_subset_sum_with_repeats(numbers, wanted_sum, current_sum, current_numbers, total_lists):
    """
    :param numbers: list of integers.
    :param wanted_sum: the wanted sum.
    :param current_sum: integer, temporary sum.
    :param current_numbers: list, temporary numbers in list.
    :param total_lists: list, contains lists of all combinations of getting wanted sum.
    :return: list, list of all combinations that their sum equals to wanted sum.
    """
    if current_sum == wanted_sum:
        total_lists.append(current_numbers)
    elif current_sum < wanted_sum:
        for num in numbers:
            recursive_subset_sum_with_repeats(numbers, wanted_sum, current_sum + num, current_numbers + [num],
                                              total_lists)


def subset_sum_with_repeats(ls, num):
    """
    :param ls: list of integers
    :param num: the wanted sum.
    :return: list, list of all combinations that their sum equals to wanted sum.
    """
    total_lists = []
    recursive_subset_sum_with_repeats(ls, num, 0, [], total_lists)
    return total_lists


def recursive_abc_words(num, perm_st, current_st, total_abc_lists):
    """
    :param num: integer, num that represents the wanted len of string.
    :param perm_st: string, the permanent string which wanted to change - 'abc'
    :param current_st: string, the temporary string.
    :param total_abc_lists: list, list of all combinations of string in len(num), with 'abc'
    :return:
    """
    if len(current_st) == num:
        total_abc_lists.append(current_st)
        return
    recursive_abc_words(num, perm_st, current_st + perm_st[0], total_abc_lists)
    recursive_abc_words(num, perm_st, current_st + perm_st[1], total_abc_lists)
    recursive_abc_words(num, perm_st, current_st + perm_st[2], total_abc_lists)


def abc_words(num):
    """
    :param num: integer, num that represents the wanted len of string.
    :return: list, list of all combinations of string in len(num) using 'abc'.
    """
    total_abc_lists = []
    recursive_abc_words(num, 'abc', '', total_abc_lists)
    return total_abc_lists, len(total_abc_lists)


def rec_char_to_char_words(ch1, ch2, num, current_st, total_chars_lists):
    """
    :param ch1: string, the first char (smaller in ascii table than ch2)
    :param ch2: string, the second char (bigger in ascii table than ch1)
    :param num: integer, len of the wanted strings
    :param current_st: string, the temporary string.
    :param total_chars_lists: list, list of all combinations of string in len(num) using all word between ch1 and ch2
    :return:
    """
    if len(current_st) == num:
        total_chars_lists.append(current_st)

    elif len(current_st) < num:
        for number in range(ord(ch1), ord(ch2) + 1):
            rec_char_to_char_words(ch1, ch2, num, current_st + chr(number), total_chars_lists)


def char_to_char_words(ch1, ch2, num):
    """
    :param ch1: string, the first char (smaller in ascii table than ch2)
    :param ch2: string, the second char (bigger in ascii table than ch1)
    :param num: integer, len of the wanted strings
    :return: total_chars_lists: list, list of all combinations of string in len(num) using all word between ch1 and ch2
    """
    total_chars_lists = []
    rec_char_to_char_words(ch1, ch2, num, '', total_chars_lists)
    return total_chars_lists


def solve_maze_monotonic(maze):
    return
