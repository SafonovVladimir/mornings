def sum_of_odd_numbers(row_number: int) -> int:
    result_list = [[1], ]
    start_number = 1
    for i in range(2, row_number + 1):
        temp_result = []
        for j in range(i):
            start_number += 2
            temp_result.append(start_number)
        result_list.append(temp_result)
    return sum(result_list[row_number - 1])
    # return result

    # odd_list = []
    # for i in range(0, row_number):
    #     if i % 2 == 1:
    #         odd_list.append(i)
    #
    # for digit in range(len(odd_list):
    #
    #
    # return result

print(sum_of_odd_numbers(4))
print(sum_of_odd_numbers(1))
