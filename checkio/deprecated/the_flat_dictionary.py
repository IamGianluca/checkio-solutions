

def flatten(dictionary):
    """Given a dictionary where the keys are strings and the values are strings
    or dictionaries, flatten the dictionary, but save the structures in the
    keys. The result is a dictionary without the nested dictionaries. The keys
    contain paths that contain the parent keys from the original dictionary.
    The keys in the path are separated by a "/". If a value is an empty
    dictionary, then it is replaced by an empty string ("").

    Args:
        dictionary [dict]: The dictionary to flatten.
    Returns:
        An flatten [dict].
    """
    stack = [((), dictionary)]
    result = {}
    while stack:
        path, current = stack.pop()
        for k, v in current.items():
            if isinstance(v, dict) and v:
                stack.append((path + (k,), v))
            else:
                if not v:
                    v = ""
                result["/".join((path + (k,)))] = v
    return result
