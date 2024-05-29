def mean(number):
    total_sum = sum(int(digit) for digit in str(number))
    digit_count = len(str(number))

    mean_value = total_sum / digit_count
    return mean_value