def flatten(dictionary):
    """Given a dictionary where the keys are strings and the values are strings
    or dictionaries, flatten the dictionary, but save the structures in the
    keys. The result is a dictionary without the nested dictionaries. The keys
    contain paths that contain the parent keys from the original dictionary.
    The keys in the path are separated by a "/". If a value is an empty
    dictionary, then it is replaced by an empty string ("").

    @param dictionary: the dictionary to flatten"""

    stack = [((), dictionary)]
    result = {}
    #import pdb; pdb.set_trace()
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


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({"name": {
                        "first": "One",
                        "last": "Drone"},
                    "job": "scout",
                    "recent": {},
                    "additional": {
                        "place": {
                            "zone": "1",
                            "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}
