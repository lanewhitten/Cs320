class Node():
    def __init__(self, key):
        self.key = key
        self.values = []
        self.left = None
        self.right = None
    
    def __len__(self):
        size = len(self.values)
        if self.left != None:
            size += len(self.left)
        if self.right != None:
            size += len(self.right)
        return size

    def lookup(self, key):
        if key == self.key:
            return self.values
        elif key < self.key and self.left != None:
            return self.left.lookup(key)
        elif key > self.key and self.right != None:
            return self.right.lookup(key)
        else:
            return None
    
#    def count_missing_rates(self):
 #       missing_rates_count = self.values.count(-1)
#
 #       if self.left:
  #          missing_rates_count += self.left.count_missing_rates()
   ##        missing_rates_count += self.right.count_missing_rates()
#
 #       return missing_rates_count
class BST():
    def __init__(self):
        self.root = None

    def add(self, key, val):
        if self.root == None:
            self.root = Node(key)  #is this right?

        curr = self.root
        while True:
            if key < curr.key:
                # go left
                if curr.left == None:
                    curr.left = Node(key)
                curr = curr.left
            elif key > curr.key:
                 # go right
                if curr.right == None:
                    curr.right = Node(key)
                curr = curr.right
            else:
                # found it!
                assert curr.key == key
                break

        curr.values.append(val)
   
    def __dump(self, node):
        if node == None:
            return
        self.__dump(node.right)            # 1
        print(node.key, ":", node.values)  # 2
        self.__dump(node.left)             # 3

    def dump(self):
        self.__dump(self.root)
    
    def height(self):
        def calcHeight(node):
            if node is None:
                return 0
            else:
                left_height = calcHeight(node.left)
                right_height = calcHeight(node.right)
                return max(left_height, right_height) + 1

        return calcHeight(self.root)