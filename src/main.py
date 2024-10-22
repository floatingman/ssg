from textnode import TextNode, TextType
from build import copy_directory, generate_page, generate_pages_recursive
import logging
import os

def main():
    # Define paths
    content_dir = "content"
    template_path = "template.html"
    public_dir = "public"

    print("Generating pages...")
    generate_pages_recursive(content_dir, template_path, public_dir)

if __name__ == "__main__":
    main()
