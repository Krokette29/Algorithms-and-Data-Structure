import binascii


class BloomFilter(object):
    def __init__(self, num_bits=8, key_type="int"):
        self.bloom_array = [False] * num_bits
        self.key_type = key_type

    def __key_type_check(self, key):
        """
        Check the type of keys.

        """
        if self.key_type == "string":
            if not isinstance(key, str):
                raise ValueError("Key type error!")

        elif self.key_type == "int":
            if not isinstance(key, int):
                raise ValueError("Key type error!")

        else:
            raise ValueError("Unknown key type!")

    def __str_to_int(self, key: str):
        """
        Transform from string to integer, in order to use the hash function.

        """
        string = binascii.b2a_hex(key.encode('utf-8'))
        return int(string, 16)

    def __hash_functions(self, key):
        """
        Use total five hash functions to get five indexes, where the entry in the array should be set True.

        """
        indexes = [key % 2, key % 3, key % 5, key % 7]
        return indexes

    def insert(self, key):
        """
        Insert a key into the bloom filter.

        """
        self.__key_type_check(key)
        key_int = self.__str_to_int(key) if self.key_type == "string" else key

        indexes = self.__hash_functions(key_int)
        for index in indexes:
            self.bloom_array[index] = True

    def has(self, key):
        """
        Check whether the bloom filter has the certain key.

        """
        self.__key_type_check(key)
        key_int = self.__str_to_int(key) if self.key_type == "string" else key

        indexes = self.__hash_functions(key_int)
        for index in indexes:
            if not self.bloom_array[index]:
                return False

        return True

    def search(self, key):
        if self.has(key):
            print("Key in the bloom filter!")
        else:
            print("Key not found in the bloom filter!")


def password_checker(bloom_filter, key):
    """
    A simple example of bloom filter's usage - password checker.

    """
    if bloom_filter.has(key):
        print("Too simple password!")
    else:
        print("Good password!")


def main():
    # for example, bloom filter can be used as a password checker
    # first we add two simple passwords into bloom filter
    bloom_filter = BloomFilter(key_type="string")
    bloom_filter.insert('abcde')
    bloom_filter.insert('12345')

    # check passwords
    password1 = 'abcde'
    password2 = 'goodPassword'
    password_checker(bloom_filter, password1)
    password_checker(bloom_filter, password2)

    # but it may have some false positive errors
    password3 = 'goodPassword357'
    password_checker(bloom_filter, password3)


if __name__ == '__main__':
    main()
