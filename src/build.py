import os
import shutil
import logging
from markdown_blocks import markdown_to_html_node, extract_title

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def copy_directory(source, destination):
    """
    Recursively copy contents from source directory to destination directory.
    
    Args:
    source (str): Path to the source directory
    destination (str): Path to the destination directory
    """
    # First, delete all contents of the destination directory
    if os.path.exists(destination):
        logging.info(f"Cleaning destination directory: {destination}")
        shutil.rmtree(destination)
    
    # Create the destination directory
    os.makedirs(destination, exist_ok=True)
    
    # Walk through the source directory
    for root, dirs, files in os.walk(source):
        # Create corresponding subdirectories in destination
        for dir_name in dirs:
            src_path = os.path.join(root, dir_name)
            dest_path = os.path.join(destination, os.path.relpath(src_path, source))
            os.makedirs(dest_path, exist_ok=True)
            logging.info(f"Created directory: {dest_path}")
        
        # Copy files
        for file_name in files:
            src_file = os.path.join(root, file_name)
            dest_file = os.path.join(destination, os.path.relpath(src_file, source))
            shutil.copy2(src_file, dest_file)
            logging.info(f"Copied file: {dest_file}")

def generate_page(from_path, template_path, dest_path):
    """
    Generate an HTML page from a markdown file using a template.

    Args:
    from_path (str): Path to the source markdown file
    template_path (str): Path to the HTML template file
    dest_path (str): Path where the generated HTML file will be saved
    """
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read the markdown file
    with open(from_path, 'r') as md_file:
        markdown_content = md_file.read()

    # Read the template file
    with open(template_path, 'r') as template_file:
        template_content = template_file.read()

    # Convert markdown to HTML
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()

    # Extract the title
    try:
        title = extract_title(markdown_content)
    except ValueError:
        print(f"Warning: No title found in {from_path}. Using a default title.")
        title = "Untitled Page"

    # Replace placeholders in the template
    full_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    # Ensure the directory for dest_path exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Write the full HTML to the destination file
    with open(dest_path, 'w') as dest_file:
        dest_file.write(full_html)

    print(f"Page generated successfully: {dest_path}")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    """
    Recursively generate HTML pages from markdown files in a directory.

    Args:
    dir_path_content (str): Path to the content directory
    template_path (str): Path to the HTML template file
    dest_dir_path (str): Path to the destination directory for generated HTML files
    """
    for root, _, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith('.md'):
                # Construct the full path to the markdown file
                md_path = os.path.join(root, file)
                
                # Construct the relative path from the content directory
                rel_path = os.path.relpath(md_path, dir_path_content)
                
                # Construct the destination path, replacing .md with .html
                dest_path = os.path.join(dest_dir_path, os.path.splitext(rel_path)[0] + '.html')
                
                # Ensure the destination directory exists
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                
                # Generate the page
                generate_page(md_path, template_path, dest_path)
                
                print(f"Generated: {dest_path}")

    print("All pages generated successfully.")
