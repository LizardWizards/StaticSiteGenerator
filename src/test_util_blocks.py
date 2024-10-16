import unittest

from textnode import TextNode
from htmlnode import HTMLNode
from parentnode import ParentNode
import util_blocks

class TestUtil(unittest.TestCase):
    # ----------- markdown_to_blocks() ----------- #
    def test_markdown_to_blocks(self):
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]
        
        text = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        
        actual = util_blocks.markdown_to_blocks(text)

        self.assertEqual(expected, actual)

    def test_markdown_to_blocks_strips_whitespace(self):
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "All of the text has some whitespace"
        ]
        
        text = " # This is a heading \n\n This is a paragraph of text. It has some **bold** and *italic* words inside of it.   \n\n  All of the text has some whitespace  "
        
        actual = util_blocks.markdown_to_blocks(text)

        self.assertEqual(expected, actual)

    def test_markdown_to_blocks_removes_empty_blocks(self):
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
        ]
        
        text = "\n# This is a heading \n\n\n \n This is a paragraph of text. It has some **bold** and *italic* words inside of it.   \n\n  "
        
        actual = util_blocks.markdown_to_blocks(text)

        self.assertEqual(expected, actual)

    # ----------- block_to_block_type() ----------- #
    def test_block_to_blocktype_paragraph(self):
        expected = "paragraph"
        
        text = "This is just a regular old paragraph"
        
        actual = util_blocks.block_to_block_type(text)

        self.assertEqual(expected, actual)

    def test_block_to_blocktype_heading(self):
        
        testCases = [("# heading 1", "heading"), 
                    ("## heading 2", "heading"), 
                    ("### heading 3", "heading"), 
                    ("#### heading 4", "heading"), 
                    ("##### heading 5", "heading"),
                    ("###### heading 6", "heading"), 
                    ("####### NOT A HEADING", "paragraph")]

        for text, expected in testCases:
            actual = util_blocks.block_to_block_type(text)
            self.assertEqual(expected, actual)

    def test_block_to_blocktype_code(self):
        expected = "code"
        
        text = "'''A code block'''"
        
        actual = util_blocks.block_to_block_type(text)

        self.assertEqual(expected, actual)

    def test_block_to_blocktype_quote(self):
        expected = "quote"
        
        text = "> This is a quote\n>with multiple lines"
        
        actual = util_blocks.block_to_block_type(text)

        self.assertEqual(expected, actual)

    def test_block_to_blocktype_unordered_list(self):
        expected = "unordered_list"
        
        text = "- This is an\n- unordered list\n* with multiple lines"
        
        actual = util_blocks.block_to_block_type(text)

        self.assertEqual(expected, actual)

    def test_block_to_blocktype_ordered_list(self):
        expected = "ordered_list"
        
        text = "1. This is an\n2. ordered list\n3. with multiple lines"
        
        actual = util_blocks.block_to_block_type(text)

        self.assertEqual(expected, actual)

    # ----------- markdown_to_html_node() ----------- #
    def test_markdown_to_html_node_heading(self):
        expected = HTMLNode("div", children=[    
            HTMLNode("h1", "h1 Heading 8-)", None, None),
            HTMLNode("h2", "h2 Heading", None, None),
            HTMLNode("h3", "h3 Heading", None, None),
            HTMLNode("h4", "h4 Heading", None, None),
            HTMLNode("h5", "h5 Heading", None, None),
            HTMLNode("h6", "h6 Heading", None, None),
        ])

        text = "# h1 Heading 8-)\n\n## h2 Heading\n\n### h3 Heading\n\n#### h4 Heading\n\n##### h5 Heading\n\n###### h6 Heading"

        actual = util_blocks.markdown_to_html_node(text)

        self.assertEqual(expected, actual)

    def test_markdown_to_html_node_quote(self):
        expected = HTMLNode("div", children=[    
            HTMLNode("blockquote", "Here's a quote More of the quote", None, None),
        ])

        text = "> Here's a quote\n> More of the quote"

        actual = util_blocks.markdown_to_html_node(text)

        self.assertEqual(expected, actual)

    def test_markdown_to_html_node_ordred_list(self):
        expected = HTMLNode("div", children=[    
            HTMLNode("ol", children=[
                HTMLNode("li", "Lorem ipsum dolor sit amet", None, None),
                HTMLNode("li", "Consectetur adipiscing elit", None, None),
                HTMLNode("li", "Integer molestie lorem at massa", None, None)
            ])
        ])

        text = "1. Lorem ipsum dolor sit amet\n2. Consectetur adipiscing elit\n3. Integer molestie lorem at massa"

        actual = util_blocks.markdown_to_html_node(text)

        self.assertEqual(expected, actual)

    def test_markdown_to_html_node_unordred_list(self):
        expected = HTMLNode("div", children=[    
            HTMLNode("ul", children=[
                HTMLNode("li", "something", None, None),
                HTMLNode("li", "something else", None, None),
                HTMLNode("li", "another thing", None, None)
            ])
        ])

        text = "- something\n- something else\n* another thing"

        actual = util_blocks.markdown_to_html_node(text)

        self.assertEqual(expected, actual)

    def test_markdown_to_html_node_code(self):
        expected = HTMLNode("div", children=[    
            HTMLNode("pre", children=[
                HTMLNode("code", "here's a\nmulti line\ncode block", None, None),
            ])
        ])
        text = "'''\nhere's a\nmulti line\ncode block\n'''"

        actual = util_blocks.markdown_to_html_node(text)

        self.assertEqual(expected, actual)

    def test_markdown_to_html_node_paragraph(self):
        expected = HTMLNode("div", None, children=[    
            HTMLNode("p", "here's some text", None, None), 
        ])

        text = "here's some text"

        actual = util_blocks.markdown_to_html_node(text)
        
        self.assertEqual(expected, actual)

    def test_markdown_to_html_node_image_link(self):
        expected = HTMLNode("div", children=[    
            HTMLNode("p", None, [
                HTMLNode("img", "", None, {'src': 'https://octodex.github.com/images/minion.png', 'alt': 'Minion'}),
                HTMLNode("img", "", None, {'src': 'https://octodex.github.com/images/stormtroopocat.jpg', 'alt': 'Stormtroopocat'})
            ]), 
            HTMLNode("p", None, [
                HTMLNode("a", "link text", None, {'href': 'https://github.com/LizardWizards/'}),
            ]),           
        ])

        text = "![Minion](https://octodex.github.com/images/minion.png)\n![Stormtroopocat](https://octodex.github.com/images/stormtroopocat.jpg)\n\n[link text](https://github.com/LizardWizards/)"

        '''
        HTMLNode(div, None, [
            HTMLNode(p, None, [
                HTMLNode(img, , None, {'src': 'https://octodex.github.com/images/minion.png', 'alt': 'Minion'}), 
                HTMLNode(img, , None, {'src': 'https://octodex.github.com/images/stormtroopocat.jpg', 'alt': 'Stormtroopocat'})
            , None), 
            HTMLNode(p, None, [
                HTMLNode(a, link text, None, {'href': 'https://github.com/LizardWizards/'})
            ], None)], None)
        '''
        actual = util_blocks.markdown_to_html_node(text)

        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()