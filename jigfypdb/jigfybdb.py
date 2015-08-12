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
