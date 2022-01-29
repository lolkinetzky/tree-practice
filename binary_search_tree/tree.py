class TreeNode:
    def __init__(self, key, val = None):
        if val == None:
            val = key

        self.key = key
        self.value = val
        self.left = None
        self.right = None
    

class Tree:
    def __init__(self):
        self.root = None

    # Time Complexity: 
    # Space Complexity: 
    def add(self, key, value = None):
        if self.root == None:
            self.root = TreeNode(key, value)
        else:
            self._add(self.root, key, value)

    def _add(self, current_node, key, value):
        if current_node == None:
            return TreeNode(key, value)

        if key <= current_node.key:
            current_node.left = self._add(current_node.left, key, value)
        else:
            current_node.right = self._add(current_node.right, key, value)
        return current_node

    
    # Time Complexity:
    # Space Complexity: 
    def find(self, key):
        if self.root == None:
            return None
        current = self.root
        while current:
            if current.key == key:
                return current.value
            elif key > current.key:
                current = current.right
            else:
                current = current.left
        return None

    
    # Time Complexity: 
    # Space Complexity: 
    def inorder(self):
        values =[]
        
        if self.root == None:
            return values

        return self.in_order(self.root, values)

    def in_order(self, node, values):
        if node == None:
            return 

        self.in_order(node.left, values)
        values.append({
            'key': node.key,
            'value': node.value
        })
        self.in_order(node.right, values)

        return values

    
    # Time Complexity:
    # Space Complexity: 
    def preorder(self):
        values = []

        if self.root == None:
            return values

        return self.pre_order(self.root, values)

    def pre_order(self, node, values):
        if node == None:
            return

        values.append({
            'key': node.key,
            'value': node.value
        })
        self.pre_order(node.left, values)
        self.pre_order(node.right, values)
        
        return values

    
    # Time Complexity:
    # Space Complexity: 
    def postorder(self):
        values = []

        if self.root == None:
            return values

        return self.post_order(self.root, values)

    def post_order(self, node, values):
        if node == None:
            return 

        self.post_order(node.left, values)
        self.post_order(node.right, values)
        values.append({
            'key': node.key,
            'value': node.value
        })

        return values

    
    # Time Complexity:
    # Space Complexity: 
    def height(self):
        if self.root == None:
            return 0

        return self._height(self.root)

    def _height(self, node):
        if node == None:
            return 0

        l = self._height(node.left)
        r = self._height(node.right)

        return (1 + max(l, r))

    
#   # Optional Method
#   # Time Complexity:
#   # Space Complexity:
    def bfs(self):
        values = []
        queue = []
        if self.root:
            queue.append(self.root)

        while len(queue) > 0:
            current_node = queue.pop(0)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
            
            values.append({
                "key": current_node.key,
                "value": current_node.value,
            })
        return values

#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
