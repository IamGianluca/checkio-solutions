def min(*args, **kwargs):
    key = kwargs.get('key', None)
    items = [element for element in args]
    return sorted(items[0] if len(items) == 1 else items, key=key)[0]


def max(*args, **kwargs):
    key = kwargs.get('key', None)
    items = [element for element in args]
    return sorted(items[0] if len(items) == 1 else items,
                  key=key, reverse=True)[0]
