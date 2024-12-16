def cool_range(start, end=None, step=1):
    if end is None:
        end = start
        start = 0

    if step > 0:
        while start < end:
            yield start
            start += step
    elif step < 0:
        while start > end:
            yield start
            start += step
    else:
        raise ValueError('Zero step is not allowed')


assert list(range(0, 2)) == list(cool_range(0, 2))
assert list(range(0, 30, 10)) == list(cool_range(0, 30, 10))
assert list(range(-10, 30, 10)) == list(cool_range(-10, 30, 10))
assert list(range(-10, -30, -10)) == list(cool_range(-10, -30, -10))
assert list(range(-10, -30, -10)) == list(cool_range(-10, -30, -10))
assert list(range(-10, -30, 0)) == list(cool_range(-10, -30, 0))
