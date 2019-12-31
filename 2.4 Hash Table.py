class HashNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTableUsingChaining(object):
    def __init__(self, length):
        self.hash_table = [HashNode(None, None) for i in range(length)]

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

    def __hash_function(self, key: int, n):
        """
        Hash function using mod.
        Args:
            key: integer key to hash
            n: mod n

        Returns:
            index of the key after hashing

        """
        return key % self.hash_function_n

    def insert(self, key: int, value):
        """
        Insert a key-value pair.
        Args:
            key: integer key
            value: any value

        """
        index = self.__hash_function(key, self.hash_function_n)

        if not self.hash_table[index].key:
            self.hash_table[index].key = key
            self.hash_table[index].value = value

        # if the node has already existed, use a chain
        else:
            insert_node = HashNode(key, value)
            insert_node.next = self.hash_table[index]
            self.hash_table[index] = insert_node

    def search(self, key: int):
        """
        Search for a certain key.

        """
        index = self.__hash_function(key, self.hash_function_n)

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


def main():
    hash_table = HashTableUsingChaining(15)
    print("hash function using {}".format(hash_table.hash_function_n))

    # insert chaining test
    hash_table.insert(1, 2341)
    hash_table.insert(14, 1244)

    # search test
    hash_table.search(1)
    hash_table.search(14)


if __name__ == "__main__":
    main()
