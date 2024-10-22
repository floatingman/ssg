import re
from htmlnode import HTMLNode
from textnode import TextNode
from inline_markdown import text_to_textnodes
from htmlnode import LeafNode

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

def markdown_to_blocks(markdown):
    blocks = []
    current_block = []

    for line in markdown.split('\n'):
        if line.strip() == '':
            if current_block:
                blocks.append('\n'.join(current_block))
                current_block = []
        else:
            current_block.append(line)

    if current_block:
        blocks.append('\n'.join(current_block))

    return blocks

def block_to_block_type(block):
    lines = block.split('\n')
    
    # Check for heading
    if block.startswith(('#')):
        # Ensure there's a space after the '#' characters and the line starts with 1-6 '#' characters
        heading_match = re.match(r'^#{1,6} ', block)
        if heading_match:
            return block_type_heading
    
    # Check for code block
    if block.startswith('```') and block.endswith('```'):
        return block_type_code
    
    # Check for quote block
    if all(line.startswith('>') for line in lines):
        return block_type_quote
    
    # Check for unordered list
    if all(re.match(r'^\s*[\*\-]\s', line) for line in lines):
        return block_type_ulist
    
    # Check for ordered list
    if all(line.strip().split('.')[0].isdigit() for line in lines):
        numbers = [int(line.strip().split('.')[0]) for line in lines]
        if numbers == list(range(1, len(numbers) + 1)):
            return block_type_olist
    
    # If none of the above conditions are met, it's a paragraph
    return block_type_paragraph

def text_to_children(text):
    textnodes = text_to_textnodes(text)
    return [LeafNode(node.text_type, node.text) for node in textnodes]

def create_heading_node(block):
    level = len(block.split()[0])  # Count the number of '#' symbols
    content = block.split(' ', 1)[1]  # Get the heading text
    return HTMLNode(f"h{level}", None, text_to_children(content))

def create_code_node(block):
    code_content = '\n'.join(block.split('\n')[1:-1])  # Remove the first and last lines (```)
    return HTMLNode("pre", None, [HTMLNode("code", None, [LeafNode(None, code_content)])])

def create_quote_node(block):
    content = '\n'.join(line.lstrip('> ').strip() for line in block.split('\n'))
    return HTMLNode("blockquote", None, text_to_children(content))

def create_list_node(block, list_type):
    items = [line.lstrip('*-1234567890. ').strip() for line in block.split('\n')]
    list_items = [HTMLNode("li", None, text_to_children(item)) for item in items]
    return HTMLNode(list_type, None, list_items)

def create_paragraph_node(block):
    return HTMLNode("p", None, text_to_children(block))

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == "heading":
            children.append(create_heading_node(block))
        elif block_type == "code":
            children.append(create_code_node(block))
        elif block_type == "quote":
            children.append(create_quote_node(block))
        elif block_type == "unordered_list":
            children.append(create_list_node(block, "ul"))
        elif block_type == "ordered_list":
            children.append(create_list_node(block, "ol"))
        else:  # paragraph
            children.append(create_paragraph_node(block))
    
    return HTMLNode("div", None, children)
