import heapq
from collections import defaultdict, Counter


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


def huffman_encoding(data):
    if not data:
        return "", {}

    frequency = Counter(data)
    root = build_huffman_tree(frequency)
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


# Example usage
if __name__ == "__main__":
    data = "this is an example for huffman encoding"
    print(f"Original data: {data}")

    encoded_data, huffman_code, root = huffman_encoding(data)
    print(f"Encoded data: {encoded_data}")
    print(f"Huffman Codes: {huffman_code}")

    total_bits = calculate_total_bits(data, huffman_code)
    print(f"Total bits required: {total_bits}")

    char = 'e'
    bits_for_char = calculate_bits_for_char(char, huffman_code)
    print(f"Bits required for character '{char}': {bits_for_char}")

    decoded_data = huffman_decoding(encoded_data, root)
    print(f"Decoded data: {decoded_data}")



