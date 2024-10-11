from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("No tag provided")
        
        if self.children == None:
            raise ValueError("No children provided")
        
        '''
        add the tag

        for each child node:
            get the child nodes' html version
            add it to our string
        
        
        add the closing tag
        '''

        tag = f"<{self.tag}>"
        
        for child in self.children:
            tag += child.to_html()

        tag += f"</{self.tag}>"
        print(tag)

        
        return tag