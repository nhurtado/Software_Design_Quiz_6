def add(numbers_string):
    if not isinstance(numbers_string, str):
        raise TypeError('Must be string')

    try:
        int(numbers_string[0])
        numbers = numbers_string.split(",")
    except ValueError:
        numbers = numbers_string[1:].split(numbers_string[0])
    numbers = list(map(int, numbers))

    return sum(numbers)
