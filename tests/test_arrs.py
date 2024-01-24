from utils import arrs
import pytest


@pytest.mark.parametrize('array, index, expected', [
    ([1, 2, 3], 1, 2),
    ([], 0, "test"),
    ([1, 2, 3, 4], -1, 'test')
])
def test_get(array, index, expected):
    assert arrs.get(array, index, "test") == expected


@pytest.mark.parametrize('array, start, end, expected', [
    ([1, 2, 3], 1, 3, [2, 3]),
    ([], 0, 100, []),
    ([1, 2, 3, 4], -2, None, [3, 4])
])
def test_slice(array, start, end, expected):
    assert arrs.my_slice(array, start, end) == expected


