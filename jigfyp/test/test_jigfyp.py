import pytest
from pytest import list_of

from ..jigfyp import _encode_keys, Jigfyp

key_mapping = [
    ((b'abc', b'def'), {'key_from': b'abc!def!', 'key_to': b'abc!def!~'}),
]

@pytest.mark.parametrize('key_prefix, keys', key_mapping)
def test_encode_keys_specific(key_prefix, keys):
    delimiter = b'!'
    highest_character = b'~'
    assert _encode_keys(delimiter, highest_character, key_prefix) == keys

@pytest.mark.randomize(delimiter = str, highest_character = str, 
                       key_prefix = list_of(str), ncalls = 3)
def test_encode_keys_random(delimiter, highest_character, key_prefix):
    d = delimiter.encode('ascii')
    h = highest_character.encode('ascii')
    keys = _encode_keys(d, h, tuple(x.encode('ascii') for x in key_prefix))
    assert set(keys) == {'key_from', 'key_to'}
    assert isinstance(keys, dict)
    assert keys['key_from'].endswith(d)
    assert keys['key_to'].endswith(d + h)
    for name in ['key_from', 'key_to']:
        assert keys[name].count(d) == len(key_prefix)
