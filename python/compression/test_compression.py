from compression import Compression

def test_it_initializes():
    compression = Compression()

    assert isinstance(compression, Compression)

def test_it_compresses_1():
    compression = Compression()
    input_list = ["a","a","b","b","c","c","c"]

    assert compression.compress(input_list) == 6

def test_it_compresses_1():
    compression = Compression()
    input_list = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

    assert compression.compress(input_list) == 4