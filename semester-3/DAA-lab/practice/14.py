import heapq

class Node:
    def __init__(self, char, prob):
        self.char = char
        self.prob = prob
        self.left = None
        self.right = None

    # Define comparison methods for heapq
    def __lt__(self, other):
        return self.prob < other.prob

def construct_huffman_tree(chars, probs):
    # Create priority queue (min-heap)
    pq = []
    for char, prob in zip(chars, probs):
        heapq.heappush(pq, Node(char, prob))

    # Build Huffman tree
    while len(pq) > 1:
        left = heapq.heappop(pq)
        right = heapq.heappop(pq)
        internal_node = Node(None, left.prob + right.prob)
        internal_node.left = left
        internal_node.right = right
        heapq.heappush(pq, internal_node)

    # Return root of Huffman tree
    return pq[0]

def encode_huffman_tree(root, code=''):
    codes = {}
    if root:
        if not root.left and not root.right:  # Leaf node
            codes[root.char] = code
        else:
            codes.update(encode_huffman_tree(root.left, code + '0'))
            codes.update(encode_huffman_tree(root.right, code + '1'))
    return codes

# Given data
chars = ['m', 'n', 'o', 'p', 'q', 'r']
probs = [0.5, 0.1, 0.4, 0.3, 0.2, 0.5]

# Construct Huffman tree
huffman_tree = construct_huffman_tree(chars, probs)

# Encode characters using Huffman codes
huffman_codes = encode_huffman_tree(huffman_tree)

# Print Huffman codes
print("Huffman Codes:")
for char, code in huffman_codes.items():
    print(char + ":", code)
