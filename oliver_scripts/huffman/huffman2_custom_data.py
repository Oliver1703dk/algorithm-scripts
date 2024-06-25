import heapq
from collections import defaultdict, Counter
import graphviz


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Defining comparator methods for the priority queue
    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(frequencies):
    heap = [HuffmanNode(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)

        merged = HuffmanNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2

        heapq.heappush(heap, merged)

    return heap[0]


def build_huffman_codes(node, code="", huffman_code={}):
    if node is None:
        return

    if node.char is not None:
        huffman_code[node.char] = code

    build_huffman_codes(node.left, code + "0", huffman_code)
    build_huffman_codes(node.right, code + "1", huffman_code)

    return huffman_code


def huffman_encoding(data, frequencies):
    if not data:
        return "", {}

    root = build_huffman_tree(frequencies)
    huffman_code = build_huffman_codes(root)

    encoded_data = "".join(huffman_code[char] for char in data)
    return encoded_data, huffman_code, root


def calculate_total_bits(data, huffman_code):
    total_bits = sum(len(huffman_code[char]) * freq for char, freq in Counter(data).items())
    return total_bits


def calculate_bits_for_char(char, huffman_code):
    return len(huffman_code.get(char, ""))


def huffman_decoding(encoded_data, root):
    decoded_data = []
    current_node = root
    for bit in encoded_data:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_data.append(current_node.char)
            current_node = root

    return "".join(decoded_data)


def visualize_huffman_tree(node):
    def add_edges(graph, node, prefix=""):
        if node.left:
            graph.edge(prefix, prefix + "0", label="0")
            add_edges(graph, node.left, prefix + "0")
        if node.right:
            graph.edge(prefix, prefix + "1", label="1")
            add_edges(graph, node.right, prefix + "1")
        if node.char is not None:
            graph.node(prefix, label=f'{node.char}\n{node.freq}', shape='circle')

    graph = graphviz.Digraph(format='png')
    graph.node('', label=f'{node.freq}', shape='circle')
    add_edges(graph, node)
    return graph


# Example usage
if __name__ == "__main__":
    frequencies = {'b': 90, 'c': 15, 'd': 40, 'f': 30, 'g': 125, 'h': 35}
    data = ''.join(char * freq for char, freq in frequencies.items())

    encoded_data, huffman_code, root = huffman_encoding(data, frequencies)
    print(f"Encoded data: {encoded_data}")
    print(f"Huffman Codes: {huffman_code}")

    total_bits = calculate_total_bits(data, huffman_code)
    print(f"Total bits required: {total_bits}")

    char = 'e'
    bits_for_char = calculate_bits_for_char(char, huffman_code)
    print(f"Bits required for character '{char}': {bits_for_char}")

    decoded_data = huffman_decoding(encoded_data, root)
    print(f"Decoded data: {decoded_data}")

    # Visualize the Huffman Tree
    graph = visualize_huffman_tree(root)
    graph.render('huffman_tree')
    print("Huffman tree visualized and saved as 'huffman_tree.png'")
