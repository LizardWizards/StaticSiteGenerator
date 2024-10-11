import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):

    def test_no_children(self):

        node = ParentNode("p")
        with self.assertRaises(ValueError) as context:
            node.to_html()

        self.assertTrue('No children provided' in str(context.exception))

    def test_no_value(self):

        node = ParentNode(children = [
                LeafNode("b", "Bold text")
            ])
        with self.assertRaises(ValueError) as context:
            node.to_html()

        self.assertTrue('No tag provided' in str(context.exception))

    def test_children_only(self):
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"

        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        actual = node.to_html()
        self.assertEqual(expected, actual)

    def test_parent_node_inception(self):
        expected = "<p><b>Bold text</b><b>Bold text</b><b>Bold text</b><p><i>Italic text</i><p>Normal text</p><i>Italic text</i></p></p>"
        
        parent0 = ParentNode(
            "p",
            [
                LeafNode(None, "Normal text"),
            ],
        )

        parent1 = ParentNode(
            "p",
            [
                LeafNode("i", "Italic text"),
                parent0,
                LeafNode("i", "Italic text"),
            ],
        )

        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode("b", "Bold text"),
                LeafNode("b", "Bold text"),
                parent1,
            ],
        )

        actual = node.to_html()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()