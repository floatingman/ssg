import unittest

from htmlnode import HTMLNode


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
        node = HTMLNode("div", None, None, {"class": "my-class", "id": "my-id"})
        self.assertEqual(node.props_to_html(), "class=my-class id=my-id")

    def test_none_props_to_html(self):
        node = HTMLNode("div", None, None, None)
        self.assertEqual(node.props_to_html(), None)
