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