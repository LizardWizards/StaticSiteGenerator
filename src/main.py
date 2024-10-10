from textnode import TextNode

def main():
    print("Here")
    dummyTextNode = TextNode("test node", "bold", "https://google.com")
    print("Here2")
    print(dummyTextNode.__repr__())

main()