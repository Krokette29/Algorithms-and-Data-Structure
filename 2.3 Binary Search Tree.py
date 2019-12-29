import random


class NodeBST(object):
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.parent = None
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return "<class NodeBST ({} : {})>".format(self.key, self.value)
    __repr__ = __str__

    def reset(self):
        self.key = None
        self.value = None
        self.parent = None
        self.left_child = None
        self.right_child = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def __str__(self):
        return "<class BinarySearchTree>"
    __repr__ = __str__

    def __compare(self, key=None, method='compare', source=None, print_path=False):
        compare_node = source if source else self.root
        parent_node = None

        while compare_node:
            parent_node = compare_node

            if method == 'search':
                if parent_node.key == key:
                    # when the method is search, compare_node is the result
                    parent_node = parent_node.parent
                    break

            if method == 'compare' or method == 'search':
                compare_node = parent_node.left_child if key <= parent_node.key else parent_node.right_child

            if method == 'min':
                compare_node = parent_node.left_child

            if method == 'max':
                compare_node = parent_node.right_child

            if print_path:
                try:
                    print("({}, {}) -> ({}, {})".format(parent_node.key, parent_node.value,
                                                        compare_node.key, compare_node.value))
                except AttributeError:
                    pass

        return parent_node, compare_node

    def __check_root(self):
        """
        Check whether the tree is empty.

        """
        if not self.root or not self.root.key:
            raise IndexError("The tree is empty!")

    def __check_node(self, node):
        """
        Check whether a node exists.
        Args:
            node: class NodeBST

        """
        if not node or not node.key:
            raise IndexError("Node doesn't exist!")

    def __swap_kv(self, node1, node2):
        """
        Swap key-value pair of two node.

        Args:
            node1: class NodeBST
            node2: class NodeBST

        """
        node1.key, node2.key = node2.key, node1.key
        node1.value, node2.value = node2.value, node1.value

    def rotation(self, key, right_rotation=False):
        """
        Rotate around a certain node.
        Args:
            key: the key of node to be rotated
            right_rotation: True for right rotation, False for left rotation

        """
        parent_node, node = self.__compare(key, method='search')

        # left rotation
        if not right_rotation:
            self.__check_node(node.right_child)

            # update parent
            parent = node.parent
            neighbor = node.right_child
            if node.key <= parent.key:
                parent.left_child = neighbor
            else:
                parent.right_child = node.right_child

            # update node
            node.parent = neighbor
            if neighbor.left_child and neighbor.left_child.key:
                node.right_child = neighbor.left_child

            # update neighbor
            neighbor.parent = parent
            neighbor.left_child = node

        # right rotation
        else:
            self.__check_node(node.left_child)

            # update parent
            parent = node.parent
            neighbor = node.left_child
            if node.key <= parent.key:
                parent.left_child = neighbor
            else:
                parent.right_child = node.right_child

            # update node
            node.parent = neighbor
            if neighbor.right_child and neighbor.right_child.key:
                node.left_child = neighbor.right_child

            # update neighbor
            neighbor.parent = parent
            neighbor.right_child = node

    def insert(self, key, value):
        """
        Insert a key-value pair.

        """
        insert_node = NodeBST(key, value)

        # insert root
        if not self.root or not self.root.key:
            self.root = insert_node

        else:
            # find the position to insert the node
            parent_node, _ = self.__compare(key)
            insert_node.parent = parent_node
            if key <= parent_node.key:
                parent_node.left_child = insert_node
            else:
                parent_node.right_child = insert_node

        print("Insert {} : {}".format(key, value))

    def get_node(self, key, print_path=False):
        """
        Get the node with the given key.
        Args:
            key: the key of the node
            print_path: True for printing the searching path, and vice versa

        Returns:
            search_node: class NodeBST

        """
        self.__check_root()

        parent_node, search_node = self.__compare(key, method='search', print_path=print_path)
        self.__check_node(search_node)

        return search_node

    def search(self, key, print_path=False):
        """
        Search for a certain key. Print the information of the node.
        Args:
            key: the key of the node to be searched
            print_path: True for printing the searching path, and vice versa

        """
        search_node = self.get_node(key, print_path)
        print("ID: {}\nValue: {}".format(search_node.key, search_node.value))

    @property
    def min(self):
        self.__check_root()

        min_node, _ = self.__compare(method='min')
        return min_node if min_node else None

    @property
    def max(self):
        self.__check_root()

        max_node, _ = self.__compare(method='max')
        return max_node if max_node else None

    def get_predecessor(self, key):
        """
        Get the predecessor the of given node.
        Args:
            key: the key of the node to be searched

        Returns:
            pred_node: predecessor of the node, class NodeBST

        """
        self.__check_root()

        parent_node, search_node = self.__compare(key, method='search')
        self.__check_node(search_node)

        # if the node has a left tree
        if search_node.left_child and search_node.left_child:
            pred_node, _ = self.__compare(method='max', source=search_node.left_child)

        # if the node has no left tree
        else:
            while search_node.key < parent_node.key:
                search_node = parent_node
                parent_node = parent_node.parent

                # if it reaches the root, means there is no predecessor
                if not parent_node:
                    return NodeBST(None, None)

            pred_node = parent_node

        return pred_node

    def get_successor(self, key):
        """
        Get the successor the of given node.
        Args:
            key: the key of the node to be searched

        Returns:
            succ_node: successor of the node, class NodeBST

        """
        self.__check_root()

        parent_node, search_node = self.__compare(key, method='search')
        self.__check_node(search_node)

        if search_node.right_child and search_node.right_child.key:
            pred_node, _ = self.__compare(method='min', source=search_node.right_child)
        else:
            while search_node.key > parent_node.key:
                search_node = parent_node
                parent_node = parent_node.parent

                # if it reaches the root, means there is no predecessor
                if not parent_node:
                    return NodeBST(None, None)

            pred_node = parent_node

        return pred_node

    def print_in_order(self, source=None, descending=False):
        """
        Print the key-value pairs in the ascending/descending order of keys.
        Args:
            source: used for recursion, not for users
            descending: True for descending order

        """
        self.__check_root()

        if not source:
            source = self.root
        if not descending:
            if source.left_child and source.left_child.key:
                self.print_in_order(source.left_child)
            print("{} : {}".format(source.key, source.value))
            if source.right_child and source.right_child.key:
                self.print_in_order(source.right_child)
        else:
            if source.right_child and source.right_child.key:
                self.print_in_order(source.right_child)
            print("{} : {}".format(source.key, source.value))
            if source.left_child and source.left_child.key:
                self.print_in_order(source.left_child)

    def delete(self, key):
        """
        Delete a node with the given key.
        Args:
            key: the key of the node to be deleted

        """
        self.__check_root()

        parent_node, search_node = self.__compare(key, method='search')
        self.__check_node(search_node)

        # Case 1: the node has no children nodes
        if (not search_node.left_child) and (not search_node.right_child):
            search_node.reset()

            # if the node has parent, delete the child of the parent
            if parent_node and parent_node.key:
                if key <= parent_node.key:
                    parent_node.left_child = None
                else:
                    parent_node.right_child = None

        # Case 2: the node has only one child node
        elif bool(search_node.left_child) != bool(search_node.right_child):
            child = search_node.left_child if search_node.left_child else search_node.right_child
            if key <= parent_node.key:
                parent_node.left_child = child
            else:
                parent_node.right_child = child

            child.parent = parent_node
            search_node.reset()

        # Case 3: the node has two children nodes
        else:
            pred = self.get_predecessor(key)
            self.__swap_kv(search_node, pred)
            if pred.left_child and pred.left_child.key:
                pred.parent.right_child = pred.left_child
            else:
                pred.parent.right_child = None
            pred.reset()



tree = BinarySearchTree()
random.seed(1)

key_list = [random.randint(1000, 2000) for i in range(10)]
value_list = [random.randint(60, 100) for i in range(10)]

for i in range(10):
    tree.insert(key_list[i], value_list[i])

print('------------------------------------------')
sorted_list = sorted(key_list)
print('max: %s' % max(key_list))
print('min: %s' % min(key_list))
print('sorted array: {}'.format(sorted_list))
print('------------------------------------------')

print("min key: %s" % tree.min.key)
print("max key: %s" % tree.max.key)
print("successor of 1261 is: %s" % tree.get_successor(1261).key)

print('----->')
tree.print_in_order()
print('----->')

print('delete value 1867')
tree.delete(1867)
tree.search(1779, print_path=True)

print('rotate around 1582')
tree.rotation(1582)
tree.search(1507, print_path=True)
