import unittest

from textnode import TextNode
import util

class TestUtil(unittest.TestCase):
    # ----------- text_node_to_html_node() ----------- #
    def test_node_to_html_text(self):
        expected = "Text Test"

        textNode = TextNode("Text Test", "text_type_text", None)
        new_node = util.text_node_to_html_node(textNode)
        actual = new_node.to_html()

        self.assertEqual(expected, actual)

    def test_node_to_html_bold(self):
        expected = "<b>Bold Test</b>"

        textNode = TextNode("Bold Test", "text_type_bold", None)
        new_node = util.text_node_to_html_node(textNode)
        actual = new_node.to_html()

        self.assertEqual(expected, actual)

    def test_node_to_html_italic(self):
        expected = "<i>Italic Test</i>"

        textNode = TextNode("Italic Test", "text_type_italic", None)
        new_node = util.text_node_to_html_node(textNode)
        actual = new_node.to_html()

        self.assertEqual(expected, actual)

    def test_node_to_html_code(self):
        expected = "<code>Code Test</code>"

        textNode = TextNode("Code Test", "text_type_code", None)
        new_node = util.text_node_to_html_node(textNode)
        actual = new_node.to_html()

        self.assertEqual(expected, actual)

    def test_node_to_html_link(self):
        expected = "<a href=\"https://google.com\">Link alt text!</a>"

        textNode = TextNode("Link alt text!", "text_type_link", "https://google.com")
        new_node = util.text_node_to_html_node(textNode)
        actual = new_node.to_html()

        self.assertEqual(expected, actual)

    def test_node_to_html_image(self):
        expected = "<img src=\"https://creazilla.com/media/png-image/15594597/cat\" alt=\"Image alt text!\"></img>"

        textNode = TextNode("Image alt text!", "text_type_image", "https://creazilla.com/media/png-image/15594597/cat")
        new_node = util.text_node_to_html_node(textNode)
        actual = new_node.to_html()

        self.assertEqual(expected, actual)

    # ----------- split_nodes_delimiter() ----------- #
    def test_split_node_bold(self):
        expected = [
            TextNode("This is text with a ", "text_type_text", None), 
            TextNode("code block", "text_type_code", None), 
            TextNode(" word", "text_type_text", None)
            ]

        node = TextNode("This is text with a `code block` word", "text_type_text")
        actual = util.split_nodes_delimiter([node], "`", "text_type_code")
        self.assertEqual(expected, actual)

    def test_split_node_italic(self):
        expected = [
            TextNode("This is text with an ", "text_type_text", None), 
            TextNode("italic block", "text_type_italic", None), 
            TextNode(" word", "text_type_text", None)
            ]

        node = TextNode("This is text with an *italic block* word", "text_type_text")
        actual = util.split_nodes_delimiter([node], "*", "text_type_italic")
        self.assertEqual(expected, actual)

    def test_split_node_bold(self):
        expected = [
            TextNode("This is text with a ", "text_type_italic", None), 
            TextNode("bold block", "text_type_bold", None), 
            TextNode(" word", "text_type_italic", None)
            ]

        node = TextNode("This is text with a **bold block** word", "text_type_italic")
        actual = util.split_nodes_delimiter([node], "**", "text_type_bold")
        self.assertEqual(expected, actual)

    # ----------- extract_markdown_images() ----------- #

    def test_extract_markdown_images(self):
        expected = [('snoopy', 'https://upload.wikimedia.org/wikipedia/en/5/53/Snoopy_Peanuts.png'), ('kirby', 'https://kirby.nintendo.com/assets/img/about/characters-kirby.png')]

        text = "This is text with a ![snoopy](https://upload.wikimedia.org/wikipedia/en/5/53/Snoopy_Peanuts.png) and ![kirby](https://kirby.nintendo.com/assets/img/about/characters-kirby.png) and a [link!](https://www.wikipedia.org/)"
        actual = util.extract_markdown_images(text)
        self.assertEqual(expected, actual)

    def test_extract_markdown_images_empty(self):
        expected = []

        text = "This is text with no images"
        actual = util.extract_markdown_images(text)
        self.assertEqual(expected, actual)

    # ----------- extract_markdown_links() ----------- #

    def test_extract_markdown_links(self):
        expected = [('wikipedia', 'https://www.wikipedia.org/'), ('bulbapedia', 'https://bulbapedia.bulbagarden.net/wiki/Main_Page')]

        text = "This is text with an image ![snoopy](https://upload.wikimedia.org/wikipedia/en/5/53/Snoopy_Peanuts.png) and links to [wikipedia](https://www.wikipedia.org/) and [bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Main_Page)!"
        actual = util.extract_markdown_links(text)
        self.assertEqual(expected, actual)

    def test_extract_markdown_links_empty(self):
        expected = []

        text = "This is text with no links"
        actual = util.extract_markdown_links(text)
        self.assertEqual(expected, actual)

    # ----------- split_nodes_image() ----------- #
    def test_splits_images(self):
        expected = [
            TextNode("This is text with a ", "text_type_text", None),
            TextNode("snoopy", "text_type_image", "https://test.png"),
            TextNode(" and a [link!](https://www.wikipedia.org/)", "text_type_text", None),
            TextNode("This is text with a ", "text_type_text", None),
            TextNode("snoopy2", "text_type_image", "https://test2.png"),
            TextNode(" and ", "text_type_text", None),
            TextNode("kirby", "text_type_image", "https://test2.png"),
            TextNode(", yay!", "text_type_text", None)]

        node = TextNode(
            "This is text with a ![snoopy](https://test.png) and a [link!](https://www.wikipedia.org/)",
            "text_type_text"
        )
        node2 = TextNode(
            "This is text with a ![snoopy2](https://test2.png) and ![kirby](https://test2.png), yay!",
            "text_type_text"
        )
        actual = util.split_nodes_image([node, node2])
        self.assertEqual(expected, actual)

    def test_splits_images_ending_image(self):
        expected = [
            TextNode("This is text ending with a ", "text_type_text", None),
            TextNode("snoopy", "text_type_image", "https://test.png"),
        ]

        node = TextNode(
            "This is text ending with a ![snoopy](https://test.png)",
            "text_type_text"
        )
        actual = util.split_nodes_image([node])
        self.assertEqual(expected, actual)

    def test_returns_original_if_no_images(self):
        expected = [
            TextNode("This is text with no images", "text_type_text")
        ]

        node = TextNode(
            "This is text with no images",
            "text_type_text"
        )
        actual = util.split_nodes_image([node])
        self.assertEqual(expected, actual)

    def test_doesnt_append_empty_text_image(self):
        expected = [
            TextNode("This is text with a ", "text_type_text", None),
            TextNode("snoopy", "text_type_image", "https://test.png"),
        ]

        node = TextNode(
            "This is text with a ![snoopy](https://test.png)",
            "text_type_text"
        )
        node2 = TextNode(
            "",
            "text_type_text"
        )

        actual = util.split_nodes_image([node, node2])
        self.assertEqual(expected, actual)

    # ----------- split_nodes_link() ----------- #
    def test_splits_links(self):
        expected = [
            TextNode("This is text with a link ", "text_type_text", None),
            TextNode("to boot dev", "text_type_link", "https://www.boot.dev"),
            TextNode(" and ", "text_type_text", None),
            TextNode("to youtube", "text_type_link", "https://www.youtube.com/@bootdotdev"),
            TextNode(" and a ![snoopy](https://test.png) image", "text_type_text", None)
        ]

        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) and a ![snoopy](https://test.png) image",
            "text_type_text",
        )

        actual = util.split_nodes_link([node])
        self.assertEqual(expected, actual)

    def test_splits_link_ending_link(self):
        expected = [
            TextNode("This is text ending with a ", "text_type_text", None),
            TextNode("link", "text_type_link", "https://www.boot.dev")
        ]

        node = TextNode(
            "This is text ending with a [link](https://www.boot.dev)",
            "text_type_text"
        )
        actual = util.split_nodes_link([node])
        self.assertEqual(expected, actual)

    def test_returns_original_if_no_links(self):
        expected = [
            TextNode("This is text with no links", "text_type_text")
        ]

        node = TextNode(
            "This is text with no links",
            "text_type_text"
        )
        actual = util.split_nodes_link([node])
        self.assertEqual(expected, actual)

    def test_doesnt_append_empty_text_link(self):
        expected = [
            TextNode("This is text with a ", "text_type_text", None),
            TextNode("snoopy link", "text_type_link", "https://en.wikipedia.org/wiki/Snoopy")
        ]

        node = TextNode(
            "This is text with a [snoopy link](https://en.wikipedia.org/wiki/Snoopy)",
            "text_type_text"
        )
        node2 = TextNode(
            "",
            "text_type_text"
        )

        actual = util.split_nodes_link([node, node2])

        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()