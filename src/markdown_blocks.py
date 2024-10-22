import re

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
