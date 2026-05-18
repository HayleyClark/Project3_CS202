import unittest
from proj3 import huffman_encoding


class TestMyHuffmanEncoding(unittest.TestCase):

    def test_single_character(self):
        encoded, decoded, codes = huffman_encoding("aaaa")
        self.assertEqual(decoded, "aaaa")
        self.assertEqual(codes, {"a": "0"})
        self.assertEqual(encoded, "0000")

    def test_two_characters(self):
        encoded, decoded, codes = huffman_encoding("ABBA")
        self.assertEqual(decoded, "ABBA")
        self.assertEqual(codes, {"A": "0", "B": "1"})
        self.assertEqual(encoded, "0110")

    def test_repeated_word(self):
        encoded, decoded, codes = huffman_encoding("mississippi")
        self.assertEqual(decoded, "mississippi")
        self.assertEqual(set(codes.keys()), set("misp"))

    def test_spaces(self):
        encoded, decoded, codes = huffman_encoding("a b a")
        self.assertEqual(decoded, "a b a")
        self.assertIn(" ", codes)

    def test_empty_string(self):
        encoded, decoded, codes = huffman_encoding("")
        self.assertEqual(decoded, "")
        self.assertEqual(codes, {})
        self.assertEqual(encoded, "")
        

if __name__ == "__main__":
    unittest.main()
