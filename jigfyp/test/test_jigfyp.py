import pytest

from ..jigfyp import _encode_keys, Jigfyp

key_mapping = [
    ((b'abc', b'def'), {'key_from': b'abc!def!', 'key_to': b'abc!def!~'}),
]

@pytest.mark.parametrize('key_prefix, keys', key_mapping)
def test_encode_keys_specific(key_prefix, keys):
    delimiter = b'!'
    highest_character = b'~'
    assert _encode_keys(delimiter, highest_character, key_prefix) == keys
