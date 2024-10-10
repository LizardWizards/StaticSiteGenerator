import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_props_added_correctly(self):
        expected = "<a href=\"https://www.google.com\">Click me!</a>"
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        actual = node.to_html()
        self.assertEqual(expected, actual)

    def test_noprops_renders_correctly(self):
        expected = "<p>This is a paragraph of text.</p>"
        node =  LeafNode("p", "This is a paragraph of text.")
        actual = node.to_html()
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()