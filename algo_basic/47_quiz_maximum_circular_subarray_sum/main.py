"""
1. Maximum subarray sum
Input [1, 3, -1, -2, 4, 5, 7, -10, -1, 2]
Output 16 (1 + 3 - 1 - 2 + 4 + 5 + 7)

2. Maximum circular subarray sum
Input [1, 3, -1, -2, 4, 5, 7, -10, -1, 2]
Output 19 (1 + 3 - 1 - 2 + 4 + 5 + 7 + 2)
"""

from typing import List


def get_max_sequence_sum(numbers: List[int], operator=max) -> int:
    result_sequence, sum_sequence = 0, 0
    for num in numbers:
        # temp_sum_sequence = sum_sequence + num
        # if num < temp_sum_sequence:
        #     sum_sequence = temp_sum_sequence
        # else:
        # sum_sequence = num
        sum_sequence = max(num, sum_sequence + num)

        # if result_sequence < sum_sequence:
        #     result_sequence = sum_sequence
        result_sequence = max(result_sequence, sum_sequence)
    return result_sequence


def find_max_circular_sequence_sum(numbers: List[int], operator=max) -> int:
    # [1,2,3,-1,-2,-3,3,2,1]
    # [-100,1,2,3,-1,-2,-3,3,2,1,-100]
    max_sequence_sum = get_max_sequence_sum(numbers)
    # invert_numbers = []
    # all_sum = 0
    # for num in numbers:
    #     all_sum += num
    #     invert_numbers.append(-num)

    # max_wrap_sequence = all_sum - (get_max_sequence_sum(invert_numbers))
    max_wrap_sequence = sum(numbers) - \
        get_max_sequence_sum(numbers, operator=min)
    return max(max_sequence_sum, max_wrap_sequence)


if __name__ == '__main__':
    print(get_max_sequence_sum([1, -2, 3, 6, -1, 2, 4, -5, 2]))
    print(find_max_circular_sequence_sum([1, -2, 3, 6, -1, 2, 4, -5, 2]))
