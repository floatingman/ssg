import unittest
from markdown_blocks import markdown_to_html_node

class TestMarkdownToHTML(unittest.TestCase):
    
    def test_single_paragraph(self):
        markdown = "This is a paragraph with **bold** and *italic* text."
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(html_node.tag, "div")
        self.assertEqual(len(html_node.children), 1)
        self.assertEqual(html_node.children[0].tag, "p")
        self.assertEqual(len(html_node.children[0].children), 5)

    def test_multiple_paragraphs(self):
        markdown = "First paragraph.\n\nSecond paragraph."
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(len(html_node.children), 2)
        self.assertEqual(html_node.children[0].tag, "p")
        self.assertEqual(html_node.children[1].tag, "p")

    def test_heading(self):
        markdown = "# Heading 1\n\n## Heading 2"
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(len(html_node.children), 2)
        self.assertEqual(html_node.children[0].tag, "h1")
        self.assertEqual(html_node.children[1].tag, "h2")

    def test_code_block(self):
        markdown = "```\nprint('Hello, World!')\n```"
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(len(html_node.children), 1)
        self.assertEqual(html_node.children[0].tag, "pre")
        self.assertEqual(html_node.children[0].children[0].tag, "code")

    def test_quote(self):
        markdown = "> This is a quote\n> It continues here"
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(len(html_node.children), 1)
        self.assertEqual(html_node.children[0].tag, "blockquote")

    def test_unordered_list(self):
        markdown = "* Item 1\n* Item 2\n* Item 3"
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(len(html_node.children), 1)
        self.assertEqual(html_node.children[0].tag, "ul")
        self.assertEqual(len(html_node.children[0].children), 3)
        self.assertEqual(html_node.children[0].children[0].tag, "li")

    def test_ordered_list(self):
        markdown = "1. First item\n2. Second item\n3. Third item"
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(len(html_node.children), 1)
        self.assertEqual(html_node.children[0].tag, "ol")
        self.assertEqual(len(html_node.children[0].children), 3)
        self.assertEqual(html_node.children[0].children[0].tag, "li")

    def test_mixed_content(self):
        markdown = "# Heading\n\nParagraph\n\n* List item 1\n* List item 2\n\n> Quote"
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(len(html_node.children), 4)
        self.assertEqual(html_node.children[0].tag, "h1")
        self.assertEqual(html_node.children[1].tag, "p")
        self.assertEqual(html_node.children[2].tag, "ul")
        self.assertEqual(html_node.children[3].tag, "blockquote")

if __name__ == '__main__':
    unittest.main()
