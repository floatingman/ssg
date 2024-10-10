from textnode import TextNode, text_type_bold


def main():
    textnode = TextNode("This is a text node", text_type_bold, "https://www.goot.dev")
    print(textnode)


if __name__ == "__main__":
    main()
