import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("text1", "bold")
        node2 = TextNode("text2", "bold")
        self.assertNotEqual(node, node2)

    def test_not_eq_type(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italics")
        self.assertNotEqual(node, node2)

    def test_url_defaults_None(self):
        node = TextNode("This is a text node", "bold")
        expectedUrl = None
        self.assertEqual(node.url, expectedUrl)

    def test_printed(self):
        expectedOutput = "TextNode(TestText, TestType, TestURL)"
        node = TextNode("TestText", "TestType", "TestURL")
        output = node.__repr__()
        self.assertEqual(output, expectedOutput)

if __name__ == "__main__":
    unittest.main()