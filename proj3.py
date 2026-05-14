from __future__ import annotations
from dataclasses import dataclass, field

@dataclass(order=True, frozen=True)
class Node:
    freq: int
    char: str
    left: Node | None = None
    right: Node | None  = None

    def __str__(self):
        return f"Node: {self.char}, Freq: {self.freq}"

@dataclass(frozen=True)
class MinHeap:
    data: list[Node] = field(default_factory=list)


def heapify_up(heap: MinHeap, index: int) -> MinHeap:
    if index == 0:
        return heap
    parent = (index - 1) // 2

    if heap.data[index] < heap.data[parent]:
        new_data = heap.data[:]
        temp = new_data[index]
        new_data[index] = new_data[parent]
        new_data[parent] = temp
        return heapify_up(MinHeap(new_data), parent)
    return heap

def insert(heap: MinHeap, element: Node) -> MinHeap:
    new_data = heap.data + [element]
    new_heap = MinHeap(new_data)

    return heapify_up(new_heap, len(new_data) - 1)

def heapify_down(heap: MinHeap, index: int) -> MinHeap:
    ata = heap.data[:]
    left = 2 * index + 1
    right = 2 * index + 2
    size = len(data)

    if left >= size:
        return heap
    smallest = left

    if right < size and data[right] < data[left]:
        smallest = right

    if data[smallest] < data[index]:
        data[index], data[smallest] = data[smallest], data[index]
        return heapify_down(MinHeap(data), smallest)
    return heap


def extract_min(heap: MinHeap) -> tuple[MinHeap, Node]:
    data = heap.data
    if len(data) == 0:
        return MinHeap([]), None

    if len(data) == 1:
        return MinHeap([]), data[0]
    min_node = data[0]
    new_data = [data[-1]] + data[1:-1]
    new_heap = MinHeap(new_data)
    fixed_heap = heapify_down(new_heap, 0)

    return fixed_heap, min_node


        
def count_frequency(s: str)-> dict[str,int]:
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
    

def create_priority_queue(frequency: dict[str, int]) -> MinHeap:
    heap = MinHeap([])
    for char, freq in frequency.items():
        node = Node(freq, char)
        heap = insert(heap, node)

    return heap



def build_tree(priority_queue: MinHeap) -> Node:
    pass




def generate_codes(node: Node | None, prefix="", code: dict | None =None)-> dict:
    if code is None:
        code = {}  
    pass


def encode(s: str, codes: dict)-> str:
    pass


def decode(encoded_string: str, root: Node):
    pass

def huffman_encoding(s:str):
    #Do Not Change this function
    frequency = count_frequency(s)
    pq = create_priority_queue(frequency)
    root = build_tree_from_queue(pq)
    codes = generate_codes(root)
    encoded_string = encode(s, codes)
    decoded_string = decode(encoded_string,root)
    return encoded_string, decoded_string, codes

