def add(numbers_string):
    if not isinstance(numbers_string, str):
        raise TypeError('Must be string')

    numbers = numbers_string.split(",")
    numbers = list(map(int, numbers))
