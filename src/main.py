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
    
    '''text = "./content/markdown.txt"
    with open(text) as file:
        contents = file.read()
        util_blocks.markdown_to_html_node(contents)

        file.close()
        '''
    text = "# h1 Heading 8-)\n\n## h2 Heading\n\n### h3 Heading\n\n#### h4 Heading\n\n##### h5 Heading\n\n###### h6 Heading"

    actual = util_blocks.markdown_to_html_node(text)
    print(actual)

main()