import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html
from textnode import TextNode


class TestHTMLNode(unittest.TestCase):

    def test_repr(self):
        node = HTMLNode("div", None, None, {"class": "my-class", "id": "my-id"})
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(div, None, None, {'class': 'my-class', 'id': 'my-id'})",
        )

    def test_to_html(self):
        node = HTMLNode("div", None, None, {"class": "my-class", "id": "my-id"})
        self.assertRaises(NotImplementedError, node.to_html)

    def test_props_to_html(self):
        node = HTMLNode(
            "div", "Hello, world!", None, {"class": "my-class", "id": "my-id"}
        )
        self.assertEqual(node.props_to_html(), f' class="my-class" id="my-id"')

    def test_blank_props_to_html(self):
        node = HTMLNode("div", None, None, None)
        self.assertEqual(node.props_to_html(), "")

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_leafnode_child_class_of_htmlnode(self):
        node = LeafNode("div", None, None)
        assert issubclass(type(node), HTMLNode)

    def test_to_html_with_no_value(self):
        node = LeafNode("div", None, None)
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_with_no_tag(self):
        node = LeafNode(None, "This is a text node", None)
        self.assertEqual(node.to_html(), "This is a text node")

    def test_parentnode_child_class_of_htmlnode(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            {"href": "https://www.goot.dev"},
        )
        assert issubclass(type(node), HTMLNode)

    def test_parentnode_children_argument_not_optional(self):
        node = ParentNode(
            "p",
            None,
            {"href": "https://www.goot.dev"},
        )
        self.assertRaisesRegex(ValueError, "children cannot be None", node.to_html)

    def test_parentnode_requires_tag_argument(self):
        node = ParentNode(
            None,
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            {"href": "https://www.goot.dev"},
        )
        self.assertRaisesRegex(ValueError, "tag cannot be None", node.to_html)

    def test_parentnode_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            {"href": "https://www.goot.dev"},
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

    def test_convert_text_node_to_html(self):
        node = TextNode("This is a text node", "bold")
        leaf_node = text_node_to_html(node)
        self.assertEqual(leaf_node.tag, "b")
        self.assertEqual(leaf_node.value, "This is a text node")
        self.assertEqual(leaf_node.to_html(), "<b>This is a text node</b>")

    def test_convert_text_node_to_html_with_url(self):
        node = TextNode("This is a text node", "link", "https://example.com")
        leaf_node = text_node_to_html(node)
        self.assertEqual(leaf_node.tag, "a")
        self.assertEqual(leaf_node.value, "This is a text node")
        self.assertEqual(leaf_node.props["href"], "https://example.com")
        self.assertEqual(
            leaf_node.to_html(), '<a href="https://example.com">This is a text node</a>'
        )


if __name__ == "__main__":
    unittest.main()
