from leafnode import LeafNode
from textnode import TextNode
import re

# tag, props
text_to_html = {
    "text_type_text" : (None, None),
    "text_type_bold" : ("b", None),
    "text_type_italic" : ("i", None),
    "text_type_code" : ("code", None),
    "text_type_link" : ("a", {"url": "href"}),
    "text_type_image" : ("img", {"url": "src", "text": "alt"}),
}


# Converts a raw string of markdown-flavored text into a list of TextNode objects
def text_to_textnodes(text):
   
    first_node = TextNode(text, "text_type_text")
    result = split_nodes_image([first_node])
    result = split_nodes_link(result)
    result = split_nodes_delimiter(result, "`", "text_type_code")
    result = split_nodes_delimiter(result,"**", "text_type_bold")
    result = split_nodes_delimiter(result, "*", "text_type_italic")

    return result


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

'''
Takes a list of "old nodes", a delimiter, and a text type. 
Returns a new list of nodes, where any "text" type nodes in the input list are split into multiple nodes based on the syntax.

node = TextNode("This is text with a `code block` word", text_type_text)

returns:
[
    TextNode("This is text with a ", text_type_text),
    TextNode("code block", text_type_code),
    TextNode(" word", text_type_text),
]
'''
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []

    for oldNode in old_nodes:
        oldTextType = oldNode.text_type
        oldURL = oldNode.url
        # split it based on the delimiter
        chunksOfText = oldNode.text.split(delimiter)

        # add every other one to a original vs new text type
        old = True

        for chunk in chunksOfText:
            if old:
                result.append(TextNode(chunk, oldTextType, oldURL))
            else:
                result.append(TextNode(chunk, text_type, oldURL))
            old = not old
    return result

# takes a list of old nodes, and splits out the image nodes
def split_nodes_image(old_nodes):
    result = []

    for oldNode in old_nodes:
        # "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        originalText = oldNode.text
        if originalText == "":
            continue

        images = extract_markdown_images(originalText)
        #[(alt text, url), (alt text, url), ...]
        remaining_text = originalText
        textSections = []

        if len(images) == 0:
            result.append(oldNode)
            continue

        while len(images) > 0:
            image = images.pop(0) #('to boot dev', 'https://www.boot.dev')
           
            alt = image[0] # 'to boot dev'
            url = image[1] # 'https://www.boot.dev'
            
            textSections = remaining_text.split(f"![{alt}]({url})", 1) # ['This is text with a link ', ' and ![to youtube](https://www.youtube.com/@bootdotdev)']
            pre_image_node = TextNode(textSections[0], oldNode.text_type) # Node('This is text with a link ' , original text type)
            image_node = TextNode(alt, "text_type_image", url) # Node('to boot dev', text_type_image, 'https://www.boot.dev')
            result.append(pre_image_node) 
            result.append(image_node)

            remaining_text = textSections[1] # ' and ![to youtube](https://www.youtube.com/@bootdotdev)'

        if len(textSections) >= 2 and textSections[1]:
            result.append(TextNode(textSections[1], oldNode.text_type))

    return result

def split_nodes_link(old_nodes):
    result = []

    for oldNode in old_nodes:
        originalText = oldNode.text
        if originalText == "":
            continue
        

        links = extract_markdown_links(originalText)
        remaining_text = originalText
        textSections = []

        if len(links) == 0:
            result.append(oldNode)
            continue

        while len(links) > 0:
            link = links.pop(0)
           
            alt = link[0] 
            url = link[1] 

            textSections = remaining_text.split(f"[{alt}]({url})", 1)

            pre_link_node = TextNode(textSections[0], oldNode.text_type)
            link_node = TextNode(alt, "text_type_link", url) 
            result.append(pre_link_node) 
            result.append(link_node)

            if len(textSections) >= 2 and textSections[1]:
                remaining_text = textSections[1] 

        if len(textSections) >= 2 and textSections[1]:
            result.append(TextNode(textSections[1], oldNode.text_type))

    return result

'''
takes raw markdown text and returns a list of tuples containing the alt text and URL of any markdown images

"This is text with a ![snoopy](https://upload.wikimedia.org/wikipedia/en/5/53/Snoopy_Peanuts.png)"
returns:
[('snoopy', 'https://upload.wikimedia.org/wikipedia/en/5/53/Snoopy_Peanuts.png')]
'''
def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

'''
takes raw markdown text and returns a list of tuples containing the alt text and URL of any markdown links
'''
def extract_markdown_links(text):
    startingLink = re.findall(r"^\[(.*?)\]\((.*?)\)", text)
    matches = re.findall(r"[^!]\[(.*?)\]\((.*?)\)", text)

    return startingLink + matches
    