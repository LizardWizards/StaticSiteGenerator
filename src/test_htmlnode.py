import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        expected = " href=\"https://www.google.com\""
        node = HTMLNode("a", "test link", [], {"href": "https://www.google.com"})
        actual = node.props_to_html()
        self.assertEqual(expected, actual)

    def test_no_tag_renders_as_raw_text(self):
        expected = " href=\"https://www.google.com\""
        node = HTMLNode(value="test value", children=[], props={"href": "https://www.google.com"})
        actual = node.props_to_html()
        self.assertEqual(expected, actual)

    def test_no_value_assumed_has_children(self):
        expected = " href=\"https://www.google.com\""
        node = HTMLNode(tag="test tag", children=[], props={"href": "https://www.google.com"})
        actual = node.props_to_html()
        self.assertEqual(expected, actual)

    def test_no_children_assumed_has_value(self):
        expected = " href=\"https://www.google.com\""
        node = HTMLNode(tag="test tag", value="test value", props={"href": "https://www.google.com"})
        actual = node.props_to_html()
        self.assertEqual(expected, actual)

    def test_no_props_assumed_has_no_attributes(self):
        expected = ""
        node = HTMLNode("test tag", "test value", [])
        actual = node.props_to_html()
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()