import pytest

from checkio.deprecated.the_flat_dictionary import flatten


class TestFlatDictionary:

    def test_simple_case(self):
        example = {"key": "value"}
        expected = {"key": "value"}
        assert flatten(example) == expected

    def test_nested(self):
        nested = {
            "key": {
                "deeper": {
                    "more": {
                        "enough": "value"
                    }
                }
            }
        }
        expected = {"key/deeper/more/enough": "value"}
        assert flatten(nested) == expected

    def test_empty_value(self):
        empty = {"empty": {}}
        expected = {"empty": ""}
        assert flatten(empty) == expected

    def test_multiple_nesting_levels(self):
        unflatten = {
            "name": {
                "first": "One",
                "last": "Drone"},
                "job": "scout",
                "recent": {},
                "additional": {
                    "place": {
                        "zone": "1",
                        "cell": "2"
                    }
                }
        }
        expected = {
            "name/first": "One",
            "name/last": "Drone",
            "job": "scout",
            "recent": "",
            "additional/place/zone": "1",
            "additional/place/cell": "2"
        }
        assert flatten(unflatten) == expected
