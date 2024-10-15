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
                    htmlNodes.append(util_inline.text_node_to_html_node(textNode))

                if len(htmlNodes) > 1:
                    newNode = ParentNode("p", children=htmlNodes)
                else:
                    newNode = LeafNode("p", htmlNodes[0])
            case "heading":
                matches = re.findall(r"^#{1,6} ", block, re.M)
                headingType = len(matches[0]) - 1
                newNode = LeafNode(f"h{headingType}", block[len(matches[0]):])
            case "code":
                newNode = ParentNode("pre", children=[LeafNode("code", block)])
            case "quote":
                textWithoutSymbols = block.replace("\n>", "")
                textWithoutSymbols = textWithoutSymbols.replace(">", "")
                newNode = LeafNode("blockquote", textWithoutSymbols.strip())
            case "unordered_list":
                lines = block.splitlines()
                listItems = []
                for line in lines:
                    content = line[2:]
                    listItems.append(LeafNode("li", content))
                newNode = ParentNode("ul", children=listItems)
            case "ordered_list":
                lines = block.splitlines()
                listItems = []
                for line in lines:
                    content = line[3:]
                    listItems.append(LeafNode("li", content))
                newNode = ParentNode("ol", children=listItems)
        return newNode