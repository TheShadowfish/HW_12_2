from utils import arrs
import pytest


def test_get(array_fixture):
    assert arrs.get(array_fixture, 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get(array_fixture, -1, "test") == "test"
    assert arrs.get(array_fixture, 4, "test") == 'test'


@pytest.mark.parametrize('array, start, end, expected', [
    ([1, 2, 3], 1, 3, [2, 3]),
    ([], 0, 100, []),
    ([1, 2, 3, 4], -2, None, [3, 4]),
    ([1, 2, 3, 4], None, 2, [1, 2])
])
def test_slice(array, start, end, expected):
    assert arrs.my_slice(array, start, end) == expected


