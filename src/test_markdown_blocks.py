import unittest
from markdown_blocks import markdown_to_blocks

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



if __name__ == "__main__":
    unittest.main()
