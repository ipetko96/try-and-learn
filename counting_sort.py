unsorted_list = [15, 63, 225, 55, 91, 72, 10]


def counting_sort_v1(unsorted_list: list) -> list:
    frequency_list = [0] * (max(unsorted_list) + 1)

    for i in unsorted_list:
        frequency_list[i] += 1

    prefix_sum = []

    for i in range(len(frequency_list)):
        if i == 0:
            prefix_sum.append(frequency_list[i])
        else:
            prefix_sum.append(prefix_sum[i - 1] + frequency_list[i])

    sorted_list = [0] * (len(unsorted_list))

    for i in reversed(unsorted_list):
        sorted_list[prefix_sum[i] - 1] = i
        prefix_sum[i] -= 1

    return sorted_list


def counting_sort_v2(unsorted_list: list) -> list:
    frequency_list = [0] * (max(unsorted_list) + 1)

    for i in unsorted_list:
        frequency_list[i] += 1

    for i in range(1, max(unsorted_list) + 1):
        frequency_list[i] += frequency_list[i - 1]

    sorted_list = [0] * (len(unsorted_list))

    for i in reversed(unsorted_list):
        sorted_list[frequency_list[i] - 1] = i
        frequency_list[i] -= 1

    return sorted_list


def gpt_counting_sort_v2(unsorted_list: list) -> list:
    frequency_list = [0] * (max(unsorted_list) + 1)

    for i in unsorted_list:
        frequency_list[i] += 1

    sorted_index = 0
    sorted_list = [0] * len(unsorted_list)

    for i, freq in enumerate(frequency_list):
        while freq > 0:
            sorted_list[sorted_index] = i
            sorted_index += 1
            freq -= 1

    return sorted_list


import time

t = time.process_time()
print(unsorted_list, counting_sort_v2(unsorted_list))
elapsed_time = time.process_time() - t
# print(elapsed_time)

t = time.process_time()
print(unsorted_list, gpt_counting_sort_v2(unsorted_list))
elapsed_time = time.process_time() - t
# print(elapsed_time)

import math


def sort(array, radix=10):
    if len(array) == 0:
        return array

    # Determine minimum and maximum values
    minValue = array[0]
    maxValue = array[0]
    for i in range(1, len(array)):
        if array[i] < minValue:
            minValue = array[i]
        elif array[i] > maxValue:
            maxValue = array[i]

    # Perform counting sort on each exponent/digit, starting at the least
    # significant digit
    exponent = 1
    while (maxValue - minValue) / exponent >= 1:
        array = countingSortByDigit(array, radix, exponent, minValue)
        exponent *= radix

    return array


def countingSortByDigit(array, radix, exponent, minValue):
    bucketIndex = -1
    buckets = [0] * radix
    output = [None] * len(array)

    # Count frequencies
    for i in range(0, len(array)):
        bucketIndex = math.floor(((array[i] - minValue) / exponent) % radix)
        buckets[bucketIndex] += 1

    # Compute cumulates
    for i in range(1, radix):
        buckets[i] += buckets[i - 1]

    # Move records
    for i in range(len(array) - 1, -1, -1):
        bucketIndex = math.floor(((array[i] - minValue) / exponent) % radix)
        buckets[bucketIndex] -= 1
        output[buckets[bucketIndex]] = array[i]

    return output


print(unsorted_list, sort(unsorted_list))
