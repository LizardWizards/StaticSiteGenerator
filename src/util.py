from parentnode import ParentNode
from leafnode import LeafNode

# tag, props
text_to_html = {
    "text_type_text" : (None, None),
    "text_type_bold" : ("b", None),
    "text_type_italic" : ("i", None),
    "text_type_code" : ("code", None),
    "text_type_link" : ("a", {"url": "href"}),
    "text_type_image" : ("img", {"url": "src", "text": "alt"}),
}

# converts a TextNode to an HTMLNode (LeafNode)
def text_node_to_html_node(text_node):
    newNode, tag = None, None
    type = text_node.text_type

    if type in text_to_html:
        tag = text_to_html[type][0]
    else:
        raise TypeError("Invalid text type")

    props = text_to_html[type][1]
    newProps = {}
    if props != None:
        if "url" in props:
            newProps[props["url"]] = text_node.url
        if "text" in props:
            newProps[props["text"]] = text_node.text

    match type:
        case "text_type_text" | "text_type_bold" | "text_type_italic" | "text_type_code":
            newNode = LeafNode(tag, text_node.text, None)
        case "text_type_link":
            newNode = LeafNode(tag, text_node.text, newProps)
        case "text_type_image":
            newNode = LeafNode(tag, "", newProps)

    return newNode