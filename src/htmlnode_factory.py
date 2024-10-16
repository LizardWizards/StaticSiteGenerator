from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
import util_inline

import re

class HTMLNodeFactory:

    def create_node(type, block):
        match type:
            case "paragraph":
                textNodes = util_inline.text_to_textnodes(block)
                htmlNodes = []
                for textNode in textNodes:
                    if textNode.text != "\n" and textNode.text != "":
                        htmlNodes.append(util_inline.text_node_to_html_node(textNode))
                if len(htmlNodes) > 1 or (len(htmlNodes) == 1 and htmlNodes[0].tag != None):
                    newNode = ParentNode("p", children=htmlNodes)
                else:
                    newNode = LeafNode("p", value=block)
            case "heading":
                matches = re.findall(r"^#{1,6} ", block, re.M)
                headingType = len(matches[0]) - 1
                newNode = LeafNode(f"h{headingType}", block[len(matches[0]):])
            case "code":
                code = block[3:-3]
                newNode = ParentNode("pre", children=[LeafNode("code", code.strip())])
            case "quote":
                textWithoutSymbols = block.replace("\n>", "")
                textWithoutSymbols = textWithoutSymbols.replace(">", "")
                newNode = LeafNode("blockquote", textWithoutSymbols.strip())
            case "unordered_list":
                lines = block.splitlines()

                listItems = []                
                for line in lines:    
                    listItemNodes = util_inline.text_to_textnodes(line[2:])
                    listItemChildren = []

                    for item in listItemNodes:
                        if item.text != "\n" and item.text != "":
                            listItemChildren.append(util_inline.text_node_to_html_node(item))

                    if len(listItemChildren) > 1:
                        listItems.append(ParentNode("li", children=listItemChildren))
                    else:
                        listItems.append(LeafNode("li", value=listItemChildren[0].value))

                newNode = ParentNode("ul", children=listItems)
                print("RETURNING________________")
                print(newNode)
            case "ordered_list":
                lines = block.splitlines()
                listItems = []
                for line in lines:
                    content = line[3:]
                    listItems.append(LeafNode("li", content))
                newNode = ParentNode("ol", children=listItems)
        return newNode
    
