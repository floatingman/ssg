import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type, extract_title

class TestMarkdownToBlocks(unittest.TestCase):

    def test_single_block(self):
        markdown = "This is a single block of text."
        expected = ["This is a single block of text."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_multiple_blocks(self):
        markdown = "First block\n\nSecond block\n\nThird block"
        expected = ["First block", "Second block", "Third block"]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_empty_input(self):
        markdown = ""
        expected = []
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_only_newlines(self):
        markdown = "\n\n\n"
        expected = []
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_mixed_content(self):
        markdown = "# Heading\n\nParagraph with **bold** and *italic*.\n\n* List item 1\n* List item 2"
        expected = [
            "# Heading",
            "Paragraph with **bold** and *italic*.",
            "* List item 1\n* List item 2"
        ]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_code_block(self):
        markdown = "Here's some code:\n\n```python\ndef hello():\n    print('Hello, world!')\n```"
        expected = [
            "Here's some code:",
            "```python\ndef hello():\n    print('Hello, world!')\n```"
        ]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_trailing_newlines(self):
        markdown = "First block\n\nSecond block\n\n"
        expected = ["First block", "Second block"]
        self.assertEqual(markdown_to_blocks(markdown), expected)

class TestBlockToBlockType(unittest.TestCase):

    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading 1"), "heading")
        self.assertEqual(block_to_block_type("## Heading 2"), "heading")
        self.assertEqual(block_to_block_type("###### Heading 6"), "heading")
        self.assertEqual(block_to_block_type("####### Not a heading"), "paragraph")

    def test_code_block(self):
        self.assertEqual(block_to_block_type("```\ncode here\n```"), "code")
        self.assertEqual(block_to_block_type("```python\ndef function():\n    pass\n```"), "code")
        self.assertEqual(block_to_block_type("```\nMulti-line\ncode block\n```"), "code")

    def test_quote(self):
        self.assertEqual(block_to_block_type("> This is a quote"), "quote")
        self.assertEqual(block_to_block_type("> Multi-line\n> quote block"), "quote")
        self.assertEqual(block_to_block_type("Not a > quote"), "paragraph")

    def test_unordered_list(self):
        self.assertEqual(block_to_block_type("* Item 1\n* Item 2"), "unordered_list")
        self.assertEqual(block_to_block_type("- Item 1\n- Item 2"), "unordered_list")
        self.assertEqual(block_to_block_type("* Mixed\n- List items"), "unordered_list")
        self.assertEqual(block_to_block_type("*Not a list item"), "paragraph")

    def test_ordered_list(self):
        self.assertEqual(block_to_block_type("1. First item\n2. Second item"), "ordered_list")
        self.assertEqual(block_to_block_type("1. First\n2. Second\n3. Third"), "ordered_list")
        self.assertEqual(block_to_block_type("1. First\n3. Third"), "paragraph")
        self.assertEqual(block_to_block_type("1. First\n2. Second\n2. Second again"), "paragraph")

    def test_paragraph(self):
        self.assertEqual(block_to_block_type("This is a normal paragraph."), "paragraph")
        self.assertEqual(block_to_block_type("Multi-line\nparagraph\nblock"), "paragraph")
        self.assertEqual(block_to_block_type("Paragraph with **bold** and *italic*."), "paragraph")

    def test_edge_cases(self):
        self.assertEqual(block_to_block_type(""), "paragraph")
        self.assertEqual(block_to_block_type("  "), "paragraph")
        self.assertEqual(block_to_block_type("1. Not an ordered list\nBecause this line isn't numbered"), "paragraph")
        self.assertEqual(block_to_block_type("* Not an unordered list\nBecause this line doesn't start with *"), "paragraph")


class TestExtractTitle(unittest.TestCase):

    def test_simple_title(self):
        markdown = "# Hello"
        self.assertEqual(extract_title(markdown), "Hello")

    def test_title_with_spaces(self):
        markdown = "#    Title with spaces    "
        self.assertEqual(extract_title(markdown), "Title with spaces")

    def test_title_with_other_content(self):
        markdown = "# Main Title\n\nSome content\n## Subtitle"
        self.assertEqual(extract_title(markdown), "Main Title")

    def test_title_not_at_start(self):
        markdown = "Some content\n# Main Title\nMore content"
        self.assertEqual(extract_title(markdown), "Main Title")

    def test_no_title(self):
        markdown = "Just some content\nWithout a title"
        with self.assertRaises(ValueError):
            extract_title(markdown)

    def test_multiple_titles(self):
        markdown = "# First Title\n## Subtitle\n# Second Title"
        self.assertEqual(extract_title(markdown), "First Title")

if __name__ == "__main__":
    unittest.main()
