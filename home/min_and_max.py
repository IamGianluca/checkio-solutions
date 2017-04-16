from collections import defaultdict


def min(*args, **kwargs):
    key = kwargs.get('key', None)
    if len(args) == 1:  # elements passed as iterable
        args = args[0]
    if key:
        storage = defaultdict(list)
        for element in args:
            storage[key(element)].append(element)
        ordered = sorted(storage.keys())
        key = ordered[0]
        return storage[key][0]
    else:
        ordered = sorted(args)
    return ordered[0]


def max(*args, **kwargs):
    key = kwargs.get('key', None)
    if len(args) == 1:  # elements passed as iterable
        args = args[0]
    if key:
        storage = defaultdict(list)
        for element in args:
            storage[key(element)].append(element)
        ordered = sorted(storage.keys())
        key = ordered[-1]
        return storage[key][0]
    else:
        ordered = sorted(args)
        return ordered[-1]
