class Jigfyp:
    def __init__(self, db, delimiter = b'!', highest_character = b'~'):
        self.db = db
        for name in ['delimiter', 'highest_character']:
            if not isinstance(name, bytes):
                raise TypeError('%s must be bytes.' % name)
            setattr(self, name, locals()[name])

    def put(db, key, value):
        '''
        Save a record to the level database.

        :param leveldb.LevelDB db: The levelDB instance to query...'
        :type key: tuple of bytes
        :param key: The key
        :param bytes value: The value
        '''

    def read_one(db, key):
        '''
        Read one record from the level database.

        :param leveldb.LevelDB db: The levelDB instance to query...'
        :type key: tuple of bytes
        :param key: The key
        :rtype: tuple containing two bytes elements
        :returns: The raw key and value corresponding to that key
        '''

    def read_many(db, key_prefix):
        '''
        Read several records from the level database. All records whose keys
        begin with the particular prefix are returned.

        :param leveldb.LevelDB db: The levelDB instance to query...'
        :type key_prefix: tuple of bytes
        :param key_prefix: A left-aligned subset of the key values.
        :rtype: iterable of tuples, each containing two bytes elements
        :returns: Iterable of keys-value pairs
        '''

    def delete_one(db, key):
        '''
        Delete one record from the level database.

        :param leveldb.LevelDB db: The levelDB instance to query...'
        :type key: tuple of bytes
        :param key: The key
        :rtype: None
        :returns: Nothing
        '''

    def delete_many(db, key_prefix):
        '''
        Delete several records from the level database.

        :param leveldb.LevelDB db: The levelDB instance to query...'
        :type key_prefix: tuple of bytes
        :param key_prefix: A left-aligned subset of the key values.
        :rtype: None
        :returns: Nothing
        '''

def _encode_keys(delimiter, highest_character, key, validate = False):
    if validate:
        if len(delimiter) != 1 or len(highest_character) != 1:
            raise ValueError('delimiter and highest_character must both have length 1.')
        def f():
            for x in key:
                if delimiter in x:
                    raise ValueError('%s contains the delimiter (%s)' % (repr(key), repr(delimiter)))
                elif highest_character in x:
                    raise ValueError('%s contains the highest_character (%s)' % (repr(key), repr(highest_character)))
                else:
                    yield x
        _key = f()
    else:
        _key = key

    if len(key) > 0:
        key_from = delimiter.join(_key) + delimiter
        key_to = key_from + highest_character
    else:
        key_from = key_to = None

    return {
        'key_from': key_from,
        'key_to': key_to,
    }
