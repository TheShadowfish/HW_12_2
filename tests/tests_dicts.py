from utils import dicts
import pytest


@pytest.mark.parametrize('collection, key, expected', [
    ({"vcs": "mercurial"}, 'vcs', 'mercurial'),
    ({}, 'any_key', 'test'),
    ({"vcs": "mercurial", "any_key": "pressed_yet"}, 'any_key', 'pressed_yet'),
    ({"vcs": "mercurial", "any_key": "pressed_yet"}, 'any_vcs', 'test')
])
def test_get_val(collection, key, expected):
    assert dicts.get_val(collection, key, "test") == expected
