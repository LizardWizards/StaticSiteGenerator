from textnode import TextNode
from parentnode import ParentNode
from leafnode import LeafNode
import util_inline
import util_blocks

def main():
    #dummyTextNode = TextNode("Text Bold Test", "text_type_bold")
    #print(dummyTextNode.__repr__())

    #new_node = util.text_node_to_html_node(dummyTextNode)
    #print(new_node.to_html())

    
    text = "1. This is an\n2. ordered list\n3. with multiple lines"
    print(util_blocks.is_ordered_list(text))

main()