def euler(max_size):
    size = 1
    total_sum = 1
    red_number = 1
    while size < max_size:
        size += 2
        for i in range(0,4):
            print red_number
            red_number += size-1
            total_sum += red_number
    return total_sum

if __name__ == '__main__':
    print euler(1001)
