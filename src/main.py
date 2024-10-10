from textnode import TextNode
from leafnode import LeafNode

def main():
    dummyTextNode = TextNode("test node", "bold", "https://google.com")
    print(dummyTextNode.__repr__())

main()