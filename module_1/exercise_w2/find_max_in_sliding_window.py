def find_max_in_range(num_list: list[int], k: int) -> list[int]:
    result: list[int] = []
    loop_times = len(num_list) - k + 1

    for i in range(loop_times):
        target_range = num_list[i:i + k]
        result.append(max(target_range))

    return result


print(find_max_in_range([3, 4, 5, 1], 3))
