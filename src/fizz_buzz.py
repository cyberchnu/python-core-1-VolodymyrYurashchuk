def fizz_buzz(param):
    is_divisible_by_3 = param % 3 == 0
    is_divisible_by_5 = param % 5 == 0

    if is_divisible_by_3 and not is_divisible_by_5:
        return "Fizz"
    elif not is_divisible_by_3 and is_divisible_by_5:
        return "Buzz"
    elif is_divisible_by_3 and is_divisible_by_5:
        return "FizzBuzz"
    else:
        return str(param)