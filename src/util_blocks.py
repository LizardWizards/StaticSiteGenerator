from leafnode import LeafNode
from textnode import TextNode
import re

def markdown_to_blocks(markdown):
    blocks = []
    chunks = markdown.split("\n\n")
    for chunk in chunks:
        if chunk.strip() != "\n" and chunk.strip() != "":
            blocks.append(chunk.strip())

    return blocks

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