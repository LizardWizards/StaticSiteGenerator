import unittest

from textnode import TextNode
import util

class TestUtil(unittest.TestCase):
    def test_text(self):
        expected = "Text Test"

        textNode = TextNode("Text Test", "text_type_text", None)
        new_node = util.text_node_to_html_node(textNode)
        actual = new_node.to_html()

        self.assertEqual(expected, actual)

    def test_bold(self):
        expected = "<b>Bold Test</b>"

        textNode = TextNode("Bold Test", "text_type_bold", None)
        new_node = util.text_node_to_html_node(textNode)
        actual = new_node.to_html()

        self.assertEqual(expected, actual)

    def test_italic(self):
        expected = "<i>Italic Test</i>"

        textNode = TextNode("Italic Test", "text_type_italic", None)
        new_node = util.text_node_to_html_node(textNode)
        actual = new_node.to_html()

        self.assertEqual(expected, actual)

    def test_code(self):
        expected = "<code>Code Test</code>"

        textNode = TextNode("Code Test", "text_type_code", None)
        new_node = util.text_node_to_html_node(textNode)
        actual = new_node.to_html()

        self.assertEqual(expected, actual)

    def test_link(self):
        expected = "<a href=\"https://google.com\">Link alt text!</a>"

        textNode = TextNode("Link alt text!", "text_type_link", "https://google.com")
        new_node = util.text_node_to_html_node(textNode)
        actual = new_node.to_html()

        self.assertEqual(expected, actual)

    def test_image(self):
        expected = "<img src=\"https://creazilla.com/media/png-image/15594597/cat\" alt=\"Image alt text!\"></img>"

        textNode = TextNode("Image alt text!", "text_type_image", "https://creazilla.com/media/png-image/15594597/cat")
        new_node = util.text_node_to_html_node(textNode)
        actual = new_node.to_html()

        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()