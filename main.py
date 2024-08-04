def number_of_ways_to_clim_stairs(total_steps):
    present_value = 1
    last_value = 1
    if total_steps == 0:
        return 0
    elif total_steps == 1:
        return 1
    else:
        for value in range(2, total_steps+1):
            temp = present_value
            present_value = present_value + last_value
            last_value = temp
        return present_value
total_steps = 3
call_function = number_of_ways_to_clim_stairs(total_steps)
print(call_function)