import unittest

from textnode import TextNode
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

if __name__ == "__main__":
    unittest.main()