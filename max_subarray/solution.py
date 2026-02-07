def find_max_contiguous_subarray(nums_list):
    local_max = nums_list[0]
    global_max = nums_list[0]

    for index in range(1, len(nums_list)):
        local_max = max(nums_list[index], local_max + nums_list[index])
        global_max = max(global_max, local_max)

    return global_max
