from textnode import TextNode
from parentnode import ParentNode
from leafnode import LeafNode
import util

def main():
    dummyTextNode = TextNode("Text Bold Test", "text_type_bold")
    print(dummyTextNode.__repr__())

    new_node = util.text_node_to_html_node(dummyTextNode)
    print(new_node.to_html())



main()