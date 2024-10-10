class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    # returns True if all of the properties of two TextNode objects are equal
    def __eq__(self, nodeB):
        if self.text == nodeB.text and self.text_type == nodeB.text_type and self.url == nodeB.url:
            return True
        return False
    
    # returns a string representation of the TextNode object
    def __repr__(self):
        stringRepresentation = f"TextNode({self.text}, {self.text_type}, {self.url})"
        return stringRepresentation