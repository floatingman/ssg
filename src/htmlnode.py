class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html not implemented")

    def props_to_html(self):
        if not self.props:
            return None

        props_html = ""

        for key, value in self.props.items():
            props_html += f"{key}={value}"
            props_html += " "

        props_html = props_html.strip()
        return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("value cannot be None")
        if self.tag is None:
            return self.value
        return f"<{self.tag}>{self.props_to_html()}</{self.tag}>"
