import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def encode(node, prefix, huffCodes):
    if node is None:
        return
    if node.left is None and node.right is None:
        huffCodes[node.char] = prefix
    encode(node.left, prefix + '0', huffCodes)
    encode(node.right, prefix + '1', huffCodes)

def huffmanCoding(s):
    freq = {char: s.count(char) for char in set(s)}
    heap = [Node(char, freq) for char, freq in freq.items()]
    heapq.heapify(heap)
    while len(heap) != 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    root = heap[0]
    huffCodes = {}
    encode(root, '', huffCodes)
    return huffCodes

s = 'Grace'
huffCodes = huffmanCoding(s)
print('Huffman Codes:')
for char, code in huffCodes.items():
    print(f'{char}: {code}')
print('Encoded String:')
print(''.join(huffCodes[char] for char in s))
