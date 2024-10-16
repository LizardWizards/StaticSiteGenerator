from leafnode import LeafNode
from textnode import TextNode
from htmlnode import HTMLNode
from parentnode import ParentNode
from htmlnode_factory import HTMLNodeFactory
import re

# converts a full markdown document into a single HTMLNode.
# That single HTMLNode contains many child HTMLNode objects representing the nested elements.
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    childNodes = []
    for block in blocks:
        type = block_to_block_type(block)
        if block != "" and block != "\n":
            newNode = HTMLNodeFactory.create_node(type, block)
            childNodes.append(newNode)
    
    divNode = ParentNode("div", children=childNodes)

    return divNode


# separates lines of markdown into blocks
def markdown_to_blocks(markdown):
    blocks = []
    chunks = markdown.split("\n\n")
    for chunk in chunks:
        if chunk.strip() != "\n" and chunk.strip() != "":
            blocks.append(chunk.strip())

    return blocks

# returns the type that a block is
def block_to_block_type(block):
    type = "paragraph"
    if is_heading(block):
        type = "heading"
    elif is_code(block):
        type = "code"
    elif is_quote(block):
        type = "quote"
    elif is_unordered_list(block):
        type = "unordered_list"
    elif is_ordered_list(block):
        type = "ordered_list"
    return type

def is_heading(block):
    matches = re.findall(r"^#{1,6} ", block, re.M)
    if matches:
        return True
    return False

def is_code(block):
    if len(block) >= 7 and block[0:3] == "'''" and block[-3:] == "'''":
        return True
    return False

def is_quote(block):
    lines = block.splitlines()
    for line in lines:
        if line[0] != ">":
            return False
    return True

def is_unordered_list(block):
    lines = block.splitlines()
    for line in lines:
        if line[0:2] != "- " and line[0:2] != "* ":
            return False
    return True

def is_ordered_list(block):
    lines = block.splitlines()
    number = 1
    for line in lines:
        if line[0:3] != f"{number}. ":
            return False
        number += 1
    return True