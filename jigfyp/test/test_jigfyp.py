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
                       key_prefix = list_of(str),
                       max_length = 5, # So errors are easy to read
                       ncalls = 3, encoding = 'ascii')
def test_encode_keys_random(delimiter, highest_character, key_prefix):
    kp = tuple(x.replace(delimiter, '').replace(highest_character, '').encode('ascii') for x in key_prefix)

    d = delimiter.encode('ascii')
    h = highest_character.encode('ascii')
    if len(d) == 1 and len(h) == 1:
        keys = _encode_keys(d, h, kp)
        assert set(keys) == {'key_from', 'key_to'}
        assert isinstance(keys, dict)
        if len(key_prefix) == 0:
            for name in ['key_from', 'key_to']:
                assert keys[name] == None
        else:
            assert keys['key_from'].endswith(d)
            assert keys['key_to'].endswith(d + h)
            for name in ['key_from', 'key_to']:
                assert keys[name].count(d) == len(key_prefix)

            assert len(keys['key_from']) + 1 == len(keys['key_to'])
    else:
        with pytest.raises(ValueError):
            _encode_keys(d, h, kp)
