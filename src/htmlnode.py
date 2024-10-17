class HTMLNode:
    '''
    tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
    value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
    children - A list of HTMLNode objects representing the children of this node
    props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
    '''
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    # returns True if all of the properties of two TextNode objects are equal
    def __eq__(self, nodeB):
        if self.tag == nodeB.tag and self.value == nodeB.value and self.props == nodeB.props:
            if self.children is not None:
                for i in range(len(self.children)):
                    if self.children[i] != nodeB.children[i]:
                        return False
            return True
        return False
    
    def __repr__(self):
        stringRepresentation = f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
        return stringRepresentation
    
    # implemented by child classes to render themselves in html
    def to_html(self):
        raise NotImplementedError
    
    # returns a string that represents the HTML attributes of the node
    def props_to_html(self):
        propString = ""
        if self.props:
            for prop in self.props:
                propString += f" {prop}=\"{self.props[prop]}\""
        return propString