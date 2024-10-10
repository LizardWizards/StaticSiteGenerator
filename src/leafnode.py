from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self,tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, props=props)
    
    def to_html(self):
        nodeString = ""
        if not self.value:
            raise ValueError
        
        if self.tag == None:
            return str(self.value)
        
        props = ""
        if self.props != None:
            props = self.props_to_html()

        nodeString = f"<{self.tag}{props}>{self.value}</{self.tag}>"
        return nodeString