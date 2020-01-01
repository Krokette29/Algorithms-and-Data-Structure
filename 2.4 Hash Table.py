import binascii


class HashNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTableUsingChaining(object):
    def __init__(self, length, key_type="int"):
        self.hash_table = [HashNode(None, None) for i in range(length)]
        self.key_type = key_type

        # n for hash function mod
        self.hash_function_n = self.__max_prime_num(length)

    def __max_prime_num(self, length):
        """
        Calculate the largest prime number smaller than the length.
        Args:
            length: length of the hash table

        Returns:
            value: largest prim number smaller than the length

        """
        for value in reversed(range(1, length+1)):
            prime = True
            for i in range(2, value):
                if value % i == 0:
                    prime = False
                    break
            if prime:
                return value

        raise IndexError("No prime number found! Try another length!")

    def __hash_function(self, key, n):
        """
        Hash function using mod.
        Args:
            key: integer key to hash
            n: mod n

        Returns:
            index of the key after hashing

        """
        return key % self.hash_function_n

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

    def insert(self, key, value):
        """
        Insert a key-value pair.
        Args:
            key: integer key
            value: any value

        """
        self.__key_type_check(key)
        key_int = self.__str_to_int(key) if self.key_type == "string" else key

        index = self.__hash_function(key_int, self.hash_function_n)

        if not self.hash_table[index].key:
            self.hash_table[index].key = key
            self.hash_table[index].value = value

        # if the node has already existed, use a chain
        else:
            insert_node = HashNode(key, value)
            insert_node.next = self.hash_table[index]
            self.hash_table[index] = insert_node

    def search(self, key):
        """
        Search for a certain key.

        """
        self.__key_type_check(key)
        key_int = self.__str_to_int(key) if self.key_type == "string" else key

        index = self.__hash_function(key_int, self.hash_function_n)
        node = self.hash_table[index]

        if not node.key:
            print("No key found!")
        else:
            while node.key:
                if node.key == key:
                    print("Key: {}, Value: {}".format(node.key, node.value))
                    break
                else:
                    node = node.next
                    if not node:
                        print("No key found!")
                        break


class HashTableUsingOpenAddressing(object):
    def __init__(self, length,  key_type="int", mode='l'):
        self.hash_table = [HashNode(None, None) for i in range(length)]
        self.length = length
        self.key_type = key_type
        self.hash_function_n = self.__max_prime_num(length)
        self.hash_function_n2 = 5

        if mode == 'l':
            self.hash_mode = "LinearProbing"
        elif mode == 'd':
            self.hash_mode = "DoubleHashing"
        else:
            raise ValueError("Unknown hash table type!")

    def __max_prime_num(self, length):
        """
        Calculate the largest prime number smaller than the length.
        Args:
            length: length of the hash table

        Returns:
            value: largest prim number smaller than the length

        """
        for value in reversed(range(1, length + 1)):
            prime = True
            for i in range(2, value):
                if value % i == 0:
                    prime = False
                    break
            if prime:
                return value

        raise IndexError("No prime number found! Try another length!")

    def __hash_function(self, key, n):
        """
        Hash function using mod.
        Args:
            key: integer key to hash
            n: mod n

        Returns:
            index of the key after hashing

        """
        return key % n

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

    def insert(self, key, value):
        """
        Insert a key-value pair.
        Args:
            key: integer key
            value: any value

        """
        self.__key_type_check(key)
        key_int = self.__str_to_int(key) if self.key_type == "string" else key

        index = self.__hash_function(key_int, self.hash_function_n)

        if not self.hash_table[index].key:
            self.hash_table[index].key = key
            self.hash_table[index].value = value

        # if the node has already existed, use a linear probing or double hashing
        else:
            pointer = index
            node = self.hash_table[pointer]

            if self.hash_mode == "LinearProbing":
                step = 1
            # double hashing
            else:
                step = self.__hash_function(key, self.hash_function_n2)

            while self.hash_table[pointer].key:
                pointer += step
                if pointer >= self.length:
                    pointer -= self.length
                if pointer == index:
                    raise IndexError("Hash table out of range!")

            self.hash_table[pointer].key = key
            self.hash_table[pointer].value = value

    def search(self, key):
        self.__key_type_check(key)
        key_int = self.__str_to_int(key) if self.key_type == "string" else key

        index = self.__hash_function(key_int, self.hash_function_n)

        if not self.hash_table[index].key:
            print("Key not found!")
        else:
            pointer = index
            node = self.hash_table[pointer]

            if self.hash_mode == "LinearProbing":
                step = 1
            # double hashing
            else:
                step = self.__hash_function(key, self.hash_function_n2)

            while node.key:
                pointer += step
                if pointer >= self.length:
                    pointer -= self.length
                if self.hash_table[pointer].key == key:
                    print("Key: {}, Value: {}".format(self.hash_table[pointer].key, self.hash_table[pointer].value))
                    break
                if pointer == index:
                    print("Key not found!")
                    break


def main():
    #############################
    # hash table for integer
    print("-> hash table for integer")

    hash_table = HashTableUsingChaining(15)
    print("hash function using {}".format(hash_table.hash_function_n))

    # insert chaining test
    hash_table.insert(1, 2341)
    hash_table.insert(14, 1244)

    # search test
    hash_table.search(1)
    hash_table.search(14)
    print('------------------------')

    #############################
    # hash table for string
    print("-> hash table for string")

    hash_table_str = HashTableUsingChaining(15, key_type="string")
    hash_table_str.insert('abc', 123)
    hash_table_str.insert('cdf', 'sfb')
    hash_table_str.search('kfc')
    hash_table_str.search('abc')
    hash_table_str.search('cdf')
    print('------------------------')

    #############################
    # hash table for linear probing
    print("-> hash table for linear probing")

    hash_table_linear_probing = HashTableUsingOpenAddressing(15)
    hash_table_linear_probing.insert(3, 'abc')

    # 16 % 13 = 3, so next index: 3 + 1 = 4
    hash_table_linear_probing.insert(16, 'cdf')
    hash_table_linear_probing.search(14)
    hash_table_linear_probing.search(16)
    print("index 3: {}".format(hash_table_linear_probing.hash_table[3].key))
    print("index 4: {}".format(hash_table_linear_probing.hash_table[4].key))
    print('------------------------')

    #############################
    # hash table for double hashing
    print("-> hash table for double hashing")

    hash_table_double_hashing = HashTableUsingOpenAddressing(15, mode='d')
    hash_table_double_hashing.insert(4, 'abc')

    # 17 % 13 = 4, and 17 % 5 = 2, so next index: 4 + 2 = 6
    hash_table_double_hashing.insert(17, 'cdf')
    hash_table_double_hashing.search(14)
    hash_table_double_hashing.search(16)
    print("index 3: {}".format(hash_table_double_hashing.hash_table[4].key))
    print("index 6: {}".format(hash_table_double_hashing.hash_table[6].key))


if __name__ == "__main__":
    main()
